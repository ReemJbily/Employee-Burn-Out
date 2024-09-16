from flask import Flask, request, jsonify,render_template, redirect, send_file, url_for
import pickle
import numpy as np
import pandas as pd
import catboost as cb

# Load the pre-trained model

app=Flask(__name__)

filename=r'C://Users//Windows.10//Employee-Burn-Out//burn-out-model-catboost.pk1'


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    # Extract form data
    work_period = 12.0
    data = {
        'Gender': int(request.args.get('Gender', 0)),
        'Company_Type': int(request.args.get('Company_Type', 0)),
        'Remote': int(request.args.get('Remote', 0)),
        'Designation': int(request.args.get('Designation', 0)),
        'Resource': int(request.args.get('Resource', 0)),
        'Mental_Fatigue_Score': float(request.args.get('Mental_Fatigue_Score', 0.0))
    }

    # Convert dictionary to DataFrame
    data_list = [data['Gender'], data['Company_Type'], data['Remote'], data['Designation'], data['Resource'],
                 data['Mental_Fatigue_Score'], work_period]

    # Perform prediction
    prediction_result = round(model.predict(data_list)*10000, 2)
    if prediction_result<0:
        prediction_result=-prediction_result
    return render_template('predict.html', prediction=prediction_result)

if __name__ == '__main__':
    model = pickle.load(open(filename, 'rb'))
    app.run(debug=True)
