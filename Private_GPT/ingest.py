# Installing required packages
# Uncomment and run if these packages are not already installed
# !pip install os
# !pip install glob
# !pip install langchain
# !pip install python-dotenv
# !pip install chromadb
# !pip install sentence-transformers
# !pip install transformers

# Importing necessary libraries
import os  # To interact with the operating system, such as reading environment variables
import glob  # For file pattern matching (used to find documents)
import chromadb  # For vector storage and embeddings

# Importing additional components from specific packages
from chromadb.config import Settings  # Settings configuration for ChromaDB
from typing import List  # For type hinting lists
from dotenv import load_dotenv  # To load environment variables from a .env file
from multiprocessing import Pool  # Enables parallel processing for efficiency
from tqdm import tqdm  # For progress bar functionality

# Importing document loaders for various file types
from langchain.document_loaders import (
    CSVLoader,
    EverNoteLoader,
    TextLoader,
    UnstructuredEmailLoader,
    UnstructuredHTMLLoader,
    UnstructuredMarkdownLoader,
    UnstructuredODTLoader,
    UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredEPubLoader,
    UnstructuredHTMLLoader,
    UnstructuredMarkdownLoader,
    PyMuPDFLoader,
    PyPDFLoader
)

# Importing additional LangChain components for document processing and embeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.docstore.document import Document
from constants import CHROMA_SETTINGS  # Import Chroma settings defined in constants.py

# Load environment variables
if not load_dotenv():
    print("Could not load .env file or it is empty. Please check it exists and is readable.")
    exit(1)  # Exit if environment variables cannot be loaded

# Configurable parameters
chunk_size = 1000  # Max token size for each text chunk
chunk_overlap = 100  # Overlap size for chunk splitting
persist_directory = os.environ.get('PERSIST_DIRECTORY')  # Directory for storing Chroma vectors
source_directory = os.environ.get('SOURCE_DIRECTORY', 'source_documents')  # Source directory for documents
embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME')  # Embeddings model name

# Mapping of file extensions to their respective document loaders
LOADER_MAPPING = {
    ".csv": (CSVLoader, {}),
    ".doc": (UnstructuredWordDocumentLoader, {}),
    ".docx": (UnstructuredWordDocumentLoader, {}),
    ".enex": (EverNoteLoader, {}),
    ".epub": (UnstructuredEPubLoader, {}),
    ".html": (UnstructuredHTMLLoader, {}),
    ".md": (UnstructuredMarkdownLoader, {}),
    ".odt": (UnstructuredODTLoader, {}),
    ".ppt": (UnstructuredPowerPointLoader, {}),
    ".pptx": (UnstructuredPowerPointLoader, {}),
    ".pdf": (PyMuPDFLoader, {}),
    ".txt": (TextLoader, {"encoding": "utf8"})
}

# Function to load a single document based on its file extension
def load_single_document(file_path: str) -> List[Document]:
    """
    Loads a single document based on the file extension and returns a list of Document objects.
    """
    ext = "." + file_path.rsplit(".", 1)[-1].lower()  # Extract the file extension
    if ext in LOADER_MAPPING:
        loader_class, loader_args = LOADER_MAPPING[ext]
        loader = loader_class(file_path, **loader_args)
        return loader.load()
    raise ValueError(f"Unsupported file extension '{ext}'")  # Error if extension is unsupported

# Function to load multiple documents from the specified directory
def load_documents(source_dir: str, ignored_files: List[str] = []) -> List[Document]:
    """
    Loads all documents from the specified directory, ignoring files in ignored_files list.
    """
    all_files = []  # List to store file paths
    for ext in LOADER_MAPPING:
        # Find all files with each extension (case insensitive) and add to the list
        all_files.extend(glob.glob(os.path.join(source_dir, f"**/*{ext.lower()}"), recursive=True))
        all_files.extend(glob.glob(os.path.join(source_dir, f"**/*{ext.upper()}"), recursive=True))
    # Filter out ignored files
    filtered_files = [file_path for file_path in all_files if file_path not in ignored_files]
    
    # Load documents in parallel to speed up processing
    with Pool(processes=os.cpu_count()) as pool:
        results = []
        with tqdm(total=len(filtered_files), desc='Loading new documents', ncols=80) as pbar:
            for i, docs in enumerate(pool.imap_unordered(load_single_document, filtered_files)):
                results.extend(docs)
                pbar.update()  # Update progress bar
    return results

# Function to process documents and split them into chunks for embedding
def process_documents(ignored_files: List[str] = []) -> List[Document]:
    """
    Load documents, split them into smaller chunks, and return the chunks.
    """
    print(f"Loading documents from {source_directory}")
    documents = load_documents(source_directory, ignored_files)
    if not documents:
        print("No new documents to load")
        exit(0)  # Exit if no documents are found
    print(f"Loaded {len(documents)} new documents from {source_directory}")
    # Initialize the text splitter with defined chunk size and overlap
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_documents(documents)
    print(f"Split into {len(texts)} chunks of text (max. {chunk_size} tokens each)")
    return texts

# Function to check if a VectorStore (embedding storage) exists in the specified directory
def does_vectorstore_exist(persist_directory: str, embeddings: HuggingFaceBgeEmbeddings) -> bool:
    """
    Checks if a VectorStore with embeddings already exists in the specified directory.
    """
    db = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    # If there are no documents, return False; otherwise, True
    return bool(db.get()['documents'])

# Main function to execute the embedding and storage process
def main():
    # Initialize embeddings using the specified HuggingFace model
    embeddings = HuggingFaceBgeEmbeddings(model_name=embeddings_model_name)
    # Create a Chroma client with defined settings
    chroma_client = chromadb.PersistentClient(settings=CHROMA_SETTINGS, path=persist_directory)
    
    # Check if a vectorstore already exists
    if does_vectorstore_exist(persist_directory, embeddings):
        print(f"Appending to existing vectorstore at {persist_directory}")
        db = Chroma(persist_directory=persist_directory, embedding_function=embeddings,
                    client_settings=CHROMA_SETTINGS, client=chroma_client)
        collection = db.get()
        # Process documents, ignoring those already stored
        texts = process_documents([metadata['source'] for metadata in collection['metadatas']])
        print("Creating embeddings. This may take a few minutes...")
        db.add_documents(texts)  # Add new embeddings
    else:
        print("Creating new vectorstore")
        texts = process_documents()
        print("Creating embeddings. This may take a few minutes...")
        db = Chroma.from_documents(texts, embeddings, persist_directory=persist_directory,
                                   client_settings=CHROMA_SETTINGS, client=chroma_client)
    
    db.persist()  # Save vectorstore to disk
    db = None  # Close connection
    print("Ingestion complete! You can now run PrivateGPT.py to query your documents.")

# Execute the main function when the script runs
if __name__ == "__main__":
    main()
