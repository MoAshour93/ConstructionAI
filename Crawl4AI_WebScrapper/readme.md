# 🕸️ Web Scraper App with Streamlit - Crawl4AI 🌐

This repository provides a user-friendly **web scraping tool** built using **Streamlit**, inspired by the **Crawl4AI** library. This app lets users scrape content from web pages, convert it into Markdown format, and download the cleaned text—accessible through an intuitive interface! 🚀

## 📑 Table of Contents
1. [📋 Project Overview](#project-overview)
2. [✨ Features](#features)
3. [🔧 Installation](#installation)
4. [📂 Application Structure](#application-structure)
5. [🔍 Detailed Steps](#detailed-steps)
6. [💾 Creating an Executable File](#creating-an-executable-file)
7. [🚀 Usage](#usage)
8. [🙏 Acknowledgments](#acknowledgments)

---

## 📋 Project Overview
This project streamlines web scraping, processing, and downloading text content in **Markdown format**. Leveraging **Streamlit** for the frontend and **Crawl4AI** for scraping, it provides an accessible tool for non-technical users with a visually appealing interface and easy download options.

---

## ✨ Features
- **🌐 Web Scraping**: Extract HTML content from a given URL.
- **🔄 HTML to Markdown Conversion**: Easily convert scraped HTML to Markdown for readability.
- **🎨 Customizable Frontend Styling**: Enhanced user experience with sleek CSS styling.
- **📥 Downloadable Output**: Save content in Markdown format with a convenient download link.
- **💻 Executable Deployment**: Use a shell script to deploy and run the app effortlessly.

---

## 🔧 Installation
To set up the environment and install dependencies, follow these steps:

1. **Create a Virtual Environment**:
    ```bash
    pip install virtualenv
    python3 -m venv crawl4ai
    source crawl4ai/bin/activate
    ```

2. **Install Requirements**:
    ```bash
    pip install streamlit crawl4ai crawl4ai[sync] markdownify beautiful-soup requests
    ```

---

## 📂 Application Structure
The codebase is organized into distinct sections for easy navigation:
- **🎨 Custom Styling**: CSS styling for an enhanced app experience.
- **🔧 Helper Functions**:
    - **Adjust Resource URLs**: Ensures images display correctly by converting relative URLs.
    - **HTML to Markdown Conversion**: Retains essential formatting during HTML-to-Markdown conversion.
    - **Markdown Cleanup**: Refines the Markdown output.
    - **Download Link Creation**: Generates a downloadable Markdown file link.
- **🖥️ Main App**: User interface and core functionality.

---

## 🔍 Detailed Steps

### Step 1: Setting up the Coding Environment
- **Install Required Libraries**: Follow the steps in the installation section.
- **Activate the Virtual Environment**: For a contained setup.

### Step 2: Styling the Streamlit App
- Custom CSS styling enhances visual elements, making the app user-friendly with functions like `apply_custom_styles`.

### Step 3: Helper Functions
- **adjust_resource_urls** 🖼️: Ensures images display correctly by converting URLs.
- **html_to_markdown** 📜: Converts HTML into Markdown with `markdownify`, retaining structure.
- **clean_markdown** ✨: Ensures a neat Markdown format.
- **download_markdown** 📥: Creates a downloadable Markdown file.

### Step 4: Enabling Markdown Download
- Users can download scraped content as a `.md` file, thanks to a custom download link in the Streamlit interface.

### Step 5: Main Streamlit App Interface
The `main` function builds the Streamlit app interface:
- **🌐 URL Input**: Enter the URL of the web page to scrape.
- **🚀 Scrape Button**: Activates the scraping process.
- **📄 Output Display**: Shows the converted Markdown content.
- **📥 Download Button**: Provides a link to download the Markdown file.

---

## 💾 Creating an Executable File
For easy deployment, create a shell script to run the app without needing the terminal.

1. **Navigate to Your Project Directory**:
    ```bash
    cd ~/Path_to_Your_Project_Folder
    ```

2. **Create a Shell Script**:
    ```bash
    nano run_webscraper.sh
    ```

3. **Add the Following Content**:
    ```bash
    #!/bin/bash
    # Activate the virtual environment
    source ~/Path_to_Your_Project_Folder/crawl4ai/bin/activate

    # Run the Streamlit app
    streamlit run ~/Path_to_Your_Project_Folder/webscrapping_CrawlAI_enhanced.py
    ```

4. **Save and Make the Script Executable**:
    ```bash
    chmod +x run_webscraper.sh
    ```

5. **Run the Script**: You can launch the app by running this script or selecting "Run as a program" (on supported systems).

---

## 🚀 Usage
1. **Launch the App**: Run the shell script (`run_webscraper.sh`) or execute directly from the terminal.
2. **Input a URL**: Enter the URL of the page you want to scrape.
3. **Download Markdown**: View and download the Markdown content from the app interface.

---

## 🙏 Acknowledgments
This project was inspired by **DataInsightEdge** and built using **Crawl4AI**. Special thanks to:
- [Crawl4AI Repository](https://github.com/unclecode/crawl4ai) for the framework.
- [APC Mastery Path](https://www.youtube.com/@APCMasteryPath) YouTube channel for supporting project development.

For more, visit [APC Mastery Path](https://www.apcmasterypath.co.uk) or contact [Mohamed Ashour](mailto:mohamed_ashour@apcmasterypath.co.uk).
