from EmotionDetection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotions(self):
        # Define test cases: (statement, expected dominant emotion)
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]

        for text, expected in test_cases:
            with self.subTest(text=text):
                result = emotion_detector(text)
                self.assertIn('dominant_emotion', result, "Output missing 'dominant_emotion'")
                self.assertEqual(result['dominant_emotion'], expected,
                                 f"Dominant emotion for '{text}' should be '{expected}' but got '{result['dominant_emotion']}'")

if __name__ == "__main__":
    unittest.main()
