# Early Stage Alzheimer's Disease Detection

A desktop application that predicts Alzheimer's risk from patient age and cognitive scores, with a Tkinter-based GUI for uploading MRI/CT scans and viewing generated reports.

## Overview

This project explores early-stage Alzheimer's detection using a simple machine learning pipeline built on cognitive assessment data (memory, thinking, and decision-making scores) combined with patient age. It includes:

- A trained Random Forest classifier
- A desktop GUI (login/register + prediction dashboard) built with Tkinter
- Sample cognitive datasets used for training and testing
- Sample MRI/CT scan images for demonstration

## Project Structure

```
├── src/
│   ├── gui.py            # Main application - login system + prediction dashboard
│   └── train_model.py    # Script used to train and save the Random Forest model
├── data/
│   ├── cognitive_data_500_samples.csv   # Larger sample dataset (500 records)
│   └── sample_patient_data.csv          # Smaller sample dataset
├── images/
│   ├── ct_scan_sample.jpg
│   ├── mri_sample_1.jpg
│   └── mri_sample_2.jpg
└── models/
    └── alzheimer_model.pkl   # Pre-trained model
```

## How It Works

1. **Training** (`train_model.py`): Takes patient records (age, memory, thinking, and decision scores) and trains a `RandomForestClassifier` to predict Alzheimer's risk (0 = normal, 1 = at risk). The trained model is serialized with `pickle`.

2. **GUI application** (`gui.py`): 
   - A login/register/reset system (credentials stored locally in a plain text file, not included in this repo)
   - A main dashboard where you enter patient details, upload an MRI/CT scan, and get a prediction
   - Image-based feature extraction: converts the uploaded scan to grayscale and derives rough memory/thinking/decision indicators from pixel intensity
   - A dataset analysis tool that summarizes age distribution across a CSV of patient records

## Getting Started

### Requirements

```
pandas
scikit-learn
pillow
numpy
```

Install with:
```bash
pip install pandas scikit-learn pillow numpy
```

### Running

1. Train the model (optional — a pre-trained model is already included in `models/`):
   ```bash
   python src/train_model.py
   ```

2. Launch the GUI:
   ```bash
   python src/gui.py
   ```

## Known Limitations

- The image-based feature extraction is a simplified heuristic based on average pixel intensity, not a proper CNN-based image analysis — it's meant to demonstrate the prediction workflow rather than serve as clinically accurate image diagnostics.
- The training dataset is small; predictions are for demonstration purposes only and not intended for real diagnostic use.
- `gui.py` includes optional sound alerts using Python's `winsound` module, which only works on Windows. On other operating systems, remove or replace that block to run the app.
- User authentication is stored in a local plaintext file for simplicity and is not included in this repository — you'll need to register a user the first time you run the app.

## Disclaimer

This is an academic/personal project built for learning purposes. It is **not** a validated medical diagnostic tool and should not be used for real clinical decision-making.
