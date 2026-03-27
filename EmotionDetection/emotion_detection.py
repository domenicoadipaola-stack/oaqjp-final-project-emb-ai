import requests
import json
    
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyse } }
    
    # Send the POST request
    response = requests.post(url, json=myobj, headers=headers)

        # Check if the request was successful (status code 200-299)
    if response.status_code == 200:
        res = json.loads(response.text)
        # Process the response as needed
        # Extract emotion scores
        emotions = res['emotionPredictions'][0]['emotion']
    
    elif response.status_code == 400:
        # Handle blank entries - return dictionary with None values
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        # Handle other errors
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Find the dominant emotion (highest score)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Add dominant_emotion to the result
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    
    return result