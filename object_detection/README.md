# Object Detection 📷 🧼

A project based on YOLO and brain tumor database, to detect tumor.


## 📁 Project Structure
object_detection\
├── result\
│ ├── F1_curve.png\
│ ├── val_batch1_pred.jpg\
│ ├── val_batch2_pred.jpg\
│ └── val_batch3_pred.jpg\
├── README.md\
├── config_generator.py\
├── predict.py\
├── requirment.txt\
└── train.py


## 🛠️ Requirements
- Python 3.10+
- Ultralytic.

## 🚀 Getting Started
1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Then start  with `python config_generator.py` to create a config file. If need to change params, do it by editing this `.py` file.
4. For training `python train.py`
5. For useing Prediction use `python predict.py SOURCE` which could be a image/video/webcam. For webcam use `0`.

## 📝 License
This repo Licensed under `GNU Affrero General Public License`.
For more information check License
