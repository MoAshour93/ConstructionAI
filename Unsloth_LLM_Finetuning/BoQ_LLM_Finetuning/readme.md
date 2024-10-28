# 🔧 Finetuning Llama 3.1 8B Instruct Model for Bills of Quantities Codification 📚

This repository contains the code and steps required to finetune the **Llama 3.1 8B Instruct model** on a custom dataset of anonymized Bill of Quantities data. By leveraging the powerful [Unsloth library 🚀](https://github.com/unsloth), we expedite the fine-tuning process and undertaking the codification of bills of quantities in accordance with the New Rules of Measurement 1 which is produced by the Royal Institution of Chartered Surveyors.

## 📑 Table of Contents

- [📋 Project Overview](#project-overview)
  - [🎯 Objective](#objective)
  - [🗝️ Key Steps](#key-steps)
- [⚙️ Setup and Installation](#setup-and-installation)
  - [1️⃣ Environment Setup](#1-environment-setup)
    - [🔧 Step 1.1: Windows Subsystem for Linux](#step-11-windows-subsystem-for-linux)
    - [🐍 Step 1.2: Anaconda](#step-12-anaconda)
    - [📦 Step 1.3: Installing Unsloth](#step-13-installing-unsloth)
    - [💻 Step 1.4: Installing PyTorch and Nvidia CUDA Toolkit](#step-14-installing-pytorch-and-nvidia-cuda-toolkit)
  - [📂 2. Dataset Preparation](#2-dataset-preparation)
  - [🧩 3. Model Loading and Configuration](#3-model-loading-and-configuration)
  - [🔍 4. Model Training and Quantization](#4-model-training-and-quantization)
  - [🌐 5. Local Deployment with OpenWebUI](#5-local-deployment-with-openwebui)
- [🚀 Usage](#usage)
- [🔮 Future Enhancements](#future-enhancements)
- [💬 Support and Contributions](#support-and-contributions)
- [🔗 General Links & Resources](#-general-links--resources)

---

## 📋 Project Overview

### 🎯 Objective
This project fine-tunes the **Llama 3.1 8B Instruct model**, creating a tailored language model trained on previous well codified bills of quantities in accordance with the New Rules of Measurement 1 which is produced by the Royal Institution of Chartered Surveyors. The final model, deployed through **OpenWebUI**, serves as an intelligent assistant that provides guidance to quantity surveyors, estimators and cost managers when codifying bills of quantities.

### 🗝️ Key Steps
1. **Environment Setup** 🖥️: Install all dependencies and set up the required libraries.
2. **Dataset Transformation** 📊: Convert the dataset into **ShareGPT** and **Huggingface** formats.
3. **Model Loading and Configuration** ⚙️: Load Llama 3.1 8B Instruct model and adjust fine-tuning parameters.
4. **Model Training and Quantization** 🎓: Train the model with supervised fine-tuning and LoRA, then save it with quantization for optimized storage.
5. **Deployment** 🌐: Deploy the fine-tuned model locally using OpenWebUI.

---

## ⚙️ Setup and Installation

### 1️⃣ Environment Setup

#### 🔧 Step 1.1: Windows Subsystem for Linux
- Unsloth works on a Linux-based system. For your preferred Linux distribution, [download here](https://www.linux.org/pages/download/).
- Alternatively, follow [Microsoft’s guide to install WSL](https://learn.microsoft.com/en-us/windows/wsl/install).  
  Install WSL via PowerShell:

      wsl --install

#### 🐍 Step 1.2: Anaconda
- Install **Conda** via [Anaconda’s main site](https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh).
- Navigate to where you saved the Anaconda distribution, then execute:

      chmod +x Anaconda3-[version]-Linux-x86_64.sh
      ./Anaconda3-[version]-Linux-x86_64.sh

  Replace `[version]` as needed.

#### 📦 Step 1.3: Installing Unsloth
- Visit the [Unsloth repository](https://github.com/unslothai/unsloth?tab=readme-ov-file) and follow the steps to set up your Python environment. Open a terminal in your project folder and type:

      conda create unsloth_env python=3.10 pytorch-cuda=12.1 pytorch cudatoolkit xformers -c pytorch -c nvidia -c xformers -y
      conda activate unsloth_env
      pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
      pip install --no-deps "trl<0.9.0" wandb huggingface_hub peft accelerate bitsandbytes datasets

- Alternatively, use **pip**:

      sudo apt install python3-venv
      python3 -m venv unsloth_env
      source unsloth_env/bin/activate
      pip install --upgrade pip
      pip install "unsloth[cu121-torch240] @ git+https://github.com/unslothai/unsloth.git"

#### 💻 Step 1.4: Installing PyTorch and Nvidia CUDA Toolkit
- Install **PyTorch** with CUDA:

      pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

- Install **Nvidia CUDA Toolkit v12.1**:

      wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
      sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
      wget https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda-repo-wsl-ubuntu-12-1-local_12.1.0-1_amd64.deb
      sudo dpkg -i cuda-repo-wsl-ubuntu-12-1-local_12.1.0-1_amd64.deb
      sudo cp /var/cuda-repo-wsl-ubuntu-12-1-local/cuda-*-keyring.gpg /usr/share/keyrings/
      sudo apt-get update
      sudo apt-get -y install cuda

### 📂 2. Dataset Preparation

Convert the anonymized dataset into [ShareGPT format](https://huggingface.co/docs/datasets/sharegpt) and then to Huggingface format. Detailed steps include:

- Loading the dataset.
- Converting it to ShareGPT JSON format.
- Transforming it for Huggingface compatibility.

### 🧩 3. Model Loading and Configuration

Load the **Llama 3.1 8B Instruct model** using Unsloth and configure supervised fine-tuning parameters, including **LoRA** for efficiency, learning rates, and batch sizes.

For details, see the notebook [`RICS_APC_LLM_Finetuning_llama3_1_instruct_8b_conversational.ipynb`](./notebooks/RICS_APC_LLM_Finetuning_llama3_1_instruct_8b_conversational.ipynb).

### 🔍 4. Model Training and Quantization

1. Train the model by running the provided scripts.
2. Quantize the model post-training for optimized storage and faster inference.

The trained model is saved in `models/`.

### 🌐 5. Local Deployment with OpenWebUI

To deploy the model locally:

1. Install **OpenWebUI** dependencies.
2. Load the quantized model into OpenWebUI for a streamlined chatbot experience.

---

## 🚀 Usage

After deployment, cost managers, estimators and quantity surveyors can deploy this finetuned large language model to codify large-scale uncodified bills of quantities.

---

## 🔮 Future Enhancements

Potential improvements include:
- Experimenting with larger datasets and data augmentation.
- Cloud deployment for remote access.
- Integrations with tools for enhanced feedback.

---

## 💬 Support and Contributions

Contributions are welcome! For major changes, please open an issue first. Reach out on our [LinkedIn Page](https://www.linkedin.com/company/apc-mastery-path) or [website](https://www.apcmasterypath.co.uk).

---

## 🔗 General Links & Resources

- **Our Website**: [www.apcmasterypath.co.uk](https://www.apcmasterypath.co.uk)
- **APC Mastery Path Blogposts**: [APC Blogposts](https://www.apcmasterypath.co.uk/blog-list)
- **LinkedIn Pages**: [Personal](https://www.linkedin.com/in/mohamed-ashour-0727/) | [APC Mastery Path](https://www.linkedin.com/company/apc-mastery-path)
