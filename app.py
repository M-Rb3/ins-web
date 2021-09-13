from flask import Flask, url_for, render_template, redirect
from forms import PredictForm
from flask import request, sessions
import requests
from flask import json
from flask import jsonify
from flask import Request
from flask import Response
import urllib3
import json
# from flask_wtf import FlaskForm

app = Flask(__name__, instance_relative_config=False)
app.config["TEMPLATES_AUTO_RELOAD"] = True
# you will need a secret key
app.secret_key = 'bH9LdWff0kxs0LZL8wm3-P305XIS_xXLob1abwM3C25p'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


@app.route('/', methods=('GET', 'POST'))
def startApp():
    form = PredictForm()
    return render_template('index.html', form=form)


@app.route('/predict', methods=('GET', 'POST'))
def predict():
    form = PredictForm()
    if form.submit():

        token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={
                                       "apikey": 'bH9LdWff0kxs0LZL8wm3-P305XIS_xXLob1abwM3C25p', "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})

        mltoken = token_response.json()["access_token"]
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer '
                  + mltoken}

        if(form.bmi.data == None):
            python_object = []
        else:
            python_object = [form.age.data, form.sex.data, float(form.bmi.data),
                             form.children.data, form.smoker.data, form.region.data]
        # Transform python objects to  Json

        userInput = []
        userInput.append(python_object)

        payload_scoring = {"input_data": [{"fields": ["age", "sex", "bmi",
                                                      "children", "smoker", "region"], "values": userInput}]}

        response_scoring = requests.post(
            "https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/602a578d-1844-4b5c-957c-7f27ad888301/predictions?version=2021-09-13", json=payload_scoring, headers=header)

        output = json.loads(response_scoring.text)
        print(output)
        for key in output:
            ab = output[key]

        for key in ab[0]:
            bc = ab[0][key]

        roundedCharge = round(int(bc[0][0]), 2)

        form.abc = roundedCharge  # this returns the response back to the front page
        return render_template('index.html', form=form)
