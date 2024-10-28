# 🎙️ PDF to Podcast Conversion with LLMs 📄➡️🎧

This repository hosts a pipeline for transforming **PDF files into audio podcasts**! Leveraging advanced **Language Models (LLMs)** and **Text-to-Speech (TTS)** technology, this tool converts textual PDF information into engaging, high-quality audio content. It’s ideal for creators, researchers, or anyone looking to make static documents more accessible through audio.

---

## 📑 Table of Contents
1. [📋 Project Overview](#project-overview)
2. [✨ Features](#features)
3. [🔧 Installation](#installation)
4. [🔄 Workflow](#workflow)
5. [📝 Detailed Steps](#detailed-steps)
    - [📕 Step 1: PDF Text Extraction](#step-1-pdf-text-extraction)
    - [✍️ Step 2: Podcast Script Generation](#step-2-podcast-script-generation)
    - [🛠️ Step 3: Transcript Refinement](#step-3-transcript-refinement)
    - [🎙️ Step 4: Audio Generation](#step-4-audio-generation)
6. [📋 Requirements](#requirements)
7. [🚀 Usage](#usage)
8. [📂 File Structure](#file-structure)
9. [🙏 Acknowledgments](#acknowledgments)

---

## 📋 Project Overview
This project uses **modern LLMs** and **TTS technology** to automate the conversion of PDFs into audio podcasts. Built on **Llama 3.1 8b** and high-quality TTS models (Parler and Bark), this tool delivers a seamless process from raw PDF to professional-sounding podcast with minimal manual input. The modular Jupyter Notebook structure makes each step transparent and easy to customize.

---

## ✨ Features
- **📄 Automated PDF Text Extraction**: Quickly extracts text from PDFs, accommodating various formats.
- **🧠 LLM-Driven Content Generation**: Creates scripts that are rephrased and summarized for podcast-style delivery.
- **📝 Script Refinement**: Enhances readability and flow, tailoring content for audio listeners.
- **🎙️ Natural Sounding TTS Output**: Uses Parler and Bark TTS models to produce clear, natural-sounding audio.

---

## 🔧 Installation
To set up the environment, ensure **Python** is installed, then execute:
```bash
pip install -r requirements.txt
```
This installs dependencies, including foundational packages like `torch` and `transformers` needed for TTS and NLP tasks.

---

## 🔄 Workflow
The project workflow includes four primary stages, each with a dedicated notebook:
1. **Extract Text** 📄 from the PDF.
2. **Generate Podcast Script** 📝 using Llama 3.1 8b.
3. **Refine Script** ✍️ for clarity and flow.
4. **Synthesize Audio** 🎧 for podcast-ready MP3 output.

---

## 📝 Detailed Steps

### 📕 Step 1: PDF Text Extraction
- **Notebook**: `Step1_PDF_preprocessing.ipynb`
- **Purpose**: Extracts text from PDF documents for easy processing.
- **Libraries**: Utilizes `PyPDF2` for PDF parsing.
- **Process**:
  - Converts each PDF page into cleaned text.
  - Saves extracted text as a `.txt` file, ready for LLM processing.

### ✍️ Step 2: Podcast Script Generation
- **Notebook**: `Step2_Transcript_Writer.ipynb`
- **Purpose**: Uses Llama 3.1 8b to summarize and rephrase content for audio.
- **Highlights**:
  - The LLM converts extracted text into a listener-friendly script.
  - Produces a draft script saved as a text file for refinement.

### 🛠️ Step 3: Transcript Refinement
- **Notebook**: `Step3_Rewriter.ipynb`
- **Purpose**: Polishes the initial script, optimizing it for audio narration.
- **Process**:
  - Improves readability and conversational flow.
  - Reduces redundancy and clarifies complex ideas.

### 🎙️ Step 4: Audio Generation
- **Notebook**: `Step4_TTS_Workflow.ipynb`
- **Purpose**: Converts the refined script into high-quality audio.
- **Models Used**: Combines **Parler** and **Bark** TTS models.
- **Output**: Creates an `.mp3` file that’s ready for playback or distribution.

---

## 📋 Requirements
The `requirements.txt` file provides a comprehensive list of dependencies, including:
- **NLP and LLM**: `transformers`, `torch`, `datasets`
- **PDF Parsing**: `PyPDF2`
- **Audio Processing**: `pydub`, `audioread`, `librosa`
- **TTS Models**: `parler_tts`, `bark`

### Key Dependencies
- **LLM Processing**: `transformers`, `torch`
- **Text Extraction**: `PyPDF2`
- **Audio Tools**: `pydub`

---

## 🚀 Usage
1. **Prepare PDF Files** 📄: Place PDFs in a folder accessible to the notebooks.
2. **Run Notebooks Sequentially**:
   - **Step 1**: Run `Step1_PDF_preprocessing.ipynb` to extract text.
   - **Step 2**: Run `Step2_Transcript_Writer.ipynb` to create a script.
   - **Step 3**: Run `Step3_Rewriter.ipynb` to refine the script.
   - **Step 4**: Run `Step4_TTS_Workflow.ipynb` to generate audio.
3. **Review Output** 📄: Check the output at each step to ensure quality.

---

## 📂 File Structure
The project includes the following files:
- **`Step1_PDF_preprocessing.ipynb`**: PDF text extraction.
- **`Step2_Transcript_Writer.ipynb`**: Script generation.
- **`Step3_Rewriter.ipynb`**: Script refinement.
- **`Step4_TTS_Workflow.ipynb`**: Audio synthesis.
- **`requirements.txt`**: Lists all dependencies.

---

## 🙏 Acknowledgments
This project is powered by the amazing open-source tools provided by:
- **Meta AI** for the **Llama 3.1 8b** language model.
- **Parler and Bark TTS** for high-quality audio generation.
- **PyPDF2** and **Pydub** for essential PDF and audio handling.

---

## 🔗 General Links & Resources

- **Our Website:** [www.apcmasterypath.co.uk](https://www.apcmasterypath.co.uk)
- **APC Mastery Path Blogposts:** [APC Blogposts](https://www.apcmasterypath.co.uk/blog-list)
- **LinkedIn Pages:** [Personal](https://www.linkedin.com/in/mohamed-ashour-0727/) | [APC Mastery Path](https://www.linkedin.com/company/apc-mastery-path)
