import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        response = requests.post(URL, json=input_json, headers=header)
        response.raise_for_status()
        
        response_dict = response.json()
        
        emotions = response_dict.get('emotionPredictions', [{}])[0].get('emotion', {})
        
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 2)
        sadness_score = emotions.get('sadness', 0)

        all_emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        
        dominant_emotion = max(all_emotions, key=all_emotions.get)

        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

    except requests.exceptions.HTTPError as err:
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        else:
            print(f"HTTP error occurred: {err}")
            return None

def emotion_predictor(detected_text):
    if not detected_text or all(value is None for value in detected_text.values()):
        return detected_text
    
    emotions = detected_text.get('emotionPredictions', [{}])[0].get('emotion', {})
    
    anger = emotions.get('anger')
    disgust = emotions.get('disgust')
    fear = emotions.get('fear')
    joy = emotions.get('joy')
    sadness = emotions.get('sadness')
    
    max_emotion = max(emotions, key=emotions.get, default=None)

    formatted_dict_emotions = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': max_emotion
    }
    
    return formatted_dict_emotions