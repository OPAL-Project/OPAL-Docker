import requests
import json
import configargparse
from configargparse import FileType

#####################################
# main program                      #
#####################################

# We parse all the arguments required by the manager
parser = configargparse.ArgumentParser(
    description='Submits jobs to be pre computed for OPAL.')
parser.add_argument('-f', '--json_file', type=FileType('r'), required=True,
                    help='json file containing all the jobs to be precomputed.')
parser.add_argument('-u', '--api_url', required=True,
                    help='URL of the OPAL API to submit to.')
parser.add_argument('-t', '--manager_token', required=True,
                    help='Token of the manager to submit to the API.')
args = parser.parse_args()

# URL of the OPAL API.
url = 'http://' + args.api_url + '/job/create'

# We load the json file and submit the different requests
data = json.load(args.json_file)

# Headers of the request please DO NOT EDIT
headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache"
}

for i in range(len(data)):
    # We format the request with the user token and the job
    request = {"opalUserToken": str(args.manager_token),
               "job": json.dumps(data[i])}

    # We send the request
    response = requests.post(url, json=request, headers=headers)

    # We print the response of the interface
    print(response.text)

print('All requests have been submitted.\nNumber of requests submitted: ' + str(i+1))
