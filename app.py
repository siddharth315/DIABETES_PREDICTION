from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        pregnancies = int(request.form['Pregnancies'])
        glucose = int(request.form['Glucose'])
        blood_pressure = int(request.form['BloodPressure'])
        skin_thickness = int(request.form['SkinThickness'])
        insulin = int(request.form['Insulin'])
        bmi = float(request.form['BMI'])
        dpf = float(request.form['DiabetesPedigreeFunction']) if request.form['DiabetesPedigreeFunction'] else 0.5
        age = int(request.form['Age'])

        features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
        prediction = model.predict(features)

        result = "The person is likely to have diabetes." if prediction[0] == 1 else "The person is not likely to have diabetes."

        input_summary = {
            "Pregnancies": pregnancies,
            "Glucose": glucose,
            "Blood Pressure": blood_pressure,
            "Skin Thickness": skin_thickness,
            "Insulin": insulin,
            "BMI": bmi,
            "Diabetes Pedigree Function": dpf,
            "Age": age
        }

        return render_template('result.html', result=result, inputs=input_summary)

    except Exception as e:
        return render_template('result.html', result="Error in prediction: " + str(e), inputs={})

if __name__ == '__main__':
    app.run(debug=True)
