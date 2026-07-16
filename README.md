# 🤖 HelpDesk AI

An AI-powered HelpDesk Chatbot built using TensorFlow Seq2Seq LSTM and Flask.

## 📌 Project Overview

HelpDesk AI is a customer support chatbot that generates responses to user queries using an Encoder-Decoder (Seq2Seq) LSTM neural network.

The chatbot has been trained on over **26,000 customer support conversations** and can answer questions related to:

- Order Cancellation
- Refunds
- Shipping
- Password Reset
- Billing
- Account Management
- Delivery Status
- General Customer Support

---

## 🚀 Features

- AI-based Seq2Seq Chatbot
- TensorFlow/Keras Deep Learning Model
- Flask Web Application
- Modern Chat Interface
- Tokenizer-based Text Processing
- Encoder-Decoder LSTM Architecture
- Model saved for inference
- Easy deployment

---

## 🛠 Tech Stack

- Python
- TensorFlow
- Keras
- Flask
- NumPy
- Pandas
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```
helpdesk-ai/
│
├── app.py
├── chatbot.py
├── requirements.txt
├── README.md
│
├── saved_models/
│   ├── chatbot_model.keras
│   ├── tokenizer.pkl
│   └── history.pkl
│
├── notebooks/
│   ├── 01_data_loading.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_tokenizer.ipynb
│   ├── 04_padding.ipynb
│   ├── 05_seq2seq_model.ipynb
│   ├── 06_training.ipynb
│   └── 07_chatbot_inference.ipynb
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── data/
```

---

## 📊 Dataset

Customer Support Dataset

- 26,872 conversations
- Question-Answer pairs
- Multiple customer service intents

---

## 🧠 Model Architecture

Encoder
- Embedding Layer
- LSTM (128 units)

↓

Decoder

- Embedding Layer
- LSTM (128 units)
- Dense Softmax Layer

↓

Generated Response

---

## ⚙️ Installation

Clone repository

```bash
git clone https://github.com/sameer-verma-07/helpdesk-ai.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## 📷 Demo

Example queries:

- Hello
- Cancel my order
- Refund request
- Forgot password
- Track shipment

---

Live Demo 

https://helpdesk-ai-production-cfbe.up.railway.app

---

## 👨‍💻 Author

Sameer Verma

GitHub:
https://github.com/sameer-verma-07
