from flask import Flask, request, jsonify,render_template, redirect, send_file, url_for
import pickle
import numpy as np
import pandas as pd
import catboost as cb

# Load the pre-trained model

app=Flask(__name__)

filename=r'C://Users//Windows.10//Employee-Burn-Out//burn-out-model.pk1'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Extract form data
        
        return redirect(url_for('prediction', **request.form))
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def prediction():
        gender=0
        company_type=0
        remote=0
        work_period=4.0
        data = {
            'Gender': str(request.form['Gender']),
            'Company_Type': str(request.form['Company Type']),
            'Remote': str(request.form['Remote']),
            'Designation': int(request.form['Designation']),
            'Resource': int(request.form['Resource']),
            'Mental_Fatigue_Score': float(request.form['Mental Fatigue Score'])
        }
        if data['Gender']=='Male':
            gender=1
        else:
            gender=0
        
        if data['Company_Type']=='Service':
            company_type=1
        else:
            company_type=0

        if data['Remote']=='Remote':
            remote=1
        else:
            remote=0   
        # Convert dictionary to DataFrame
        data_list = [gender,company_type,remote,data['Designation'],data['Resource'],
                           data['Mental_Fatigue_Score'],work_period]

        # Perform prediction

        prediction_result = round(model.predict(data_list)*100,2)
        return render_template('predict.html', prediction=prediction_result)

if __name__ == '__main__':
    model = pickle.load(open(filename, 'rb'))
    prediction_result = None 
    app.run(debug=True)    