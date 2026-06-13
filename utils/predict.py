from xray_model import model
from utils.preprocess import preprocess_image
import torch


def predict_xray(path):

    img = preprocess_image(path)

    with torch.no_grad():
        preds = model(img)

    result = dict(
        zip(
            model.pathologies,
            preds[0].numpy()
        )
    )

    # Remove empty labels
    while "" in result:
        del result[""]

    return result
