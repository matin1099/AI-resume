import json

# Storing model basic param in a json file
model_info = {
    "model_size": "yolo11s.pt",  # model names
    "task": "detection",
    "data_yaml": "brain-tumor.yaml",  # dataset yaml file
    "epochs": 100,  # epochs
    "image_size": 640,  # image shape for inputs
    "val_on_train": False,  # validation on training
    "batch_size": 16,  # batch size
    "save": True,  # save odel wigth for resuming
    "test_for_predict": None,  # type: ignore
    "best_model": "/runs/detect/train/weights/best.pt",  # best model after train
}

with open("config.json", "w") as configfile:
    json.dump(model_info, configfile)
