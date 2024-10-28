
from pprint import pp
import requests
import json


def emotion_detector(text_to_analyse:str = '') -> str:
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = { 
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock',
        'Content-Type': 'application/json'
    }
    data = {
        "raw_document": {
            "text": text_to_analyse
        }   
    }

    resp = None
    try:
        response = requests.post(url, headers=headers, json=data)
    except Exception as e:
        print(f"Error at processing reques: {e}")
        return None
    else:
        resp = response
    
    if resp.status_code == 200:
        print(f"Response: {resp.json()}")
        return resp.json()
    else:
        print("Error:", resp.status_code, resp.text)
        return None

if __name__ =="__main__":
    
    test_str = "I love this new technology."
    pp(emotion_detector(test_str))