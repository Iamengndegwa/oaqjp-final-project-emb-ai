import requests
import json  # for JSON parsing if needed
def detect_emotion(text_to_analyze):
    """
    Detect emotions from the input text using Watson NLP Emotion Predict API,
    extract relevant emotions, find dominant emotion, and return formatted dict.
    
    Args:
        text_to_analyze (str): The text to analyze emotions from.
    
    Returns:
        dict: Dictionary with emotion scores and dominant emotion.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        # Convert response text to dict (if response.json() not used)
        response_dict = response.json()
        
        # Example path to emotions in response (adjust if different)
        # Assuming emotions are in response_dict['emotion']['document']['emotion']
        emotions = response_dict.get('emotion', {}).get('document', {}).get('emotion', {})
        
        # Extract required emotions with default 0 if not present
        anger = emotions.get('anger', 0)
        disgust = emotions.get('disgust', 0)
        fear = emotions.get('fear', 0)
        joy = emotions.get('joy', 0)
        sadness = emotions.get('sadness', 0)
        
        # Create dictionary of emotions
        emotion_scores = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        
        # Find dominant emotion (emotion with highest score)
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Add dominant emotion to output
        emotion_scores['dominant_emotion'] = dominant_emotion
        
        return emotion_scores
    
    except requests.exceptions.RequestException as e:
        return {
            "error": "Request to Emotion Predict API failed",
            "details": str(e)
        }