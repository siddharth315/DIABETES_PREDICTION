# Diabetes Prediction Using Machine Learning

A Machine Learning-based web application that predicts the likelihood of Diabetes using medical parameters. The system is built using Python and Flask and provides real-time predictions through a simple web interface.

---

## Project Overview

Diabetes is a serious chronic disease that affects millions of people worldwide. Early detection can help individuals take preventive measures and seek medical guidance.

This project uses a trained Machine Learning model to predict whether a person is likely to have diabetes based on health-related inputs.

---

## Features

- Predicts Diabetes based on user input
- Trained Machine Learning model
- Web-based interface using Flask
- Instant prediction results
- Clean and simple UI
- Modular project structure

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML
- CSS
- Pickle (for saving trained model)

---

## Input Parameters

The model takes the following health inputs:

- Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

---

## Machine Learning Model

- Dataset: PIMA Indians Diabetes Dataset
- Link: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database
- Algorithm Used: Logistic Regression
- Model saved as: `model.pkl`
- Training Script: `train_model.py`

The model is trained separately and loaded inside the Flask application (`app.py`) for prediction.

---

## Project Structure

```
diabetes-prediction/
│
├── model/                   # dataset
├── static/                  # CSS, images, JS files
├── templates/               # HTML files
├── app.py                   # Main Flask application
├── train_model.py           # Model training script
├── model.pkl                # Saved trained model
├── requirements.txt         # Required dependencies
└── README.md                # Project documentation
```

---

## Installation & Setup

### 1️) Clone the Repository

```bash
git clone https://github.com/your-username/diabetes-prediction.git
cd diabetes-prediction
```

### 2) Install Dependencies

```bash
pip install -r requirements.txt
```

### 3) Run the Application

```bash
python app.py
```

### 4) Open your browser and go to

```bash
http://127.0.0.1:5000/
```
