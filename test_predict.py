from utils.predict import predict_xray

path = "sample_images/test.png"

result = predict_xray(path)

sorted_result = sorted(
    result.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nTop 5 Predictions:\n")

for disease, score in sorted_result[:5]:
    print(
        f"{disease:20s} {score:.4f}"
    )
