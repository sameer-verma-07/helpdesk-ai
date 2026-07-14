"""
HelpDesk AI
Chatbot Inference Module
"""

import pickle
import numpy as np

from pathlib import Path

from tensorflow.keras.models import load_model, Model
from tensorflow.keras.layers import Input
from tensorflow.keras.preprocessing.sequence import pad_sequences


# ----------------------------------------------------
# Paths
# ----------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "saved_models"


# ----------------------------------------------------
# Constants
# ----------------------------------------------------

MAX_LENGTH = 20


print("Loading tokenizer...")

with open(MODEL_DIR / "tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)


print("Loading trained model...")

model = load_model(MODEL_DIR / "chatbot_model.keras")


print("Model Loaded Successfully!")