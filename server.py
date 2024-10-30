
from flask import Flask, request, jsonify

import EmotionDetection

fapp = Flask(__name__)

@fapp.route(rule='/emotionDetector', methods=['GET','POST'])
def fetch_emotion():
    if request.method == 'GET':    
        return "To get emotions use POST!\n"
    if request.method == 'POST':
        print(request.body)
        return "OK\n"

if __name__ == "__main__":
    flask.run(debug=True)