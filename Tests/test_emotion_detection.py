import unittest
import sys
import os
from pprint import pp

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import EmotionDetection as ED
from server import fapp


class TestEmotionDetection(unittest.TestCase):

    def get_dominant_emotion(self, text=''):
        resp_dict = None
        try:
            resp_dict = ED.emotion_detector(text_to_analyse=text)
        except TypeError as e:
            raise
            print(f"Error calling ED.emotion_detector: {e=}")
        
        return resp_dict["dominant_emotion"] if resp_dict else None
    

    def test_joy(self):
        self.assertEqual(self.get_dominant_emotion("I am glad this happened"), "joy")

    def test_anger(self):
        self.assertEqual(
            self.get_dominant_emotion("I am really mad about this"), "anger"
        )

    def test_disgust(self):
        self.assertEqual(
            self.get_dominant_emotion("I feel disgusted just hearing about this"),
            "disgust",
        )

    def test_sadness(self):
        self.assertEqual(self.get_dominant_emotion("I am so sad about this"), "sadness")

    def test_fear(self):
        self.assertEqual(
            self.get_dominant_emotion("I am really afraid that this will happen"),
            "fear",
        )

    def test_empty(self):
        with self.assertRaises(TypeError) as context:
            self.get_dominant_emotion(text='')
        

class TestFlaskApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.client = fapp.test_client()

    def test_get_emotion_successful(self):
        """Test a successful response"""
        response = self.client.post('/emotionDetector', json={"text": "I love my life"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('The dominant emotion is joy.', response.text)


    def test_get_emotion_error(self):
        """Test response when 'text' is missing"""
        response = self.client.post('/emotionDetector', json={"text": ""})
        # print(response.text)
        self.assertEqual(response.status_code, 400)
        self.assertEqual('{"error":"Text field cannot be empty!"}\n', response.text)

if __name__ == "__main__":
    unittest.main()
