def infer_conditions(result):

    conditions = []

    # ============================================================
    # Pneumonia
    # ============================================================

    pneumonia_score = (
        0.5 * result.get("Pneumonia", 0)
        + 0.3 * result.get("Consolidation", 0)
        + 0.2 * result.get("Infiltration", 0)
    )

    if pneumonia_score > 0.55:

        conditions.append({

            "icon": "🦠",

            "name": "Possible Pneumonia",

            "confidence": pneumonia_score,

            "urgency": "Moderate",

            "recommendation":
            "Clinical evaluation and laboratory tests are recommended.",

            "next_tests":
            "CBC, sputum culture, CT chest",

            "explanation":
            "Findings suggest possible lung infection. Chest X-rays alone cannot determine bacterial, viral, or fungal causes."

        })


    # ============================================================
    # Tuberculosis
    # ============================================================

    tb_score = (
        0.4 * result.get("Fibrosis", 0)
        + 0.3 * result.get("Pleural_Thickening", 0)
        + 0.3 * result.get("Nodule", 0)
    )

    if tb_score > 0.55:

        conditions.append({

            "icon": "🫁",

            "name": "Tuberculosis Suspicion",

            "confidence": tb_score,

            "urgency": "Moderate",

            "recommendation":
            "Consult a pulmonologist.",

            "next_tests":
            "Sputum AFB, GeneXpert, CT chest",

            "explanation":
            "Certain radiographic findings may occasionally be seen in tuberculosis, but chest X-ray alone cannot confirm TB."

        })


    # ============================================================
    # COPD
    # ============================================================

    emphysema_score = result.get("Emphysema", 0)

    if emphysema_score > 0.65:

        conditions.append({

            "icon": "🚬",

            "name": "Possible COPD / Emphysema",

            "confidence": emphysema_score,

            "urgency": "Low",

            "recommendation":
            "Pulmonary function tests may be helpful.",

            "next_tests":
            "Spirometry",

            "explanation":
            "Emphysema findings may indicate chronic obstructive pulmonary disease."

        })


    # ============================================================
    # Lung Tumor
    # ============================================================

    tumor_score = (
        0.6 * result.get("Mass", 0)
        + 0.4 * result.get("Nodule", 0)
    )

    if tumor_score > 0.60:

        conditions.append({

            "icon": "🎗",

            "name": "Possible Lung Tumor",

            "confidence": tumor_score,

            "urgency": "High",

            "recommendation":
            "Further evaluation is strongly recommended.",

            "next_tests":
            "CT chest, PET scan, biopsy",

            "explanation":
            "Masses and nodules may represent benign or malignant tumors."

        })


    # ============================================================
    # Pneumothorax
    # ============================================================

    ptx_score = result.get("Pneumothorax", 0)

    if ptx_score > 0.75:

        conditions.append({

            "icon": "⚠️",

            "name": "Possible Pneumothorax",

            "confidence": ptx_score,

            "urgency": "Emergency",

            "recommendation":
            "Urgent medical attention is advised.",

            "next_tests":
            "Repeat chest X-ray, CT chest",

            "explanation":
            "Collapsed lung is a potentially serious condition."

        })


    # ============================================================
    # Heart Failure
    # ============================================================

    chf_score = (
        0.4 * result.get("Cardiomegaly", 0)
        + 0.3 * result.get("Effusion", 0)
        + 0.3 * result.get("Edema", 0)
    )

    if chf_score > 0.60:

        conditions.append({

            "icon": "❤️",

            "name": "Possible Congestive Heart Failure",

            "confidence": chf_score,

            "urgency": "Moderate",

            "recommendation":
            "Cardiology consultation is recommended.",

            "next_tests":
            "ECG, Echocardiography",

            "explanation":
            "Heart enlargement and fluid accumulation may suggest heart failure."

        })


    conditions.sort(
        key=lambda x: x["confidence"],
        reverse=True
    )

    return conditions