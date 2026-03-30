import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    
    response = requests.post(url, json=myobj, headers=headers)
        # Convert response text (JSON string) to a dictionary
    response_dict = json.loads(response.text)
        # Extract emotions and their scores (adjust keys based on actual response structure)
    emotions = response_dict.get('document_tone', {}).get('tones', [])
    # Create a dictionary with default 0 scores
    emotion_scores = {
        'anger': 0,
        'disgust': 0,
        'fear': 0,
        'joy': 0,
        'sadness': 0
    }
    
    # Populate emotion_scores with actual values from response
    for tone in emotions:
        tone_name = tone.get('tone_id')
        tone_score = tone.get('score', 0)
        if tone_name in emotion_scores:
            emotion_scores[tone_name] = tone_score
    
    # Find dominant emotion (emotion with the highest score)
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Add dominant emotion to the dictionary
    emotion_scores['dominant_emotion'] = dominant_emotion
    
    return emotion_scores