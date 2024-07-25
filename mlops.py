# -*- coding: utf-8 -*-
"""MLOps.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1U80RgfLvFXt6S2i17UAGEe61e8VG3Fp5
"""

from transformers import pipeline

model = pipeline('sentiment-analysis')

import pickle

with open('sentiment_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved successfully.")

!pip install gradio

import gradio as gr
import pickle

with open('sentiment_model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict(text):
    result = model(text)
    return result[0]['label']

interface = gr.Interface(fn=predict, inputs='text', outputs='label')

if __name__ == "__main__":
    interface.launch()
