from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        test_result1 = emotion_detector("I am glad this happened")
        self.assertEqual(test_result1["dominant_emotion"], "joy")

        test_result2 = emotion_detector("I am really mad about this")
        self.assertEqual(test_result2["dominant_emotion"], "anger")

        test_result3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test_result3["dominant_emotion"], "disgust")

        test_result4 = emotion_detector("I am so sad about this")
        self.assertEqual(test_result4["dominant_emotion"], "sadness")

        test_result5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test_result5["dominant_emotion"], "fear")

unittest.main()
