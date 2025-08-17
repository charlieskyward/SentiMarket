# app.py

import gradio as gr
import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification

# --- Configuration ---
MODEL_PATH = "./model/bert_sentimarket_binary_model"
# Use the optimal threshold we discovered for the best performance.
OPTIMAL_THRESHOLD = 0.7707

# --- 1. Load the Fine-Tuned Model and Tokenizer ---
# This is loaded once when the app starts.
print("Loading model and tokenizer...")
try:
    tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
    model = TFBertForSequenceClassification.from_pretrained(MODEL_PATH)
    print("✅ Model and tokenizer loaded successfully.")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    # Exit if the model can't be loaded, as the app is useless without it.
    exit()

# --- 2. Define the Prediction Function ---
def predict_sentiment(text):
    """
    Takes a text input, tokenizes it, and returns the sentiment prediction
    with confidence scores using the optimal threshold.
    """
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="tf", truncation=True, padding=True, max_length=128)
    
    # Get model predictions (logits)
    outputs = model(inputs)
    logits = outputs.logits
    
    # Convert logits to probabilities
    probabilities = tf.nn.softmax(logits, axis=1).numpy()[0]
    
    # Get the probability for the "Positive" class
    positive_score = probabilities[1]
    
    # Apply the optimal threshold to decide the label
    if positive_score >= OPTIMAL_THRESHOLD:
        prediction_label = "Positive"
    else:
        prediction_label = "Negative"
        
    # Format the output for Gradio's Label component
    # It expects a dictionary of labels and their confidence scores.
    confidences = {
        "Positive": float(positive_score),
        "Negative": float(probabilities[0])
    }
    
    print(f"Input: '{text}' -> Prediction: {prediction_label}, Score: {positive_score:.4f}")
    return confidences

# --- 3. Build the Gradio Interface ---
demo = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(
        placeholder="Enter a financial headline or news snippet...",
        label="Financial News Headline",
        lines=3
    ),
    outputs=gr.Label(num_top_classes=2, label="Sentiment Prediction"),
    title="📈 SentiMarket: Financial Sentiment Analysis",
    description=(
        "This demo showcases a BERT model fine-tuned to classify the sentiment of financial news headlines. "
        "It was trained on a custom-labeled dataset and optimized for high accuracy. "
        "Enter a headline to see the model's prediction."
    ),
    examples=[
        ["Company announces massive layoffs amid economic downturn."],
        ["New study reveals surprising benefits of morning walks for productivity."],
        ["The central bank has raised interest rates to combat soaring inflation."],
        ["Tech giant smashes earnings expectations, stock price surges."],
    ],
    allow_flagging="never" # Disable the flagging feature
)

# --- 4. Launch the App ---
if __name__ == "__main__":
    demo.launch()
