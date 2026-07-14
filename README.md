# 🤖 HelpDesk AI

A Deep Learning based Customer Support Chatbot built using **TensorFlow, Keras, Seq2Seq LSTM, NLP, Flask, HTML, CSS, and JavaScript**.

The chatbot is trained on a customer support conversation dataset and provides automated responses to common customer queries such as order cancellation, refunds, shipment tracking, delivery updates, password assistance, and more.

---

# 📌 Project Overview

HelpDesk AI is an end-to-end AI chatbot developed as an internship project.

The project demonstrates the complete Natural Language Processing pipeline:

- Data Collection
- Text Preprocessing
- Tokenization
- Sequence Padding
- Seq2Seq Encoder-Decoder Architecture
- LSTM Networks
- Model Training
- Model Inference
- Flask API
- Interactive Web Interface

---

# 🚀 Features

- Customer Support Chatbot
- Deep Learning (Seq2Seq LSTM)
- TensorFlow/Keras Model
- Flask Backend
- Responsive Web Interface
- Real-time Chat
- NLP Text Processing
- Encoder-Decoder Architecture
- Tokenizer Saved using Pickle
- Model Saved in Keras Format

---

# 🛠 Tech Stack

### Programming Language

- Python

### Deep Learning

- TensorFlow
- Keras

### NLP

- Tokenization
- Sequence Padding
- Text Cleaning

### Backend

- Flask

### Frontend

- HTML
- CSS
- JavaScript

### Others

- NumPy
- Pandas
- Pickle

---

# 📂 Project Structure

```
helpdesk-ai/
│
├── app.py
├── chatbot.py
├── requirements.txt
├── README.md
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
├── data/
│   ├── raw/
│   └── processed/
│
├── saved_models/
│   ├── chatbot_model.keras
│   ├── tokenizer.pkl
│   └── history.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── screenshots/
```

---

# 🧠 Model Architecture

The chatbot uses a Sequence-to-Sequence (Seq2Seq) Encoder-Decoder architecture.

Encoder

- Embedding Layer
- LSTM Layer

↓

Context Vector

↓

Decoder

- Embedding Layer
- LSTM Layer
- Dense Output Layer

---

# 📊 Dataset

Customer Support Training Dataset

- Approximately 27,000 question-answer pairs
- Customer support conversations
- Order Management
- Refunds
- Password Assistance
- Delivery Tracking
- Billing Queries

---

# ⚙️ Model Training

Model Type

- Seq2Seq Encoder-Decoder

Embedding Size

- 64

LSTM Units

- 128

Epochs

- 20

Loss Function

- Sparse Categorical Crossentropy

Optimizer

- Adam

---

# 💻 Running the Project

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/helpdesk-ai.git
```

## Install Requirements

```bash
pip install -r requirements.txt
```

## Run Application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 📸 Screenshots

## Home Page

(Add Screenshot)

---

## Chat Interface

(Add Screenshot)

---

## Model Training

(Add Screenshot)

---

## Model Summary

(Add Screenshot)

---

# 📈 Future Improvements

- Transformer-based architecture
- Attention Mechanism
- Beam Search Decoding
- Better Dataset
- Speech Recognition
- Voice Assistant
- Multi-language Support
- Integration with LLMs

---

# 👨‍💻 Author

**Sameer Verma**

AI & Full Stack Developer

GitHub:
https://github.com/sameer-verma-07

---

# ⭐ Internship Project

This project was developed as part of an AI internship to demonstrate end-to-end development of a Deep Learning based Customer Support Chatbot using TensorFlow and Flask.
