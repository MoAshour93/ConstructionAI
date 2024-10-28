# 📄 PDF Text Extraction & Markdown Cleansing with `marker-pdf` 📚

Welcome to the **PDF Text Extraction & Markdown Cleansing** project! This repository leverages the `marker-pdf` library to streamline the transformation of PDF content into clean, structured Markdown format. Designed with **RICS APC candidates** in mind, this project not only extracts text but also refines it into a standard format suitable for competency and experience documentation, making it ready for integration into broader data pipelines and machine learning applications.

---

## 📑 Table of Contents
1. [📋 Project Overview](#project-overview)
2. [✨ Key Features](#key-features)
3. [🔧 Installation & Setup](#installation--setup)
4. [🚀 Workflow](#workflow)
5. [📝 Usage Guide](#usage-guide)
    - [1️⃣ Terminal Commands for Text Extraction](#1️⃣-terminal-commands-for-text-extraction)
    - [2️⃣ Streamlit App for Markdown Cleansing](#2️⃣-streamlit-app-for-markdown-cleansing)
6. [📂 Folder Structure](#folder-structure)
7. [🔗 General Links & Resources](#-general-links--resources)

---

## 📋 Project Overview

This project provides two main functionalities:

1. **Text Extraction**: Using `marker-pdf`, users can extract text data from single or multiple PDF files, saving each document’s content in Markdown format within the original file directory.

2. **Markdown Cleansing and Standardization**: A Streamlit app enables users to convert raw, unformatted RICS APC Markdown content into a cleaner, standardized format. This step organizes competencies, aligns their levels, formats experience summaries, and removes irrelevant details—ideal for constructing a consistent dataset for machine learning purposes or further NLP applications.

---

## ✨ Key Features

- **Flexible Text Extraction** 📝: Extract text from one or multiple PDFs simultaneously, saving each as a Markdown file.
- **RICS APC Format Cleansing** 🔍: Refines RICS APC Markdown files to ensure content is readable and standardized.
- **Streamlit Integration** 💻: A user-friendly interface for document cleansing, no coding experience needed!
- **Database-Ready Output** 🗃️: Creates a standardized dataset, ready to integrate with machine learning models for fine-tuning.
- **Supports Model Training** 🎓: Processed content can be used to fine-tune any chosen large language model, enhancing the model’s familiarity with domain-specific language and competency formats.

---

## 🔧 Installation & Setup

To get started, clone this repository and install the necessary libraries by running:

```bash
python -m venv parse_pdfs #Creating a virtual environment named parse_pdfs
parse_pdfs\Scripts\activate #Activating the newly created virtual environment
pip install marker-pdf streamlit markdownify #Installing marker-pdf, markdownify and streamlit packages
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 #installing pytorch with cuda 12.1 from source
```

This command installs dependencies, including **marker-pdf** for text extraction, **markdownify** for conversion tasks, and **Streamlit** for app deployment.

---

## 🚀 Workflow

This project follows a two-part workflow:

1. **Text Extraction** 📝: Extracts text from PDF files into Markdown format.
2. **Content Cleansing** 🔄: Streamlines Markdown content with the Streamlit app, standardizing and cleaning up the RICS APC format.

---

## 📝 Usage Guide

### 1️⃣ Terminal Commands for Text Extraction
Utilize `marker-pdf` to convert PDF content into Markdown files directly from the terminal:

1. **Single PDF**: To extract text from a single PDF file, navigate to the desired directory and run terminal within that directory:
    ```bash
    marker_single /path/to/file.pdf /path/to/output/folder --batch_multiplier 2 --max_pages 10 --langs English
    ```

2. **Multiple PDFs**: Extract text from multiple files within a directory, navigate to the desired directory and run terminal within that directory::
    ```bash
    marker /path/to/input/folder /path/to/output/folder --workers 10 --max 10 --metadata_file /path/to/metadata.json --min_length 10000
    ```

Markdown files are saved in the same directory as the original PDFs for easy access.

### 2️⃣ Streamlit App for Markdown Cleansing
The **Streamlit app** provides a straightforward way to cleanse and standardize Markdown files with unformatted RICS APC content:

1. **Run the Streamlit App**:
    ```bash
    streamlit run app.py
    ```
   
2. **Upload Markdown Content** 📄: Feed in raw Markdown files generated from PDF text extraction.
3. **Automated Cleansing** 🔧: The app automatically formats competencies, adjusts experience summaries, and removes irrelevant symbols or text, creating a polished Markdown file.
4. **Save Output** 💾: Download the cleansed Markdown files, ready for integration into databases or for LLM fine-tuning.

---

## 📂 Folder Structure

- **converted_pdf**: Encompasses the extracted data from the pdf as well as the cleansed extracted data.
- **data**: encompasses the original pdf.
- **Jupyter Notebook**: Demonstrates step-by-step implementation of terminal commands and app deployment.

---

## 🔗 General Links & Resources

- **Our Website**: [www.apcmasterypath.co.uk](https://www.apcmasterypath.co.uk)
- **APC Mastery Path Blogposts**: [APC Blogposts](https://www.apcmasterypath.co.uk/blog-list)
- **LinkedIn Pages**: [Personal](https://www.linkedin.com/in/mohamed-ashour-0727/) | [APC Mastery Path](https://www.linkedin.com/company/apc-mastery-path)
