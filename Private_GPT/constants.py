# Import necessary libraries
import os  # For interacting with the operating system, such as accessing environment variables
from dotenv import load_dotenv  # To load environment variables from a .env file
from chromadb.config import Settings  # For configuring Chroma database settings

# Load environment variables from the .env file
load_dotenv()

# Define the folder path for storing the Chroma database
PERSIST_DIRECTORY = os.environ.get('PERSIST_DIRECTORY')
if PERSIST_DIRECTORY is None:
    # Raise an exception if the PERSIST_DIRECTORY environment variable is not set
    raise Exception('Please set the PERSIST_DIRECTORY environment variable')

# Define Chroma settings for database persistence and telemetry
CHROMA_SETTINGS = Settings(
    persist_directory=PERSIST_DIRECTORY,  # Directory to store the Chroma database files
    anonymized_telemetry=False  # Disables telemetry (data collection) for privacy
)