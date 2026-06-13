# 🩻 ChestVision AI

An AI-powered chest X-ray analysis web application built using **Flask**, **PyTorch**, and **BiomedCLIP**.

---

## 📸 Preview

### Home Page

Upload a chest X-ray image and receive AI-generated findings and possible conditions.

*(Add screenshots here later)*

```text
screenshots/
    home.png
    result.png
```

---

## ✨ Features

* 🩻 Chest X-ray image upload
* 🤖 AI-powered disease prediction
* 📊 Confidence visualization
* 📖 Disease descriptions
* 🩺 Possible condition inference
* 🎨 Modern responsive UI
* ⚡ Flask backend
* 🔬 BiomedCLIP integration

---

## Supported Conditions

* Pneumonia
* Tuberculosis
* COPD
* Emphysema
* Pleural Effusion
* Pulmonary Edema
* Lung Cancer
* Pneumothorax
* Cardiomegaly
* Pulmonary Fibrosis

---

## Tech Stack

### Backend

* Python
* Flask
* PyTorch

### AI Models

* BiomedCLIP
* OpenCLIP

### Frontend

* HTML
* CSS
* Bootstrap 5

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Krishnaxgithub/ChestVision-AI.git

cd ChestVision-AI
```

### Create Virtual Environment

```bash
python3.11 -m venv venv
```

### Activate Environment

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
pip install open_clip_torch transformers sentencepiece
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Project Structure

```text
ChestVision-AI/

app.py

templates/
static/
utils/
uploads/
sample_images/

requirements.txt
README.md
```

---

## Future Improvements

* ✅ Grad-CAM heatmaps
* ✅ PDF report generation
* ✅ Downloadable diagnosis reports
* ✅ Better model calibration
* ✅ EfficientNetV2 training
* ✅ RSNA Pneumonia dataset integration
* ✅ CheXpert dataset integration
* ✅ Model ensemble
* ✅ Cloud deployment
* ✅ Hugging Face Spaces deployment

---

## Disclaimer

⚠️ This project is intended for educational and research purposes only and should not replace professional medical diagnosis.

---

## Author

**Krishna Sharma**

GitHub:

https://github.com/Krishnaxgithub
