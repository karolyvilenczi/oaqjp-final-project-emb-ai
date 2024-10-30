
"""
This module contains the unittest TestCases.
"""
import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import EmotionDetection as ED
from server import fapp


class TestEmotionDetection(unittest.TestCase):
    """
    Class to contain tests for the EmotionDetection module
    """

    def get_dominant_emotion(self, text=""):
        """        
        Gets the dominant emotion.
        """
        resp_dict = None
        try:
            resp_dict = ED.emotion_detector(text_to_analyse=text)
        except TypeError as e:
            print(f"Error calling ED.emotion_detector: {e=}")
            raise

        return resp_dict["dominant_emotion"] if resp_dict else None

    def test_joy(self):
        """        
        Tests joy
        """
        self.assertEqual(self.get_dominant_emotion("I am glad this happened"), "joy")

    def test_anger(self):
        """
        Tests anger        
        """
        self.assertEqual(
            self.get_dominant_emotion("I am really mad about this"), "anger"
        )

    def test_disgust(self):
        """
        Tests disg.
        """
        self.assertEqual(
            self.get_dominant_emotion("I feel disgusted just hearing about this"),
            "disgust",
        )

    def test_sadness(self):
        """
        Tests sadness        
        """
        self.assertEqual(self.get_dominant_emotion("I am so sad about this"), "sadness")

    def test_fear(self):
        """
        Tests fear
        """
        self.assertEqual(
            self.get_dominant_emotion("I am really afraid that this will happen"),
            "fear",
        )

    def test_empty(self):
        """
        Tests if emty, should raise a TypeErr        
        """
        with self.assertRaises(TypeError) as context:                        
            print(f"{context=}")
            self.get_dominant_emotion(text="")


class TestFlaskApp(unittest.TestCase):
    """
    Class to contain flask related tests
    """

    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.client = fapp.test_client()

    def test_get_emotion_successful(self):
        """Test a successful response"""
        response = self.client.post("/emotionDetector", json={"text": "I love my life"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("The dominant emotion is joy.", response.text)

    def test_get_emotion_error(self):
        """Test response when 'text' is missing"""
        response = self.client.post("/emotionDetector", json={"text": ""})
        # print(response.text)
        self.assertEqual(response.status_code, 400)
        self.assertEqual('{"error":"Invalid text! Please try again!"}\n', response.text)


if __name__ == "__main__":
    unittest.main()
