"""Flask server for emotion detection application."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the home page.
    """
    return render_template('index.html')

@app.route('/emotionDetector',methods=['GET'])
def emotion_detector_route():
    """
    Analyze text and return detected emotions.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")
    result = emotion_detector(text_to_analyze)

    # Handle invalid or blank text
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_response, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
