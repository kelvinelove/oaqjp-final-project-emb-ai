"""
Emotion Detection Server

This script defines a Flask-based server for performing emotion detection on user-provided text.

Author (Learner): [kelvinelove]
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

def run_emotion_detection():
    """
    Main function to run the Emotion Detection application.
    """
    app.run(host="0.0.0.0", port=5000)

@app.route("/emotionDetector", methods=['POST'])
def emotion_detector_route():
    """
    Analyze the user-provided text for emotions and return the result.
    """
    data = request.get_json()
    text_to_detect = data.get('statement', '')

    # Call the emotion detector function
    detected_emotions = emotion_detector(text_to_detect)

    if detected_emotions is None or detected_emotions['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400

    # Format the response message
    response_message = {
        "anger": detected_emotions['anger'],
        "disgust": detected_emotions['disgust'],
        "fear": detected_emotions['fear'],
        "joy": detected_emotions['joy'],
        "sadness": detected_emotions['sadness'],
        "dominant_emotion": detected_emotions['dominant_emotion']
    }

    return jsonify(response_message), 200

@app.route("/")
def render_index_page():
    """ 
    This function initiates the rendering of the main application 
    page over the Flask channel 
    """
    return render_template('index.html')

if __name__ == "__main__":
    run_emotion_detection()