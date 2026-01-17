from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/emotionDetector',methods=['POST'])
def emotionDetector():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Please provide a 'text' field in JSON"}), 400

    text_to_analyse = data['text']
    result = emotion_detector(text_to_analyze)

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