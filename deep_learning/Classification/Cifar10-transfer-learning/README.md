# ⚡ CIFAR-10 Transfer Learning

This project applies **transfer learning** techniques to the **CIFAR-10** image classification dataset using **pretrained convolutional neural networks** **Xeption**.

Rather than training from scratch, this approach repurposes powerful feature extractors to improve accuracy and efficiency.

---

## 📊 Dataset: CIFAR-10

- **Classes**: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck
- **Image Size**: 32x32 pixels (resized to 224x224 for pretrained models)
- **Samples**: 50,000 training images + 10,000 test images

---

## 🧠 Model Architecture

- **Base Model**: Pretrained CNN (Xeption)
  - ImageNet weights
  - Base layers frozen during initial training
- **Top Layers**:
  - Global Average Pooling
  - Dense → Dropout → Dense (Softmax)

📎 Implemented in: `cifar10-tl.ipynb`

📷 Architecture diagram: `model.png`

---

## 🔧 Training Setup

- **Loss**: Categorical Crossentropy
- **Optimizer**: Adam (custom learning rate)
- **Metrics**: Accuracy
- **Callbacks**:
  - TensorBoard for logging
  - EarlyStopping (optional)
  - ModelCheckpoint (optional)

---

## ✅ Results

- Phase	Accuracy (Approx)
- Freezed base	85–88%
- Fine-Tuned	90–92%
