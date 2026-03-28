# app.py

from flask import Flask, request, jsonify
from emotion_detection import detect_emotion

app = Flask(__name__)

@app.route('/emotion', methods=['POST'])
def emotion():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    result = detect_emotion(text)
    return jsonify(result)

if __name__ == "__main__":
    # Use port 5500 for Cloud IDE Kubernetes environment
    app.run(host='0.0.0.0', port=5500)