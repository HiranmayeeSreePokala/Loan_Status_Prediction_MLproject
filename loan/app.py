from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('loan_model.pkl', 'rb'))

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the input values from the form
        data = {
            'Gender': request.form['Gender'],
            'Married': request.form['Married'],
            'Dependents': request.form['Dependents'],
            'Education': request.form['Education'],
            'Self_Employed': request.form['Self_Employed'],
            'ApplicantIncome': float(request.form['ApplicantIncome']),
            'CoapplicantIncome': float(request.form['CoapplicantIncome']),
            'LoanAmount': float(request.form['LoanAmount']),
            'Loan_Amount_Term': float(request.form['Loan_Amount_Term']),
            'Credit_History': float(request.form['Credit_History']),
            'Property_Area': request.form['Property_Area']
        }

        # Convert the input values to a numpy array
        input_data = np.array([[data['Gender'], data['Married'], data['Dependents'], data['Education'], data['Self_Employed'],
                                data['ApplicantIncome'], data['CoapplicantIncome'], data['LoanAmount'], data['Loan_Amount_Term'],
                                data['Credit_History'], data['Property_Area']]])

        # Make prediction
        prediction = model.predict(input_data)

        # Convert prediction to human-readable form
        

        return render_template('after.html', prediction=prediction)

if _name_ == '_main_':
    app.run(debug=True)