from flask import Flask, render_template,request
#import pickle
import numpy as np

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "EfnknPvhJ-_nFPaZrvBBWHMOp6KFamEZ2dAwkx-OU-rQ"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


app=Flask(__name__)
#model=pickle.load(open('regression.pkl','rb'))

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/model',methods=["GET","POST"])
def result():
    no_of_clynder=request.form["no_of_cylinders"]
    displacement=request.form["displacement"]
    horsepower=request.form["horsepower"]
    weight=request.form["weight"]
    acceleration=request.form["acceleration"]
    model_year=request.form["model_year"]
    origin=request.form["origin"]

    t1=[[int(no_of_clynder),float(displacement),int(horsepower),int(weight),float(acceleration),int(model_year),int(origin)]]
    
    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"field": [["cylinders","displacement","horsepower","weight","acceleration","model year","origin"]], "values": t1}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/2cfb110f-6a0d-4967-9320-505e6b214a29/predictions?version=2022-11-18', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    prediction=response_scoring.json()["predictions"][0]["values"][0][0]
    print(prediction)

    return render_template("index.html",y="The predicted MPG of the vehicle is ", z=str(prediction))

if __name__ == "__main__":
    app.run(debug=False)