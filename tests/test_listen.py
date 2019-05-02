"""
    Test Vote Services
"""
import requests
import unittest
try:
            from unittest.mock import patch, mock
except ImportError:
            from mock import patch

from modules.listen import SpeechProcessing
from modules.services import VoteServices

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
            "id" : "asdjasldjlaksjldkjalsjdlsja"
        },
        {
            "order_no" : "2",
            "id" : "asdjlaksjldkjalsjdlsja"
        }]
        result = SpeechProcessing._order_no_to_candidate_id(candidates, "2")
        self.assertEqual(result, "asdjlaksjldkjalsjdlsja")

<<<<<<< HEAD
    def test_convert_to_command(self):
        result = SpeechProcessing()._convert_to_command("hallo kelvin")
        print(result)
=======
    @patch.object(VoteServices, "get_token")
    def test_convert_to_command_get_token(self, mock_vote_services):
        result = SpeechProcessing()._convert_to_command("hallo kelvin")
        self.assertEqual(result['status'], "UNKNOWN")
        self.assertTrue(result['feedback'])

        result = SpeechProcessing()._convert_to_command("hallo")
        self.assertEqual(result['status'], "UNKNOWN")
        self.assertTrue(result['feedback'])

        mock_vote_services.return_value = "username", "some_token"
        result = SpeechProcessing()._convert_to_command("masuk 1")
        self.assertEqual(result['status'], "RECOGNIZED")
        self.assertTrue(result['feedback'])

    @patch.object(VoteServices, "get_candidates")
    def test_convert_to_command_get_candidates(self, mock_vote_services):
        dummy_sound_feedback = [ "1", "candidate 1", "2" ,"candidate 2"]
        dummy_candidates= [{
            "order_no" : "1",
            "id" : "asdjasldjlaksjldkjalsjdlsja"
        },
        {
            "order_no" : "2",
            "id" : "asdjlaksjldkjalsjdlsja"
        }]

        mock_vote_services.return_value = dummy_sound_feedback, dummy_candidates

        result = SpeechProcessing()._convert_to_command("tampilkan kandidat")
        self.assertEqual(result['status'], "RECOGNIZED")
        self.assertTrue(result['feedback'])

    @patch.object(VoteServices, "cast_vote")
    def test_convert_to_command_get_candidates(self, mock_vote_services):
        mock_vote_services.return_value = {
                "data" : "some services"
        }

        result = SpeechProcessing()._convert_to_command("pilih 1")
        print(result)
        self.assertEqual(result['status'], "RECOGNIZED")
        self.assertTrue(result['feedback'])
>>>>>>> 0ac66883d9c3aae060469dad4a34a47721332c0b
