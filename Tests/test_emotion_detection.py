
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import EmotionDetection

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        ...

    def test_anger(self):
        ...
    
    def test_disgust(self):
        ...

    def test_sadness(self):
        ...
    
    def test_fear(self):
        ...

if __name__ == '__main__':
    unittest.main()