Heart Failure Prediction Web App This is a Machine Learning project built for the DevTown Predictive Modelling Bootcamp. The project aims to predict the mortality rate caused by heart failure based on various clinical features. The repository includes a trained RandomForestClassifier model and a Flask web application to interact with the model.

Project Overview The core of this project is a predictive model that analyzes 12 clinical features to determine the likelihood of a heart failure event. A user-friendly web interface, built with Flask and HTML/CSS, allows users to input these features and receive a real-time prediction.

Model Accuracy: The trained model achieves an accuracy of over 80% on the test dataset.

Problem Statement To build a robust machine learning model that can accurately predict heart failure mortality using a given set of clinical records. The secondary goal is to deploy this model as a simple and interactive web application.

Dataset The project uses the Heart Failure Prediction dataset, which contains clinical records of 299 patients. The dataset heart_failure_clinical_records_dataset.csv is included in this repository.

The 12 features used for prediction are:

age

anaemia

creatinine_phosphokinase

diabetes

ejection_fraction

high_blood_pressure

platelets

serum_creatinine

serum_sodium

sex

smoking

time (Follow-up period)

Folder Structure The project repository is organized as per the bootcamp guidelines:

External CSS for styling
├── templates/ │ 
└── index.html # The main HTML file for the web app 
├── app.py # The Flask application backend 
├── Heart_Failure_Prediction.ipynb # Jupyter Notebook for model training & EDA
├── model.pkl # The saved, trained machine learning model

How to Run the Project To set up and run this project on your local machine, follow these steps:

Clone the Repository:
git clone https://github.com/Bhumikakumari6520/Predictive-Analysis_ByDevtown.git cd your-repository-name

Create a Virtual Environment (Recommended):
python -m venv venv source venv/bin/activate # On Windows, use venv\Scripts\activate

Install Dependencies: pip install pandas scikit-learn flask

Train the Model (Optional): The repository already contains a pre-trained model.pkl file. However, if you wish to train the model yourself, run the Heart_Failure_Prediction.ipynb notebook in a Jupyter environment. This will generate a new model.pkl file.

Run the Flask App: Execute the app.py script from your terminal.

python app.py

Access the Web App: Open your web browser and go to the following URL: http://127.0.0.1:5000
You can now input patient data into the form and get predictions!

Technologies Used Backend: Python, Flask

Machine Learning: Scikit-learn, Pandas

Frontend: HTML, CSS

Development: Jupyter Notebook
