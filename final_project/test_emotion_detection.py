# from emotion_analysis import emotion_detector, emotion_predictor
from EmotionDetection.emotion_detection import emotion_detector
from EmotionDetection.emotion_detection import emotion_predictor

# text_to_analyze = "I love this new technology."
text_to_analyze = "I am so happy I am doing this."

detected_emotions = emotion_detector(text_to_analyze)

if detected_emotions:
    formatted_emotions = emotion_predictor(detected_emotions)
    print(formatted_emotions)
else:
    print("No emotions detected or an error occurred.")