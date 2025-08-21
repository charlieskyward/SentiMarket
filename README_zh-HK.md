<img src="graphs/sentimarket_logo.png" alt="SentiMarket Logo" width="70" align="left">

# SentiMarket: 基於BERT的金融情緒分析工具
<br>

[English](README.md) | [简体中文](README_zh-CN.md) | [繁體中文](README_zh-HK.md)

---

➡️ **[點擊此處體驗實時互動式演示！](https://huggingface.co/spaces/charlieskyward/SentiMarket)** ⬅️

本專案展示了一個為金融新聞情緒分析而微調的BERT模型。該模型在自定義標記的資料集上進行了訓練和優化，以實現高準確度。

---

## 專案背景

金融市場深受新聞和公眾情緒的影響。本專案旨在將金融新聞標題的情緒分析過程自動化。其核心是一個`bert-base-uncased`模型，經過微調以理解金融語言的特定細微差別，可將文本分為**積極**或**消極**兩類。

---

## 資料集洞察

該模型在一個包含309條金融新聞標題的自定義資料集上進行訓練，所有資料均經過手動標記以確保質量。為了防止模型偏見，我們特意保持了兩類標籤之間的平衡，這是構建可靠分類器的關鍵一步。

![資料集分佈圖](graphs/sentiment_distribution.png)

---

## 模型性能與優化

微調過程極大地提升了模型性能，使其從基線的隨機猜測轉變為一個高度準確的分類器。

### 初始性能
初次微調後，模型在驗證集上達到了**90.3%的準確率**，相較於預訓練模型約51%的基線性能有了顯著提升。下圖的混淆矩陣展示了使用預設50%決策閾值時的原始性能。

![初始混淆矩陣](graphs/confusion_matrix.png)

### 優化後性能
進一步分析表明，通過調整決策閾值可以使模型的預測達到完美。基於最高的F1分數，我們找到了**0.7707**的最佳閾值，使模型在驗證集上實現了**100%的準確率**，完美地分類了所有31個樣本，無一錯誤。

![優化後的混淆矩陣](graphs/improved_confusion_matrix.png)

---

## 技術棧

* **Python**
* **TensorFlow / Keras**
* **Hugging Face Transformers** (用於BERT模型和分詞)
* **Gradio** (用於互動式Web演示)
* **Git & Git LFS** (用於版本控制和處理大型模型文件)
* **Scikit-learn & Matplotlib/Seaborn** (用於性能評估和視覺化)

---

## 支持本專案

如果您覺得SentiMarket有價值，並願意支持我的創作之旅，歡迎透過以下方式支持我的持續開發。您的每一份認可，都是我繼續前行的最大動力。

* [❤️️ 透過 GitHub Sponsors 支持](https://github.com/sponsors/charlieskyward)
* [🅿️ 成為我的 Patreon 支持者](https://www.patreon.com/CharlieSkyward)
