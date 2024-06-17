# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:33:01 2024

@author: rd
"""

from flask import Flask, request, jsonify
import joblib
import pandas as pd


app = Flask(__name__)

@app.route("./predict", method=["POST"])

def predict():
    
    feat_data = request.json
    df = pd.DataFrame(feat_data)
    df = df.reindex(columns=col_names_Rishat)
    
    prediction = list(model.predict)
    
    return jsonify({"prediction", str(prediction)})


if "__name__" == "__main__":
    model = joblib.load("final_model_Rishat.pkl")
    col_names = joblib.load("col_names_Rishat.pkl")
    