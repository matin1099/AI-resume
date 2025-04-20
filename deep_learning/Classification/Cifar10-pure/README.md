# 📦 CIFAR-10 Pure CNN

This project implements a **convolutional neural network (CNN)** trained from scratch on the **CIFAR-10** dataset. No transfer learning is used—just raw layers, training, and optimization.

---

## 📊 Dataset

- **Name**: CIFAR-10
- **Classes**: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck
- **Size**: 60,000 32x32 color images (50K train / 10K test)

---

## 🧠 Model Architecture

- 3 Convolutional layers
- MaxPooling
- Dropout
- Fully connected (Dense) layers
- Softmax output for classification

📎 See `cifar10.ipynb` for model structure and training code.
📎 See `mdoel.png` for model architecture.

---


## ✅ Results
 In training phase these metrics was met:

- Accuracy	~81%
- Loss	~0.4–0.6
