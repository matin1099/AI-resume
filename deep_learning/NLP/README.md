# 🧠 Natural Language Processing (NLP) Projects

This folder contains NLP experiments focused on **text generation**, **dataset parsing**, and **modeling sequential language patterns**. It includes lyric modeling using Persian poetry and raw XHTML data parsing.

---
## 📜 Project: Lyric-Based Text Generation

### 📄 `model.ipynb`

- Builds a **word-level LSTM** text generator.
- Trains on `manocheri_lyric.txt`, a cleaned corpus of classic Persian poetry.
- Uses sequential tokenization and one-hot encoding.

### 🧪 Features

- Preprocessing and tokenization
- Sequence modeling using Keras
- Sampling strategies for generating output
- Model training with callbacks

### 📷 Visuals

📎 See `mdoel.png` for model architecture.

---

## 🛠️ Script: `lyric.py`

Contains utility functions to:
- Extract , load and clean text from `xhtml` files.
- Outputs dataset as `.txt`

---

## 📂 Dataset Raw XHTML

The `dataset raw/` folder contains **XHTML documents** from **Ganjor library**  used for:

- Building a richer Persian or structured-language corpus
- Extracting semantic or structural text

--

## ✅ Results
 In training phase these metrics was met:

- Accuracy	~88%
- Loss	~0.3–0.4
