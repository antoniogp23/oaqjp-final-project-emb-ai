import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):

        # Case for 'I am glad this happened'
        res1 = emotion_detector('I am glad this happened')
        self.assertEqual(res1['dominant_emotion'], 'joy')

        # Case for 'I am really mad about this'
        res2 = emotion_detector('I am really mad about this')
        self.assertEqual(res2['dominant_emotion'], 'anger')

        # Case for 'I feel disgusted just hearing about this'
        res3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(res3['dominant_emotion'], 'disgust')

        # Case for 'I am so sad about this'
        res4 = emotion_detector('I am so sad about this')
        self.assertEqual(res4['dominant_emotion'], 'sadness')

        # Case for 'I am really afraid that this will happen'
        res5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(res5['dominant_emotion'], 'fear')


unittest.main()
