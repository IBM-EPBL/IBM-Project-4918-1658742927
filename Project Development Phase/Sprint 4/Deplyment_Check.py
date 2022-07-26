import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "EfnknPvhJ-_nFPaZrvBBWHMOp6KFamEZ2dAwkx-OU-rQ""
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["cylinders","displacement","horsepower","weight","acceleration","model year","origin"]], "values": [[8,307.0,130,3550,12.0,80,1]]}]}

response_scoring = requests.post(''https://us-south.ml.cloud.ibm.com/ml/v4/deployments/2cfb110f-6a0d-4967-9320-505e6b214a29/predictions?version=2022-11-18'', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json()["predictions"][0]["values"][0][0])