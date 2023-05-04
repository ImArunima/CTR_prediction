# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 12:53:15 2023

@author: User1
"""

from flask import Flask, render_template, request
import numpy as np
import pickle
import os


#Create an app object using the Flask class. 
app = Flask(__name__)

#Load the trained model. (Pickle file)
model = pickle.load(open('model.pkl', 'rb'))

#use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        int_features = [float(x) for x in request.form.values()] #Convert string inputs to float.
        features = [np.array(int_features)]  #Convert to the form [[a, b]] for input to the model
        prediction = model.predict(features)  # features Must be in the form [[a, b]]
        
        output = round(prediction[0], 5)
        
        return render_template('index.html', prediction_text='Predicted CTR of the email campaign is {}'.format(output))
    

if __name__ == "__main__":
    app.run(debug = True)

