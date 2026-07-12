"""
Unit tests for the emotion_detector function.
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """Tests for the emotion detection module."""
    def test_emotion_detector(self):
        """Test various statements for their expected dominant emotion."""
        # 1. I am glad this happened -> joy
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # 2. I am really mad about this -> anger
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # 3. I feel so disgusted just hearing about this -> disgust
        result_3 = emotion_detector("I feel so disgusted just hearing about this")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # 4. I am so sad about this -> sadness
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # 5. I am really afraid that this will happen -> fear
        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
