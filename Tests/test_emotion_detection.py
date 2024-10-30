import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import EmotionDetection as ED


class TestEmotionDetection(unittest.TestCase):

    def get_dominant_emotion(self, text):
        resp_dict = ED.emotion_detector(text_to_analyse=text)
        return resp_dict["dominant_emotion"]

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


if __name__ == "__main__":
    unittest.main()
