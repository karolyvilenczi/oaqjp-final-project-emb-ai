
from pprint import pp
import requests
import json

def find_dominant_emotion(resp_emotions:dict) -> dict:
    dominant_emotion = max(resp_emotions, key = resp_emotions.get )
    print(f"{dominant_emotion=}")
    return dominant_emotion



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
        picked_response = resp.json().get('emotionPredictions', None)[0].get('emotion', None)
        return picked_response
    else:
        print("Error:", resp.status_code, resp.text)
        return None


if __name__ =="__main__":
    
    test_str = "I love this new technology."
    emotions = emotion_detector(test_str)
    print(f"{emotions=}")
    dom = find_dominant_emotion(resp_emotions = emotions)
    print(f"{dom=}")