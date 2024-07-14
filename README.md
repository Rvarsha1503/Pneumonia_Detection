# Pneumonia_Detection



---

# Pneumonia Detection System

## Overview

The Pneumonia Detection System is a deep learning-based web application designed to assist in the early detection of pneumonia using chest X-ray images. This repository contains the code and resources necessary to train, deploy, and use the model.

## Features

- **Deep Learning Model:** Built on the VGG16 architecture for image classification.
- **Web Interface:** User-friendly interface to upload X-ray images and obtain diagnostic predictions.
- **Data Preprocessing:** Includes resizing, normalization, and dataset splitting for model training.
- **Flask API:** Backend API for serving the trained model and handling user requests.

## Dataset

The dataset used for training and testing the model can be downloaded from [Dataset Link](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Rvarsha1503/Pneumonia_Detection.git
   cd pneumonia-detection
   ```

2. Install dependencies:
   For Model training:
   ```
    pip install tensorflow

   ```
   ```
   import tensorflow as tf
   from tensorflow.keras.applications import VGG16
   from tensorflow.keras.models import Model
   from tensorflow.keras.layers import Dense, Flatten, Dropout
   from tensorflow.keras.preprocessing.image import ImageDataGenerator
   from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
   ```
   ---
   For app.py :
   ```
   Flask==2.0.2
   tensorflow==2.7.0
   numpy==1.22.0
   Flask-Mail==0.9.1

   ```
   ```
   from flask import Flask, request, jsonify, render_template, redirect, url_for
   import os
   from tensorflow.keras.models import load_model
   from tensorflow.keras.preprocessing.image import load_img, img_to_array
   import numpy as np
   from flask import redirect, flash
   import smtplib
   from email.mime.text import MIMEText
   import re
   import csv
   ```
## Usage

1. **Training:**
   - Place the dataset in the `data` directory.
   - Run `python train.py` to train the model.

2. **Deployment:**
   - Run `python app.py` to start the Flask server.
   - Access the web interface at `http://localhost:5000`.

## Directory Structure

```
.
├── data/               # Dataset directory (not included in repository)
├── models/             # Saved models directory
├── static/             # Static assets (CSS, images)
├── templates/          # HTML templates for web interface
├── app.py              # Flask application for serving the model
├── train.py            # Script for model training
└── README.md           # This README file
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

- Developed by [Your Name](https://github.com/Rvarsha1503)

---

