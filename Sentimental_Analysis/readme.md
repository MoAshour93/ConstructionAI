# 📊 Sentiment Analysis with Machine Learning and Deep Learning Models 💡

This repository contains a comprehensive sentiment analysis project leveraging **8 different models** across machine learning, deep learning, and transformer-based methods. By applying techniques such as text preprocessing, model training, and evaluation, this project offers a deep dive into sentiment classification, evaluating accuracy and performance across various approaches.

---

## 📑 Table of Contents

1. [Project Overview](#project-overview)
2. [Models Used](#models-used)
3. [Installation & Setup](#installation--setup)
4. [Data Preparation](#data-preparation)
5. [Workflow](#workflow)
6. [Results & Insights](#results--insights)
7. [Acknowledgments](#acknowledgments)
8. [🔗 General Links & Resources](#-general-links--resources)

---

## Project Overview

The goal of this project is to classify sentiments in text as **positive, neutral, or negative** using various models. Sentiment analysis finds applications across multiple fields, such as customer feedback analysis, social media monitoring, and employee engagement. This project explores and compares different models' effectiveness, from rule-based methods to advanced deep learning techniques, providing insights into each model's performance and potential applications.

---

## Models Used

The project includes 8 diverse models, covering a range of sentiment analysis techniques:

1. **VADER Sentiment Analysis** 🗣️ - A rule-based tool for social media sentiment.
2. **TextBlob** 📜 - A simple yet effective NLP library for basic sentiment tasks.
3. **RoBERTa** 🤖 - A transformer-based model for robust language understanding.
4. **Logistic Regression** 🔄 - A classic machine learning classifier.
5. **Multinomial Naive Bayes** 🌐 - Effective for text classification using discrete features.
6. **Support Vector Machine (SVM)** 📈 - Ideal for high-dimensional text data.
7. **XGBoost** ⚙️ - A powerful ensemble learning method for structured data.
8. **Long Short-Term Memory (LSTM)** 🧠 - A deep learning model designed for sequence data.

Each model is evaluated for accuracy, making this repository a valuable resource for comparing sentiment analysis approaches.

---

## Installation & Setup

To set up this project, clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes essential libraries such as **NLTK**, **Transformers**, **Scikit-Learn**, and **TensorFlow**.

---

## Data Preparation

The project uses a labeled dataset, structured with:
- **Sentence** - Text data containing various sentiment expressions.
- **Sentiment** - The manually assigned label (positive, neutral, or negative).

Preprocessing steps include:
- **Text Cleaning**: Removing special characters and stopwords.
- **Tokenization and Padding**: For deep learning models like LSTM.
- **TF-IDF Vectorization**: Converting text data into numeric format for machine learning models.

---

## Workflow

The project is divided into the following stages:

1. **Data Preprocessing** - Cleaning, stemming, and transforming text for model compatibility.
2. **Model Training & Evaluation** - Training each model on the preprocessed data and assessing accuracy.
3. **Performance Analysis** - Comparing model accuracies and visualizing results.

---

## Results & Insights

Key findings from the model evaluations include:

- **LSTM** showed the highest accuracy (approx. 70%) among all models, indicating strong performance with sequential data.
- **RoBERTa** achieved near-top results (approx. 68%), excelling in natural language understanding.
- Traditional machine learning models like **Logistic Regression** and **XGBoost** performed consistently well, making them viable options for smaller datasets.
- Simpler models, such as **VADER** and **TextBlob**, offer faster but less accurate predictions, making them suitable for applications needing quick sentiment assessment.

Each model’s accuracy and performance metrics are documented in the project, enabling an informed choice for specific sentiment analysis tasks.

---

## Acknowledgments

This project was inspired by a code snippet shared by **Yussria Ahmed** on LinkedIn. The analysis code was further expanded with additional models and refined for a comprehensive comparison. Special thanks to the open-source community for libraries that made this project possible.

---

## 🔗 General Links & Resources

- **Our Website:** [www.apcmasterypath.co.uk](https://www.apcmasterypath.co.uk)
- **APC Mastery Path Blogposts:** [APC Blogposts](https://www.apcmasterypath.co.uk/blog-list)
- **LinkedIn Pages:** [Personal](https://www.linkedin.com/in/mohamed-ashour-0727/) | [APC Mastery Path](https://www.linkedin.com/company/apc-mastery-path)
