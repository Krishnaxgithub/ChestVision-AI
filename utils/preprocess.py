import cv2
import torch
import numpy as np
import torchxrayvision as xrv


def preprocess_image(path):

    # Read image
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # Convert to float32
    img = img.astype(np.float32)

    # Normalize to approximately [-1024,1024]
    img = xrv.datasets.normalize(img, 255)

    # Resize to 224×224
    img = cv2.resize(img, (224, 224))

    # Add channel dimension
    img = img[None, :, :]

    # Convert to tensor
    img = torch.from_numpy(img)

    # Add batch dimension
    img = img.unsqueeze(0)

    return img