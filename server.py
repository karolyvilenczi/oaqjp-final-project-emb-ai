"""
This module handles the flask server logic.
"""

from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

import EmotionDetection

fapp = Flask(__name__)


@fapp.route(rule="/emotionDetector", methods=["GET", "POST"])
def fetch_emotion():
    """
        Uses the EmotionDetection api to fetch data
    """
    req_data = None
    if request.method == "GET":
        return "To get emotions use POST!\n", 404

    if request.method == "POST":
        req_data = None
        
        try:
            data = request.json
            if data is None:
                raise BadRequest("No JSON data provided.")
        except BadRequest as br:
            return jsonify({"error": f"Bad Request: {br}"}), 500
        except Exception as e:
            return jsonify({"error": f"Unexpected error: {e}"}), 500
        else:
            req_data = data

        if req_data["text"] == "":
            return jsonify({"error": "Invalid text! Please try again!"}), 400

        try:
            emot_resp = EmotionDetection.emotion_detector(
                text_to_analyse=req_data["text"]
            )
        except Exception as e:
            return jsonify({"error":f"Cannot process request: {e}"}), 500
        else:
            response = f"For the given statement, the system response is 'anger': {emot_resp['anger']}, 'disgust': {emot_resp['disgust']}, 'fear': {emot_resp['fear']}, 'joy': {emot_resp['joy']} and 'sadness': {emot_resp['sadness']}. The dominant emotion is {emot_resp['dominant_emotion']}."
            return response


if __name__ == "__main__":
    fapp.run(debug=True)
    