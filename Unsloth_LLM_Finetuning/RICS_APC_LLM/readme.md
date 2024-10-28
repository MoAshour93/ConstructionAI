# Finetuning Llama 3.1 8B Instruct Model for RICS APC Submissions

This repository contains the code and steps required to finetune the Llama 3.1 8B Instruct model on a custom dataset of anonymized RICS APC submissions. By leveraging the [Unsloth library](https://github.com/unsloth), we expedite the fine-tuning process, empowering RICS APC candidates with a specialized chatbot for drafting submissions and refining competence area answers.

## Table of Contents

- [Project Overview](#project-overview)
  - [Objective](#objective)
  - [Key Steps](#key-steps)
- [Setup and Installation](#setup-and-installation)
  - [1. Environment Setup](#1-environment-setup)
    - [Step 1.1: Windows Subsystem for Linux](#step-11-windows-subsystem-for-linux)
    - [Step 1.2: Anaconda](#step-12-anaconda)
    - [Step 1.3: Installing Unsloth](#step-13-installing-unsloth)
    - [Step 1.4: Installing PyTorch and Nvidia CUDA Toolkit](#step-14-installing-pytorch-and-nvidia-cuda-toolkit)
  - [2. Dataset Preparation](#2-dataset-preparation)
  - [3. Model Loading and Configuration](#3-model-loading-and-configuration)
  - [4. Model Training and Quantization](#4-model-training-and-quantization)
  - [5. Local Deployment with OpenWebUI](#5-local-deployment-with-openwebui)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [Support and Contributions](#support-and-contributions)
- [🔗 General Links & Resources](#-general-links--resources)

---

## Project Overview

### Objective
This project fine-tunes Llama 3.1 8B Instruct model, creating a tailored language model trained on previous APC submissions. The final model, deployed through OpenWebUI, serves as an intelligent assistant that provides guidance to RICS APC candidates.

### Key Steps
1. **Environment Setup:** Install all dependencies and set up the required libraries.
2. **Dataset Transformation:** Convert the dataset into ShareGPT and Huggingface formats.
3. **Model Loading and Configuration:** Load Llama 3.1 8B Instruct model and adjust fine-tuning parameters.
4. **Model Training and Quantization:** Train the model with supervised fine-tuning and LoRA, then save it with quantization for optimized storage.
5. **Deployment:** Deploy the fine-tuned model locally using OpenWebUI.

---

## Setup and Installation

### 1. Environment Setup

#### Step 1.1: Windows Subsystem for Linux
* Unsloth works only on a Linux-based system. You can download your preferred Linux distribution from the following link: https://www.linux.org/pages/download/. 
* Alternatively, you can head to the following link: https://learn.microsoft.com/en-us/windows/wsl/install to understand how to install Windows Subsystem for Linux on your machine. 
  For ease, you can install WSL on your machine by opening PowerShell and typing:
  
      wsl --install

#### Step 1.2: Anaconda
* The easiest installation of Unsloth relies on installing Conda, available within Anaconda. To do that, go to Anaconda's main website: https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh
* Once downloaded, navigate to where you saved the Anaconda distribution, open the terminal in this location, and type the following commands:
  
      chmod +x Anaconda3-[version]-Linux-x86_64.sh
      ./Anaconda3-[version]-Linux-x86_64.sh

  Replace `[version]` with the downloaded version, e.g., `Anaconda3-2024.02-1-Linux-x86_64.sh`

#### Step 1.3: Installing Unsloth
* Go to the Unsloth repository on GitHub: https://github.com/unslothai/unsloth?tab=readme-ov-file and follow these steps to set up your Python environment with required packages. Open a terminal in your project folder and type:
  
      conda create unsloth_env python=3.10 pytorch-cuda=12.1 pytorch cudatoolkit xformers -c pytorch -c nvidia -c xformers -y
      conda activate unsloth_env
      pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
      pip install --no-deps "trl<0.9.0" wandb huggingface_hub peft accelerate bitsandbytes datasets

* Alternatively, install Unsloth using pip:

      sudo apt install python3-venv
      python3 -m venv unsloth_env
      source unsloth_env/bin/activate
      pip install --upgrade pip
      pip install "unsloth[cu121-torch240] @ git+https://github.com/unslothai/unsloth.git"

#### Step 1.4: Installing PyTorch and Nvidia CUDA Toolkit
* Install the latest version of PyTorch with CUDA enabled:
  
      pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

* Install the Nvidia CUDA Toolkit v 12.1 by typing:

      wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
      sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
      wget https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda-repo-wsl-ubuntu-12-1-local_12.1.0-1_amd64.deb
      sudo dpkg -i cuda-repo-wsl-ubuntu-12-1-local_12.1.0-1_amd64.deb
      sudo cp /var/cuda-repo-wsl-ubuntu-12-1-local/cuda-*-keyring.gpg /usr/share/keyrings/
      sudo apt-get update
      sudo apt-get -y install cuda

### 2. Dataset Preparation

Convert the anonymized dataset into [ShareGPT format](https://huggingface.co/docs/datasets/sharegpt) and then to Huggingface format. Detailed steps include:

- Loading the dataset.
- Converting it to ShareGPT JSON format.
- Transforming it for Huggingface compatibility.

### 3. Model Loading and Configuration

Load the Llama 3.1 8B Instruct model using Unsloth and configure supervised fine-tuning parameters, including **LoRA** for efficiency, learning rates, and batch sizes.

For details, see [`RICS_APC_LLM_Finetuning_llama3_1_instruct_8b_conversational.ipynb`](./notebooks/RICS_APC_LLM_Finetuning_llama3_1_instruct_8b_conversational.ipynb).

### 4. Model Training and Quantization

1. Train the model by running the provided scripts.
2. Quantize the model post-training for optimized storage and faster inference.

The trained model is saved in `models/`.

### 5. Local Deployment with OpenWebUI

To deploy the model locally:

1. Install **OpenWebUI** dependencies.
2. Load the quantized model into OpenWebUI for a streamlined chatbot experience.

---

## Usage

After deployment, candidates can interact with the chatbot locally to generate APC draft responses and receive tailored feedback.

---

## Future Enhancements

Potential improvements include:
- Experimenting with larger datasets and data augmentation.
- Cloud deployment for remote access.
- Integrations with tools for enhanced feedback.

---

## Support and Contributions

Contributions are welcome! For major changes, please open an issue first. Reach out on our [LinkedIn Page](https://www.linkedin.com/company/apc-mastery-path) or [website](www.apcmasterypath.co.uk).

---

## 🔗 General Links & Resources

- **Our Website:** [www.apcmasterypath.co.uk](https://www.apcmasterypath.co.uk)
- **APC Mastery Path Blogposts:** [APC Blogposts](https://www.apcmasterypath.co.uk/blog-list)
- **LinkedIn Pages:** [Personal](https://www.linkedin.com/in/mohamed-ashour-0727/) | [APC Mastery Path](https://www.linkedin.com/company/apc-mastery-path)
