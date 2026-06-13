
import torch
import open_clip
from PIL import Image

# ==========================================================
# Device
# ==========================================================

device = "cpu"

# ==========================================================
# Load BiomedCLIP
# ==========================================================

model, _, preprocess = open_clip.create_model_and_transforms(
    "hf-hub:microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224"
)

tokenizer = open_clip.get_tokenizer(
    "hf-hub:microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224"
)

model.eval()

# ==========================================================
# Disease prompt ensemble
# ==========================================================

disease_prompts = {

    "Normal": [
        "This is a normal chest radiograph.",
        "No acute cardiopulmonary abnormality is seen.",
        "The chest x-ray is normal."
    ],

    "Pneumonia": [
        "This chest radiograph demonstrates pneumonia.",
        "There are findings consistent with pneumonia.",
        "Patchy lung infiltrates suggest pneumonia."
    ],

    "Pneumothorax": [
        "This chest radiograph demonstrates pneumothorax.",
        "A collapsed lung is visible.",
        "Air is present in the pleural space."
    ],

    "Cardiomegaly": [
        "This chest radiograph demonstrates cardiomegaly.",
        "The cardiac silhouette is enlarged.",
        "An enlarged heart is visible."
    ],

    "Pleural Effusion": [
        "This chest radiograph demonstrates pleural effusion.",
        "Fluid accumulation is present around the lungs.",
        "Blunting of the costophrenic angle suggests pleural effusion."
    ],

    "Emphysema": [
        "This chest radiograph demonstrates emphysema.",
        "Hyperinflated lungs are present.",
        "Flattening of the diaphragm suggests emphysema."
    ],

    "Pulmonary Edema": [
        "This chest radiograph demonstrates pulmonary edema.",
        "Fluid accumulation within the lungs is present.",
        "Diffuse opacities suggest pulmonary edema."
    ],

    "Pulmonary Fibrosis": [
        "This chest radiograph demonstrates pulmonary fibrosis.",
        "Fibrotic changes are present.",
        "Interstitial scarring is visible."
    ],

    "Tuberculosis": [
        "This chest radiograph demonstrates pulmonary tuberculosis.",
        "Upper lobe cavitary lesions suggest tuberculosis.",
        "Pulmonary tuberculosis is present."
    ],

    "Lung Cancer": [
        "This chest radiograph demonstrates lung cancer.",
        "A pulmonary mass is visible.",
        "Findings suggest malignancy."
    ],

    "COPD": [
        "This chest radiograph demonstrates chronic obstructive pulmonary disease.",
        "Hyperinflation suggests COPD.",
        "Chronic obstructive pulmonary disease is present."
    ]
}


# ==========================================================
# Prediction Function
# ==========================================================

def predict_xray(image_path):

    # ------------------------------------------
    # Load image
    # ------------------------------------------

    image = preprocess(
        Image.open(image_path).convert("RGB")
    ).unsqueeze(0)

    with torch.no_grad():

        image_features = model.encode_image(
            image
        )

        image_features /= image_features.norm(
            dim=-1,
            keepdim=True
        )

        result = {}

        # --------------------------------------
        # Process each disease separately
        # --------------------------------------

        for disease, prompts in disease_prompts.items():

            text = tokenizer(
                prompts
            )

            text_features = model.encode_text(
                text
            )

            text_features /= text_features.norm(
                dim=-1,
                keepdim=True
            )

            # Average prompt embeddings
            avg_text_feature = text_features.mean(
                dim=0,
                keepdim=True
            )

            avg_text_feature /= avg_text_feature.norm(
                dim=-1,
                keepdim=True
            )

            similarity = (
                image_features @ avg_text_feature.T
            )

            score = similarity.item()

            result[disease] = score

    # ------------------------------------------
    # Min-Max normalization
    # ------------------------------------------

    values = torch.tensor(
        list(
            result.values()
        )
    )

    values = (
        values - values.min()
    ) / (
        values.max() - values.min() + 1e-8
    )

    normalized_result = {}

    for disease, value in zip(
        result.keys(),
        values
    ):

        normalized_result[disease] = float(
            value
        )

    return normalized_result
