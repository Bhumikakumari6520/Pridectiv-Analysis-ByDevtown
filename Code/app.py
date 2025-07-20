from flask import Flask, request, render_template, jsonify
import pandas as pd
import pickle

# intialize flask app
app = Flask(__name__)

# Load trained model
try:
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    print("Error: File Not Found!")
    exit()

feature_names = [
    'age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 
    'ejection_fraction', 'high_blood_pressure', 'platelets', 
    'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time'
]

# Home page route
@app.route('/')
def home():
    """
    Home page render karta hai (index.html).
    """
    return render_template('index.html')


# Prediction page route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = {
            'age': float(request.form['age']),
            'anaemia': float(request.form['anaemia']),
            'creatinine_phosphokinase': float(request.form['creatinine_phosphokinase']),
            'diabetes': float(request.form['diabetes']),
            'ejection_fraction': float(request.form['ejection_fraction']),
            'high_blood_pressure': float(request.form['high_blood_pressure']),
            'platelets': float(request.form['platelets']),
            'serum_creatinine': float(request.form['serum_creatinine']),
            'serum_sodium': float(request.form['serum_sodium']),
            'sex': float(request.form['sex']),
            'smoking': float(request.form['smoking']),
            'time': float(request.form['time'])
        }

        # Make a dataframe from input data
        final_features = pd.DataFrame([input_data], columns=feature_names)
        
        # Get prediction from the Model
        prediction = model.predict(final_features)
        
        # Get Prediction probability
        prediction_proba = model.predict_proba(final_features)

        # Prepare output format text
        if prediction[0] == 1:
            probability_score = prediction_proba[0][1] * 100
            output_text = "High Risk of Heart Failure"
            result_message = f"Patient has a {probability_score:.2f}% probability of a heart failure event."
        else:
            probability_score = prediction_proba[0][0] * 100
            output_text = "Low Risk of Heart Failure"
            result_message = f"Patient has a {probability_score:.2f}% probability of being safe."

        return render_template('index.html', 
                               prediction_text=output_text, 
                               result_details=result_message,
                               show_result=True)

    except Exception as e:
        # Error handling
        error_message = f"An error occurred: {e}"
        return render_template('index.html', prediction_text=error_message)


# Run App
if __name__ == "__main__":
    app.run(debug=True) #this is for debug mode

