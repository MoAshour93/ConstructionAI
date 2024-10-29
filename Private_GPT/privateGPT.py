# Import required libraries
import chromadb  # For managing ChromaDB, the vector storage
import os  # To handle operating system operations and environment variables
import argparse  # For parsing command-line arguments
import time  # To measure response time for answering queries
from dotenv import load_dotenv  # To load environment variables from a .env file
from langchain.chains import RetrievalQA  # To handle question-answering with retrieval
from langchain.embeddings import HuggingFaceBgeEmbeddings  # For embedding text with HuggingFace models
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler  # For streaming responses
from langchain.vectorstores import Chroma  # For Chroma vector store management
from langchain.llms import GPT4All, Llamacpp  # For handling different LLMs (GPT-4All and LlamaCpp)
from constants import CHROMA_SETTINGS  # Import Chroma configuration settings

# Load environment variables from the .env file if it exists
if not load_dotenv():
    print("Could not load .env file or it is empty. Please check if it exists and is readable.")
    exit(1)  # Exit if loading the environment file fails

# Retrieve environment variables for model and storage configurations
embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")  # Name of embeddings model
persist_directory = os.environ.get("PERSIST_DIRECTORY")  # Directory path for Chroma database storage
model_type = os.environ.get("MODEL_TYPE")  # Model type (e.g., "GPT4ALL" or "LlamaCpp")
model_path = os.environ.get("MODEL_PATH")  # Path to the model file
model_n_ctx = os.environ.get("MODEL_N_CTX")  # Context size for the model
model_n_batch = int(os.environ.get("MODEL_N_BATCH"), 8)  # Batch size for processing
target_source_chunks = int(os.environ.get("TARGET_SOURCE_CHUNKS"), 4)  # Number of chunks for retrieval

# Main function to initialize the LLM, ChromaDB, and embedding model and manage the Q&A interaction
def main():
    # Parse command-line arguments for configuring source visibility and streaming
    args = parse_arguments()
    
    # Initialize the embeddings model
    embeddings = HuggingFaceBgeEmbeddings(model_name=embeddings_model_name)
    
    # Set up a persistent Chroma client with pre-defined settings
    chroma_client = chromadb.PersistentClient(settings=CHROMA_SETTINGS, path=persist_directory)
    
    # Initialize the Chroma database for retrieval with the embedding function
    db = Chroma(persist_directory=persist_directory, embedding_function=embeddings,
                client_settings=CHROMA_SETTINGS, client=chroma_client)
    
    # Define the retriever to return a specified number of document chunks for each query
    retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
    
    # Define the callback list for streaming output if streaming is enabled
    callbacks = [] if args.mute_stream else [StreamingStdOutCallbackHandler()]
    
    # Initialize the language model based on the model type specified in the environment variable
    match model_type:
        case "LlamaCpp":
            # Set up LlamaCpp model with required parameters
            llm = Llamacpp(model_path=model_path, max_tokens=model_n_ctx,
                           n_batch=model_n_batch, callbacks=callbacks, verbose=False)
        case "GPT4ALL":
            # Set up GPT4All model with the necessary parameters
            llm = GPT4All(model=model_path, max_tokens=model_n_ctx, backend='gptj',
                          n_batch=model_n_batch, callbacks=callbacks, verbose=False)
        case _default:
            # Raise an error if an unsupported model type is specified
            raise Exception(f"Model Type {model_type} is not supported. Please choose either 'LlamaCpp' or 'GPT4All'")
    
    # Initialize the question-answering chain with the LLM and document retriever
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever,
                                     return_source_documents=not args.hide_source)
    
    # Start an interactive Q&A loop
    while True:
        # Prompt the user to enter a query
        query = input("\n Enter a query: ")
        
        # Exit the loop if the user types "exit"
        if query == "exit":
            break
        # Skip empty queries
        if query.strip() == "":
            continue
        
        # Process the query and measure the time taken
        start = time.time()
        res = qa(query)
        answer = res['result']
        docs = [] if args.hide_source else res['source_documents']
        end = time.time()
        
        # Print the question and the answer
        print("\n\n > Question:")
        print(query)
        print(f"\n> Answer (took {round(end - start, 2)}s.):")
        print(answer)
        
        # Display the source documents used for the answer if enabled
        for document in docs:
            print("\n> " + document.metadata["source"] + ":")
            print(document.page_content)

# Function to parse command-line arguments for toggling source visibility and streaming output
def parse_arguments():
    parser = argparse.ArgumentParser(description='PrivateGPT: Ask questions to your documents without an internet connection,'
                                                 ' using the power of LLMs.')
    parser.add_argument("--hide-source", "-S", action='store_true',
                        help='Use this flag to disable printing of source documents used for answers.')
    parser.add_argument("--mute-stream", "-M", action='store_true',
                        help='Use this flag to disable the streaming StdOut callback for LLMs.')
    return parser.parse_args()

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
