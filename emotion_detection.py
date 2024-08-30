import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=input_json, headers=header)
    formatted_response = json.loads(response.text)

    anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]

    dominant_emotion = None
    largest_score = 0.0
    for emotion, emotion_score in formatted_response["emotionPredictions"][0]["emotion"].items():
        if emotion_score > largest_score:
            dominant_emotion = emotion
            largest_score = emotion_score

    return {'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
           }
