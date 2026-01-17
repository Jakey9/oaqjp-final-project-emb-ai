import requests
import json

def emotion_detector(text_to_analyse):
    """ use watson API to analyse emotion of text """
    """ test PR with my own main"""

    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    payload = {
        "raw_document": {
            "text": text_to_analyse 
        } 
    }

    response = requests.post(
        URL,
        headers=headers,
        data =json.dumps(payload)
    )

    return response.text
    