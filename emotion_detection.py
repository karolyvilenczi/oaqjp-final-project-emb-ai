
from pprint import pp
import requests
import json


def emotion_detector(text_to_analyse:str = '') -> str:
    watson = {
        "url":'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
        "Headers": {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        "Input":  { "raw_document": { "text": text_to_analyse } }
    }
    text = None

    resp = None
    try:
        resp = requests.post(
            url = watson["url"], 
            headers = watson["Headers"], 
            body=watson["Input"]
        )
    except Exception as e:
        print(f"Error executing request: {e}")
    else:
        text = resp.body
        pp(text)

    return text

if __name__ =="__main__":
    
    test_str = "I love this new technology."
    pp(emotion_detector(test_str))