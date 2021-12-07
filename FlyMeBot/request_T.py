import requests
import config
  # The headers to use in this REST call.
  # 
headers = {
            }   

    # The URL parameters to use in this REST call.
params ={
        'query': 'utterance',
        
        'subscription-key': config.DefaultConfig.LUIS_API_KEY
    }


    # Make the REST call.

def response(headers,params):
    r =requests.get(f'https://lasta.cognitiveservices.azure.com/luis/prediction/v3.0/apps/c4cb4b1a-f70d-4575-a4d5-b04c7e1d4812/slots/production/predict', headers=headers, params=params)
    if r.status_code == 200: # Was the request made succefully ?
        return True

    elif r.status_code == 404:
        return False

