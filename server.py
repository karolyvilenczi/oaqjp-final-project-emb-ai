"""
This module handles the flask server logic.
"""

from flask import Flask, request, jsonify

import EmotionDetection

fapp = Flask(__name__)


@fapp.route(rule="/emotionDetector", methods=["GET", "POST"])
def fetch_emotion():
    req_data = None
    if request.method == "GET":
        return "To get emotions use POST!\n", 404

    if request.method == "POST":
        # print(f"!!!!!!!!!!!!!! {request.json=}, {type(request.json)=}")
        req_data = None
        try:
            data = request.json
        except Exception as e:
            return jsonify({"error": f"Cannot process request: {e}"}), 500
        else:
            req_data = data

        if req_data["text"] == "":
            return jsonify({"error": f"Invalid text! Please try again!"}), 400

        try:
            emot_resp = EmotionDetection.emotion_detector(
                text_to_analyse=req_data["text"]
            )
        except Exception as e:
            return jsonify({"error:Cannot process request"}), 500
        else:
            response = f"For the given statement, the system response is 'anger': {emot_resp['anger']}, 'disgust': {emot_resp['disgust']}, 'fear': {emot_resp['fear']}, 'joy': {emot_resp['joy']} and 'sadness': {emot_resp['sadness']}. The dominant emotion is {emot_resp['dominant_emotion']}."
            return response

        return "testing", 200


if __name__ == "__main__":
    flask.run(debug=True)