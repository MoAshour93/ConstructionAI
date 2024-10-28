##General Information:
#---------------
#This code is developed by Mohamed Ashour who is the proud founder of APC Mastery Path.
#In case you have any queries, do not hesitate to reach out via email on mohamed_ashour@apcmasterypath.co.uk
#For further insights, you could pay our website a visit on www.apcmasterypath.co.uk
#Link to our youtube channel is: www.youtube.com/@APCMasteryPath

#Code Introduction:
#------------------
#The code is inspired by part of the code developed by the youtube channel DataInsightEdge: https://www.youtube.com/watch?v=VtranIoS2uk&ab_channel=DataEdge
#The purpose of this program is to scrap the web to get relevant information. The scraped data is captured in HTML format and then converted to a Markdown format.
#The converted HTML text could then be downloaded if required by the user as a Markdown file (extracted_text.md)
#The web scrapping Crawl AI library is used for the purpose of this mini project.
#Crawl4AI github repository: https://github.com/unclecode/crawl4ai
#Streamlit is used to provide an enhanced user interface and user experience.

##Building the application:
##-------------------------

#Step 0: Creating a virtual environment and Installing requirements 
    #Step 0.1: Open a terminal inside VSCode and type the following codes to create a virtual environment
        ##pip install virtualenv
        ##pthon3 -m venv crawl4ai
        ##source crawl4ai/bin/activate
    #Step 0.2: Install the required libraries
        ##pip install streamlit
        ##pip install crawl4ai
        ##pip install crawl4ai[sync]
        ## pip install markdownify
        ##pip install beautiful-soup
        ##pip install requests

# Step 0.3:Import necessary libraries
import streamlit as st # This library is required for building the user interface
import requests # This package is required to send requests to websites to obtain data from them
from bs4 import BeautifulSoup #This library is required to scrap text and deal with html format
import markdownify #This library is required to convert html format into markdown format taking into account the headings hierarchy in the html code
import base64 # This library is required to deal with text
import re  # Import regular expressions library for cleaning markdown

#Creating Helper functions (Steps 1 to 6):
    # Step 1: Custom Styling Function to make the app more visually appealing
    # Step 2: Function to adjust resource URLs
    # Step 3: Function to convert HTML to Markdown
    # Step 4: Function to clean up the markdown content
    # Step 5: Function to download the markdown file
    # Step 6: Main function to build the Streamlit app

