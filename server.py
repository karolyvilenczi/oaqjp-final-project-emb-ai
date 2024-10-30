
from flask import Flask

import EmotionDetection

fapp = Flask(__name__)

@fapp.route('/emotionDetector')
def fetch_emotion():
    return "EMOTIONS"

if __name__ == "__main__":
    flask.run(debug=True)