import torchxrayvision as xrv

# Load pretrained NIH model
model = xrv.models.DenseNet(
    weights="densenet121-res224-nih"
)

model.eval()
