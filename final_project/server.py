from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector", methods=['POST'])
def emotion_detector_route():

    data = request.get_json()
    text_to_detect = data.get('statement', '')

    detected_emotions = emotion_detector(text_to_detect)

    if detected_emotions is None or detected_emotions['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400

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

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='localhost', port=5000)