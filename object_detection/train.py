from json import load
from ultralytics import YOLO


# initate model
def training():
    """training function

    Returns:
        model: yolo fine tuned model
        result: summery of what happend
    """
    model = YOLO(model=model_size, task=task)

    result = model.train(
        data=data_yaml,
        epochs=epochs,
        imgsz=image_size,
        val=val_on_train,
        batch=batch_size,
        save=save,
    )
    return model, result


def validation(model):
    """validation function IF VAL_ON_TRAIN IS FALSE

    Args:
        model (yolo-model): finetuned model
    Returns:
        result: summery of what happend
    """
    result = model.val()
    return result


if __name__ == "__main__":

    # reading configs
    with open("config.json", "r") as configFile:
        config_dict = load(configFile)

    model_size = config_dict["model_size"]  # model names
    task = config_dict["task"]
    data_yaml = config_dict["data_yaml"]  # dataset yaml file
    epochs = config_dict["epochs"]  # epochs
    image_size = config_dict["image_size"]  # image shape for inputs
    val_on_train = config_dict["val_on_train"]  # validation on training
    batch_size = config_dict["batch_size"]  # batch size
    save = config_dict["save"]

    fine_tuned_model, result = training()  # train model on dataset

    if not val_on_train:
        result_val = validation(model=fine_tuned_model)
