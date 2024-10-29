# 📄 GPT-4ALL Document Query Chatbot

This project enables users to query a wide variety of documents using an advanced chatbot powered by open-source LLMs like GPT-4ALL and Llama. Leveraging embeddings, vector databases, and data loaders, this system efficiently handles document parsing, storage, and retrieval. 

## 📌 Project Overview

In today’s data-intensive environments, there’s a growing need to convert unstructured data into actionable insights. This chatbot bridges that gap by allowing users to interactively query documents, with support for multiple formats including PDF, Word, PowerPoint, Markdown, and more.

Built with `langchain` and `chromadb`, this solution processes documents by:
- Converting them into text chunks.
- Embedding these chunks as vectors.
- Storing them for easy retrieval, powered by a selected LLM model.

---

## 🚀 Features
- **Multi-format Document Support**: Accepts documents in `.pdf`, `.docx`, `.pptx`, `.txt`, and other formats.
- **Embeddings with Langchain**: Uses `HuggingFaceBgeEmbeddings` for text chunk embeddings.
- **Vector Storage with ChromaDB**: Stores text embeddings as vectors for efficient retrieval.
- **Choice of LLMs**: Supports GPT-4ALL and Llama models for answering queries.
- **Customizable Environment**: Easily configure model and embedding options via `.env`.

---

## 📂 Project Structure

- `requirements.txt`: Lists necessary Python packages.
- `.env`: Contains environment variables for model and database settings.
- `constants.py`: Holds constants for Chroma database configuration.
- `ingest.py`: Processes and stores documents as vectors for future querying.
- `privateGPT.py`: Main chatbot script for querying stored documents.

---

## 🛠 Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/gpt4all-document-query-chatbot.git
    cd gpt4all-document-query-chatbot
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
   - Create a `.env` file in the root directory, using the provided template:
     ```bash
     PERSIST_DIRECTORY=db
     MODEL_TYPE=GPT4All
     MODEL_PATH=models/ggml-gpt4all-j-v1.3-groovy.bin
     EMBEDDINGS_MODEL_NAME=all-MiniLM-L6-v2
     MODEL_N_CTX=1000
     MODEL_N_BATCH=8
     TARGET_SOURCE_CHUNKS=4
     ```

---

## 🚀 Usage

### 1. Ingest Documents
   Use `ingest.py` to process and store document embeddings:
   ```bash
   python ingest.py
   ```

### 2. Run the Chatbot
   Start querying documents using `privateGPT.py`:
   ```bash
   python privateGPT.py
   ```
   - Enter your query at the prompt.
   - Type `exit` to end the session.

### 🔧 Customizable Options
   - Use `--hide-source` or `-S` to hide source documents used in responses.
   - Use `--mute-stream` or `-M` to disable streaming output from the LLM.

---

## 🔗 General Links & Resources

- **Our Website**: [www.apcmasterypath.co.uk](https://www.apcmasterypath.co.uk)
- **APC Mastery Path Blogposts**: [APC Blogposts](https://www.apcmasterypath.co.uk/blog-list)
- **LinkedIn Pages**: [Personal](https://www.linkedin.com/in/mohamed-ashour-0727/) | [APC Mastery Path](https://www.linkedin.com/company/apc-mastery-path)

---

## ⚙️ Configuration

- **Constants**: The `constants.py` file includes important settings for the ChromaDB database.
- **Environment Variables**: Set customizable parameters in `.env`, including model path and embedding model name.

---

## 🗂️ Supported Document Formats

| Format          | Loader                        |
|-----------------|-------------------------------|
| PDF             | `PyPDFLoader`                 |
| Word Documents  | `UnstructuredWordDocumentLoader` |
| PowerPoint      | `UnstructuredPowerPointLoader` |
| Markdown        | `UnstructuredMarkdownLoader`  |
| CSV             | `CSVLoader`                   |
| Text            | `TextLoader`                  |

---

## 📈 Limitations & Next Steps

This initial implementation is a command-line-based chatbot, but it can be extended:
1. **GUI Integration**: Integrate with `Streamlit` or `Chainlit` for a graphical user interface.
2. **Multi-agent Architecture**: Develop task-specific agents for more complex queries.
3. **Broader LLM Support**: Experiment with other open-source models from Hugging Face.

---

## 📄 License
This project is licensed under the [Apache 2.0 License](LICENSE).

---

## 📞 Support
For any questions, feel free to contact [Mohamed Ashour](https://www.linkedin.com/in/mohamed-ashour-0727/).
