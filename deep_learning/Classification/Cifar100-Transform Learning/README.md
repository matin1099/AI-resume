# 🚀 CIFAR-100 Transfer Learning

This project demonstrates **transfer learning** on the **CIFAR-100** dataset using pretrained models **Xeption**. Instead of training from scratch, we leverage high-performance feature extractors to speed up training and boost accuracy.

---

## 📦 Dataset

- **Name**: CIFAR-100
- **Classes**: 100 fine-grained categories
- **Image Dimensions**: 32x32 RGB (resized to 224x224)
- **Total Samples**: 60,000 (50,000 training + 10,000 testing)

---

## 🧠 Model Architecture

- **Base Model**: Pretrained on ImageNet **Xeption**
  - Optionally frozen or partially fine-tuned
- **Head Layers**:
  - Global Average Pooling
  - Dropout
  - Dense output with Softmax (100 classes)

📝 Full implementation: `cifar100-tl.ipynb`
📎 See `mdoel.png` for model architecture.


---

## 🛠️ Training Setup

- **Loss Function**: Categorical Crossentropy
- **Optimizer**: Adam
- **Metrics**: Accuracy
- **Callbacks**:
  - TensorBoard logging
  - EarlyStopping
  - ModelCheckpoint (optional)


---

## ✅ Results

- Training Stage	Accuracy (Approx.)
- Frozen base	60–65%
- Fine-tuned	70–75%
