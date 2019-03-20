"""
    Test Vote Services
"""
import requests
import unittest
from unittest.mock import Mock, patch

from modules.listen import SpeechProcessing

class TestMockSpeechProcessing(unittest.TestCase):

    def test_convert_to_transcript(self):
        expected_data = {
          "results": [
            {
              "alternatives": [
                {
                  "confidence": 0.98267895,
                  "transcript": "how old is the Brooklyn Bridge"
                }
              ]
            },
            {
              "alternatives": [
                {
                  "confidence": 0.98267895,
                  "transcript": "how old is the Brooklyn Bridge"
                }
              ]
            },
            {
              "alternatives": [
                {
                  "confidence": 0.98267895,
                  "transcript": "how old is the Brooklyn Bridge"
                }
              ]
            }
          ]
        }
        result = SpeechProcessing()._convert_to_transcript(expected_data)
        print(result)
