import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """Test cases for the emotion_detector function"""
    
    def test_emotion_detector_joy(self):
        """Test detection of joy emotion"""
        result = emotion_detector("I am glad this happened")
        #print(result['dominant_emotion'])
        self.assertEqual(result['dominant_emotion'],"joy")
    
    def test_emotion_detector_anger(self):
        """Test detection of anger emotion"""
        result = emotion_detector("I am really mad about this")
        #print(result['dominant_emotion'])
        self.assertEqual(result['dominant_emotion'],"anger")

    def test_emotion_detector_disgust(self):
        """Test detection of disgust emotion"""
        result = emotion_detector("I feel disgusted just hearing about this")
        #print(result['dominant_emotion'])
        self.assertEqual(result['dominant_emotion'],"disgust")

    def test_emotion_detector_sadness(self):
        """Test detection of sadness emotion"""
        result = emotion_detector("I am so sad about this")
        #print(result['dominant_emotion'])
        self.assertEqual(result['dominant_emotion'],"sadness")

    def test_emotion_detector_fear(self):
        """Test detection of fear emotion"""
        result = emotion_detector("I am really afraid that this will happen")
        #print(result['dominant_emotion'])
        self.assertEqual(result['dominant_emotion'],"fear")

if __name__ == '__main__':
    unittest.main()

