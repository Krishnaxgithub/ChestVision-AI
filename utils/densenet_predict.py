from xray_model import model
from utils.preprocess import preprocess_image


def predict_densenet(image_path):

    img = preprocess_image(
        image_path
    )

    preds = model(
        img
    )

    result = {

        pathology: float(score)

        for pathology, score in zip(
            model.pathologies,
            preds[0].detach().numpy()
        )

    }

    return result