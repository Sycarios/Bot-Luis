# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
from enum import Enum
from typing import Dict
from botbuilder.ai.luis import LuisRecognizer, LuisPredictionOptions
from botbuilder.core import IntentScore, TopIntent, TurnContext
from config import DefaultConfig
from booking_details import BookingDetails

import requests
class Intent(Enum):
    BOOK_FLIGHT = "FlyMe"

    NONE_INTENT = "None"


def top_intent(intents: Dict[Intent, dict]) -> TopIntent:
    max_intent = Intent.NONE_INTENT
    max_value = 0.0

    for intent, value in intents:
        intent_score = IntentScore(value)
        if intent_score.score > max_value:
            max_intent, max_value = intent, intent_score.score

    return TopIntent(max_intent, max_value)


class LuisHelper:

    
        
    async def execute_luis_query(
         turn_context: TurnContext
    ) -> (Intent, object):
        """
        Returns an object with preformatted LUIS results for the bot's dialogs to consume.
        """
        result = BookingDetails()
        
        intent = "FlyMe"

        
        if intent == "FlyMe":

    
        
            utterance = turn_context.activity.text
            print(utterance)
        
    ##########

    # The headers to use in this REST call.
            headers = {
            }   

    # The URL parameters to use in this REST call.
            params ={
                'query': utterance,
        
                'subscription-key':  DefaultConfig.LUIS_API_KEY
            }


    # Make the REST call.
            response = requests.get(f'https://{DefaultConfig.LUIS_API_HOST_NAME}/luis/prediction/v3.0/apps/{DefaultConfig.LUIS_APP_ID}/slots/production/predict', headers=headers, params=params)

    # Display the results on the console.
            rep=response.json()
                
            try:# rep['prediction']['entities']['FlyMeBooking'][0]['or_city'][0]:

               result.or_city=rep['prediction']['entities']['FlyMeBooking'][0]['or_city'][0]
            except:
                print("no result")    

            try:# rep['prediction']['entities']['FlyMeBooking'][0]['dst_city'][0] in locals:
            
                result.dst_city=rep['prediction']['entities']['FlyMeBooking'][0]['dst_city'][0]
            except:
                print("no result")

            try:#  rep['prediction']['entities']['FlyMeBooking'][0]['str_date'][0]:
                
                result.str_date=rep['prediction']['entities']['FlyMeBooking'][0]['str_date'][0]
            except:
                print("no result")

            try:#  rep['prediction']['entities']['FlyMeBooking'][0]['end_date'][0]:
                
            
               result.end_date=rep['prediction']['entities']['FlyMeBooking'][0]['end_date'][0]
            except:
                print("no result")
                
            try:
                
            
               result.budget=rep['prediction']['entities']['FlyMeBooking'][0]['budget'][0]
            except:
                print("no result")

            try:
                
               result.sentence=rep['query']
            except:
                print("no result")

            try:
                
               result.prediction_luis=rep['prediction']
            except:
                print("no result")
        

        return intent,result

    
