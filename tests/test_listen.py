"""
    Test Vote Services
"""
import requests
import unittest
try:
            from unittest.mock import MagicMock
except ImportError:
            from mock import MagicMock

from modules.listen import SpeechProcessing

class TestMockSpeechProcessing(unittest.TestCase):

    '''
    def test_convert_to_transcript(self):
        expected_data = dict(
          "results"
            {
              "alternatives": [
                {
                  "confidence": 0.98267895,
                  "transcript": "how old is the Brooklyn Bridge"
                }
              ],
              "is_final" : True
            }
        )
        result = SpeechProcessing()._convert_to_transcript(expected_data)
        print(result)
    '''

    def test_convert_word_to_number(self):
        result = SpeechProcessing._convert_word_to_number("satu")
        self.assertEqual(result, 1)

        result = SpeechProcessing._convert_word_to_number("tiga")
        self.assertEqual(result, 3)

        with self.assertRaises(ValueError):
            result = SpeechProcessing._convert_word_to_number("jdsaljalsdkjlkasd")

    def test_order_no_to_candidate_id(self):
        candidates = [{
            "order_no" : "1",
            "candidate_id" : "asdjasldjlaksjldkjalsjdlsja"
        },
        {
            "order_no" : "2",
            "candidate_id" : "asdjlaksjldkjalsjdlsja"
        }]
        result = SpeechProcessing._order_no_to_candidate_id(candidates, "2")
        self.assertEqual(result, "asdjlaksjldkjalsjdlsja")
