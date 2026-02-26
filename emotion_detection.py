import requests # Necessary to send the POST request
import json

def emotion_detector(text_to_analyze): # Accepts 'text_to_analyze' as an argument
    # API configuration from Task 2 instructions
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input JSON format using the variable text_to_analyze
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Sending the POST request
    response = requests.post(url, json = myobj, headers = headers)
    
    # Returning the 'text' attribute of the response object
    return response.text