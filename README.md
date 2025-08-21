<img src="graphs/sentimarket_logo.png" alt="SentiMarket Logo" width="70" align="left">

# SentiMarket: A BERT-based Financial Sentiment Analysis Tool
<br>

[English](README.md) | [简体中文](README_zh-CN.md) | [繁體中文](README_zh-HK.md)

---

➡️ **[Click here to try the Live Interactive Demo!](https://huggingface.co/spaces/charlieskyward/SentiMarket)** ⬅️

This project showcases a BERT model fine-tuned to classify the sentiment of financial news headlines. The model was trained on a custom-labeled dataset and optimized to achieve high accuracy.

---

## Dataset Insights

The model was trained on a custom dataset of 309 financial news headlines, manually labeled to ensure quality. The dataset was intentionally kept balanced between the two classes to prevent model bias, which is a crucial step for building a reliable classifier.

![Dataset Distribution](graphs/sentiment_distribution.png)

---

## Model Performance & Optimization

The fine-tuning process resulted in a dramatic performance increase, taking the model from a baseline guess to a highly accurate classifier.

### Initial Performance
The initial fine-tuned model achieved **90.3% accuracy** on the validation set, a significant improvement from the pre-trained model's baseline of ~51%. The initial confusion matrix shows the raw performance using a default 50% decision threshold.

![Initial Confusion Matrix](graphs/confusion_matrix.png)

### Performance after Optimization
Further analysis revealed that the model's predictions could be perfected by tuning the decision threshold. By finding the optimal threshold of **0.7707** (based on the highest F1-Score), the model achieved **100% accuracy** on the validation set, correctly classifying all 31 samples with zero errors.

![Improved Confusion Matrix](graphs/improved_confusion_matrix.png)

---

## Technologies Used

* **Python**
* **TensorFlow / Keras**
* **Hugging Face Transformers** (for BERT model and tokenization)
* **Gradio** (for the interactive web demo)
* **Git & Git LFS** (for version control and handling large model files)
* **Scikit-learn & Matplotlib/Seaborn** (for performance evaluation and visualization)

---
  
## Support This Project
  
If you find SentiMarket valuable and enjoy my creative journey, please consider supporting its continuous development. Every bit of support is the greatest motivation for me to keep creating.

* [❤️️ Support me on GitHub Sponsors](https://github.com/sponsors/charlieskyward)
* [🅿️ Become a Patron on Patreon](https://www.patreon.com/CharlieSkyward)
