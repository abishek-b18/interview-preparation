from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from feature import extract_features

app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])

def predict():

    data=request.form['text']

    features=extract_features(data)

    prediction=model.predict([features])

    result=prediction[0]

    return jsonify({
        "prediction":str(result)
    })


if __name__=="__main__":

    app.run(
        debug=True
    )