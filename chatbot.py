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


# =====================================================
# Paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "saved_models"


# =====================================================
# Load Tokenizer
# =====================================================

print("Loading tokenizer...")

with open(MODEL_DIR / "tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

print("Tokenizer Loaded Successfully!")


# =====================================================
# Load Model
# =====================================================

print("Loading trained model...")

model = load_model(MODEL_DIR / "chatbot_model.keras")

print("Model Loaded Successfully!")


# =====================================================
# Build Encoder Model
# =====================================================

encoder_inputs = model.input[0]

encoder_embedding = model.get_layer("encoder_embedding")
encoder_lstm = model.get_layer("encoder_lstm")

_, state_h, state_c = encoder_lstm(
    encoder_embedding(encoder_inputs)
)

encoder_model = Model(
    encoder_inputs,
    [state_h, state_c]
)


# =====================================================
# Build Decoder Model
# =====================================================

decoder_inputs = model.input[1]

decoder_embedding = model.get_layer("decoder_embedding")
decoder_lstm = model.get_layer("decoder_lstm")
decoder_dense = model.get_layer("decoder_output")

decoder_state_input_h = Input(shape=(128,))
decoder_state_input_c = Input(shape=(128,))

decoder_states_inputs = [
    decoder_state_input_h,
    decoder_state_input_c
]

decoder_embedding_output = decoder_embedding(decoder_inputs)

decoder_outputs, state_h, state_c = decoder_lstm(
    decoder_embedding_output,
    initial_state=decoder_states_inputs
)

decoder_states = [
    state_h,
    state_c
]

decoder_outputs = decoder_dense(decoder_outputs)

decoder_model = Model(
    [decoder_inputs] + decoder_states_inputs,
    [decoder_outputs] + decoder_states
)


# =====================================================
# Reverse Vocabulary
# =====================================================

reverse_word_index = {
    index: word
    for word, index in tokenizer.word_index.items()
}


# =====================================================
# Constants
# =====================================================

MAX_QUESTION_LENGTH = 64
MAX_RESPONSE_LENGTH = 20


# =====================================================
# Encode User Input
# =====================================================

def encode_input(sentence):

    sentence = sentence.lower().strip()

    sequence = tokenizer.texts_to_sequences([sentence])

    sequence = pad_sequences(
        sequence,
        maxlen=MAX_QUESTION_LENGTH,
        padding="post",
        truncating="post"
    )

    states = encoder_model.predict(
        sequence,
        verbose=0
    )

    return states


# =====================================================
# Generate Response
# =====================================================

def generate_response(sentence):

    try:

        states = encode_input(sentence)

        target_seq = np.zeros((1, 1), dtype="float32")
        target_seq[0, 0] = tokenizer.word_index["sos"]

        decoded_words = []

        while True:

            output_tokens, h, c = decoder_model.predict(
                [target_seq] + states,
                verbose=0
            )

            sampled_token_index = np.argmax(
                output_tokens[0, -1, :]
            )

            sampled_word = reverse_word_index.get(
                sampled_token_index,
                ""
            )

            # Ignore SOS token
            if sampled_word == "sos":

                target_seq[0, 0] = sampled_token_index
                states = [h, c]

                continue

            # Stop generation
            if sampled_word == "eos":
                break

            # Stop on unknown token
            if sampled_word == "":
                break

            decoded_words.append(sampled_word)

            if len(decoded_words) >= MAX_RESPONSE_LENGTH:
                break

            target_seq[0, 0] = sampled_token_index
            states = [h, c]

        response = " ".join(decoded_words).strip()

        # Fallback for empty/poor responses
        if len(response.split()) < 3:
            return (
                "I'm sorry, I couldn't understand your request. "
                "Could you please rephrase it?"
            )

        return response.capitalize()

    except Exception as e:

        print("Inference Error:", e)

        return (
            "Sorry, something went wrong while generating the response."
        )