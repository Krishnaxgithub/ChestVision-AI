
from utils.biomedclip_predict import predict_xray

result = predict_xray(
    "sample_images/test.png"
)

sorted_result = sorted(
    result.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nTop Predictions:\n")

for disease, score in sorted_result:

    print(
        f"{disease:20s} {score:.4f}"
    )