# Step 1: Custom Styling Function to make the app more visually appealing
def apply_custom_styles():
    """
    This function applies custom CSS styles to the Streamlit app to enhance its appearance.
    """
    st.markdown(
        """
        <style>
        body {
            font-family: 'Helvetica Neue', sans-serif;
            background-color: #f9f9f9;
            color: #333;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
        }
        .stTextInput input {
            border-radius: 5px;
            padding: 10px;
            border: 1px solid #ddd;
            width: 100%;
            box-sizing: border-box;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Step 2: Function to adjust resource URLs
def adjust_resource_urls(soup, base_url):
    """
    Adjusts relative URLs to absolute URLs for images.
    """
    # Iterate over all image tags
    for img_tag in soup.find_all('img'):
        img_url = img_tag.get('src')
        # If the image URL is relative, convert it to an absolute URL
        if img_url and not img_url.startswith(('http://', 'https://', '//')):
            absolute_url = requests.compat.urljoin(base_url, img_url)
            img_tag['src'] = absolute_url
        # If the image URL starts with '//' (protocol-relative), add 'https:'
        elif img_url and img_url.startswith('//'):
            img_tag['src'] = 'https:' + img_url
    return soup

# Step 3: Function to convert HTML to Markdown
def html_to_markdown(html_content):
    """
    Converts HTML content to Markdown format, preserving formatting like headers, bold, italics, and images.
    """
    # Use markdownify to convert HTML to Markdown
    # Include heading tags in the conversion
    md_content = markdownify.markdownify(
        html_content,
        heading_style="ATX",  # Use '#' symbols for headings
        convert=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'b', 'i', 'img', 'strong', 'em', 'a']
    )
    return md_content

# Step 4: Function to clean up the markdown content
def clean_markdown(md_content):
    """
    Cleans up the markdown content by removing excessive empty lines and unnecessary whitespace.
    """
    # Remove multiple consecutive empty lines
    md_content = re.sub(r'\n\s*\n', '\n\n', md_content)
    # Strip leading and trailing whitespace from each line
    md_content = '\n'.join(line.strip() for line in md_content.splitlines())
    # Remove any leading/trailing whitespace from the entire content
    return md_content.strip()

# Step 5: Function to download the markdown file
def download_markdown(content, filename="extracted_content.md"):
    """
    Creates a download link for a markdown file containing the scraped content.
    """
    content_str = str(content)
    # Encode the content as Base64
    b64 = base64.b64encode(content_str.encode()).decode()

    # Create a download link with a button
    href = f"""
    <a href="data:file/markdown;base64,{b64}" download="{filename}">
        <button style="
            display: inline-block;
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
            border: none;">
            Download Markdown File
        </button>
    </a>
    """
    return href

# Step 6: Main function to build the Streamlit app
def main():
    # Apply custom styles to the app
    apply_custom_styles()

    # App title
    st.title("Web Scraper App - Extract your scrapped text to Markdown")

    # Step 6.1: URL input
    url = st.text_input("Enter the URL that you want to scrape:")

    # Step 6.2: Scrape button
    if st.button("Run Web Scraper"):
        if url:
            try:
                # Step 6.3: Send a GET request to the URL
                response = requests.get(url)
                response.raise_for_status()  # Raise an error for bad status codes

                # Step 6.4: Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(response.content, 'html.parser')

                # Step 6.5: Adjust resource URLs for images
                soup = adjust_resource_urls(soup, url)

                # Step 6.6: Extract the main content
                # Try to extract content inside <article> tags if they exist
                article = soup.find('article')
                if article:
                    html_content = str(article)
                else:
                    # Fallback to body content if <article> is not present
                    html_content = str(soup.body)

                # Step 6.7: Convert HTML to Markdown
                md_content = html_to_markdown(html_content)

                # Step 6.8: Clean up the Markdown content
                md_content = clean_markdown(md_content)

                # Step 6.9: Display the markdown content in the app
                st.markdown(md_content)

                # Step 6.10: Provide download link for scraped markdown content
                st.markdown(download_markdown(md_content), unsafe_allow_html=True)

            except requests.exceptions.RequestException as e:
                # Step 6.11: Error handling for request errors
                st.error(f"Error fetching the URL: {e}")
            except Exception as e:
                # Step 6.12: General error handling
                st.error(f"An unexpected error occurred: {e}")
        else:
            # Step 6.13: Warning for invalid URL input
            st.warning("Please enter a valid URL")

# Step 7: Run the app
if __name__ == "__main__":
    main()

#Step 8: Create an executable file to be able to run the code by right click instead of running it from terminal

#Open the terminal and follow these steps:
    
    # 8.1 Navigate to Your Project Directory
        # Open a terminal and navigate to your project directory:
            #Code:cd ~/Path_to_Your_Project_Folder
    
    #Step 8.2: Create the Shell Script File:
        # Use a text editor to create a new file named run_webscraper.sh:
            #nano run_webscraper.sh
    
    #Step 8.3:  Add the Following Content to the Script: ( Make sure to remove the hastag from line 3 and line 5 below. The hashtags are added to signify that it is a comment)
        # #!/bin/bash
        # # Activate the virtual environment
        # source ~/Path_to_Your_Project_Folder/crawl4ai/bin/activate

        # # Run the Streamlit app
        # streamlit run ~/Documents/Projects/WebScrapping_CrawlAI/webscrapping_CrawlAI_enhanced.py

    #Step 8.4: Saving the lines above to the run_webscrapper.sh file:
        #Once you add the lines above, press Ctrl+O then the Enter button then Ctrl+X to save the lines above in the created shell file.
    
    #Step 8.5: Make the Script Executable
        # Set the execute permission on the script by running the code below in terminal after the previous steps (make sure to remove the hashtag from the code below when you paste it in terminal)
            #chmod +x run_webscraper.sh
    
    #Step 8.6: Run the shell file
        #Once you have done the previous 5 steps, you can then right click on the created shell file and then press "Run as a program".