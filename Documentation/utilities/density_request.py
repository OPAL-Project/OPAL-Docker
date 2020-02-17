import requests
import json

# URL of the OPAL API. Replace 127.0.0.1:3001 by the proper URL
url = "http://127.0.0.1:3001/job/create"

# Definition of the job request for the density algorithm. NB: density do not have any params
# NB: the dates are in ISO compliant format and only an ISODate is accepted by the platform
job = {"startDate": "2013-01-01T00:00:01Z",
       "endDate": "2013-12-31T23:59:59Z",
       "algorithmName": "density",
       "resolution": "antenna",
       "keySelector": [],
       "sample": 0.01,
       "params": {}
       }

# We format the request with the user token and the job
data = {"opalUserToken": "qwerty1234",
        "job": json.dumps(job)}

# Headers of the request please DO NOT EDIT
headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache"
}

# We send the request
response = requests.post(url, json=data, headers=headers)

# We print the response of the interface
print(response.text)
