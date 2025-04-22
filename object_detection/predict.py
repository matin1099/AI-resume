import shutil
import sys
from json import load
from ultralytics import YOLO


def predict(data):
    """predict data image/video/webcam

    Args:
        data (_type_): binary image videos or webcam for webcam use int(0)
    """
    model = YOLO(model="runs/detect/train/weights/best.pt")
    res = model.predict(data, save=True, imgsz=320, stream=True, show=True)
    res[0].save()


if __name__ == "__main__":
    # reading configs
    data = sys.argv[1]
    if data == "0":
        data = int(data)

    with open("config.json", "r") as configFile:
        config_dict = load(configFile)
    bestmodel = config_dict["best_model"]  # best model

    predict(data)
