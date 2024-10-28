# PDF to Podcast Conversion with LLMs

This repository hosts a pipeline for transforming PDF files into audio podcasts. The project utilizes advanced Language Models (LLMs) and Text-to-Speech (TTS) models to create high-quality, engaging audio content from textual information in PDF documents. The pipeline is broken down into four main steps: text extraction, podcast script generation, transcript refinement, and audio synthesis. The project is well-suited for creators, researchers, or anyone interested in converting static document content into accessible audio formats.

## Table of Contents
1. [Project Overview](#Project-Overview)
2. [Features](#Features)
3. [Installation](#Installation)
4. [Workflow](#Workflow)
5. [Detailed Steps](#Detailed-Steps)
    - [Step 1: PDF Text Extraction](#Step-1-pdf-text-extraction)
    - [Step 2: Podcast Script Generation](#Step-2-podcast-script-generation)
    - [Step 3: Transcript Refinement](#Step-3-transcript-refinement)
    - [Step 4: Audio Generation](#Step-4-audio-generation)
6. [Requirements](#Requirements)
7. [Usage](#Usage)
8. [File Structure](#File-Structure)
9. [Acknowledgments](#Acknowledgments)

## Project Overview
This project leverages modern language models and text-to-speech technology to automate the conversion of PDFs into audio podcasts. Using the power of Llama 3.1 8b and high-quality TTS models (Parler and Bark), the process delivers a smooth, streamlined experience, enabling users to go from a raw PDF to a professionally sounding podcast with minimal manual input. The modular structure allows for customization, and each step is broken down into Jupyter Notebooks for clear visibility into each phase of the process.

## Features
- **Automated PDF Text Extraction**: Streamlines text extraction from PDFs, with flexibility for a variety of document formats.
- **LLM-Driven Content Generation**: Creates podcast-friendly scripts that rephrase and summarize information in an engaging way.
- **Script Refinement**: Enhances readability and structure for an audio-first format, focusing on listener engagement.
- **Natural Sounding TTS Output**: Generates high-quality audio using a combination of Parler and Bark TTS models, balancing voice clarity and natural cadence.

## Installation
To set up the environment for this project, ensure that Python is installed and execute:
```bash
pip install -r requirements.txt
```

This installs all necessary libraries and dependencies listed in `requirements.txt`, including foundational packages like `torch`, `transformers`, and others required for TTS and NLP functionalities.

## Workflow
The project workflow involves four main stages, each with its own dedicated notebook:
1. **Extract text** from the PDF document.
2. **Generate a podcast-friendly script** using Llama 3.1 8b instruct.
3. **Refine the generated script** to ensure clarity and flow.
4. **Create an audio file** by synthesizing the refined script into speech.

## Detailed Steps

### Step 1: PDF Text Extraction
- **File**: `Step1_PDF_preprocessing.ipynb`
- **Purpose**: This notebook handles the text extraction phase. It reads PDF documents and converts them into plain text, enabling easier processing for subsequent steps.
- **Libraries Used**: `PyPDF2` for PDF parsing and text extraction.
- **Workflow**:
  - Each page of the PDF is processed to capture and clean text.
  - The extracted text is saved as a `.txt` file, providing a raw input for the LLMs to interpret.
- **Considerations**: Handles different PDF structures by removing extraneous formatting, though results may vary depending on PDF complexity and layout.

### Step 2: Podcast Script Generation
- **File**: `Step2_Transcript_Writer.ipynb`
- **Purpose**: Using the extracted text, this notebook creates a podcast-ready script by rephrasing and summarizing the document content into a listener-friendly format.
- **Model Used**: Llama 3.1 8b instruct.
- **Workflow**:
  - The extracted text from Step 1 is provided to the Llama model, which reinterprets the information, targeting clarity, conciseness, and flow.
  - The script is stored as a text file, ready for further refinement.
- **Highlights**: Employs context-aware generation to enhance the script’s narrative quality and adapt complex ideas for audio presentation.

### Step 3: Transcript Refinement
- **File**: `Step3_Rewriter.ipynb`
- **Purpose**: This step refines the initial podcast script to enhance readability and ensure the narrative flow is natural and conversational.
- **Model Used**: Llama 3.1 8b instruct (same as Step 2).
- **Workflow**:
  - The generated script undergoes a second pass through the LLM, where it is further polished.
  - Focus is placed on improving sentence structure, reducing redundancy, and clarifying complex phrases.
  - The refined script is saved, forming the final text for audio synthesis.
- **Benefits**: This step ensures the script is optimized for TTS conversion, reducing errors in pronunciation and intonation.

### Step 4: Audio Generation
- **File**: `Step4_TTS_Workflow.ipynb`
- **Purpose**: Converts the refined script into an audio file, suitable for podcast distribution.
- **Models Used**: Parler TTS and Bark TTS.
- **Workflow**:
  - The finalized script is processed by Parler and Bark TTS models, which convert the text into high-quality audio.
  - The outputs from both models are combined into a single, coherent `.mp3` file, ready for playback or publishing.
- **Output**: An MP3 file with natural-sounding audio, capturing the essence of the document in a podcast format.

## Requirements
The `requirements.txt` file provides a comprehensive list of dependencies. Key libraries include:
- `transformers`: For interaction with language models.
- `torch`: Provides the core foundation for deep learning model support.
- `pydub`: Used for processing and combining audio files.
- `PyPDF2`: Enables PDF parsing and text extraction from documents.

Additionally, the Parler and Bark models are included through GitHub links, providing access to TTS models specifically suited to this project.

### Key Dependencies in `requirements.txt`:
- NLP and LLM: `transformers`, `torch`, `datasets`
- PDF Parsing: `PyPDF2`
- Audio Processing: `pydub`, `audioread`, `librosa`
- TTS Models: `parler_tts`, `bark`

## Usage
1. **Prepare PDF Files**: Place the PDFs you want to convert in a folder accessible to the notebook.
2. **Execute Each Notebook Sequentially**:
   - Open `Step1_PDF_preprocessing.ipynb` and run all cells to generate a text file from your PDF.
   - Open `Step2_Transcript_Writer.ipynb` to create an initial podcast script.
   - Open `Step3_Rewriter.ipynb` to refine the script.
   - Open `Step4_TTS_Workflow.ipynb` to generate and combine audio into a single MP3 file.
3. **Review and Quality Check**: After each step, review the output to ensure content quality and accuracy.

## File Structure
The following files are included in the project:
- **`Step1_PDF_preprocessing.ipynb`**: Notebook for text extraction from PDFs.
- **`Step2_Transcript_Writer.ipynb`**: Notebook for generating an initial podcast script.
- **`Step3_Rewriter.ipynb`**: Notebook for refining the transcript.
- **`Step4_TTS_Workflow.ipynb`**: Notebook for generating audio files.
- **`requirements.txt`**: Lists all dependencies for easy setup.

## Acknowledgments
This project leverages models and libraries from multiple sources:
- **Meta AI** for the Llama 3.1 8b language model, used in both script generation and refinement.
- **Parler and Bark TTS** for their robust text-to-speech models, providing high-quality audio outputs.
- **PyPDF2** and **Pydub** for essential PDF and audio processing utilities.

Special thanks to the open-source community for providing these tools, enabling streamlined PDF-to-audio workflows.
