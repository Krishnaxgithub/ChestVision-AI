from utils.predict import predict_xray
import os

folder = "nih/images-small"

files = os.listdir(folder)[:5]

for file in files:

    print("\n", file)

    result = predict_xray(
        os.path.join(folder, file)
    )

    result.pop("", None)

    sorted_result = sorted(
        result.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for disease, score in sorted_result[:5]:
        print(
            f"{disease:20s} {score:.4f}"
        )