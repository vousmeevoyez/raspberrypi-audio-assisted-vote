""" 
    Listen Stream
    ____________________
    this is module where we interact with microphone and open stream to google speech API
"""
import os
import re
import sys
import six

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

from six.moves import queue
from ctypes import *
from contextlib import contextmanager

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

from stream import MicrophoneStream
# configuration
from config import *
# services
from services import *
# speak utility
from speak import *

class SpeechProcessing:
    """ processing all the speech here"""

    button_pin = 3

    def __init__(self):
        self._token = None
        self._candidates = []

        GPIO.setwarnings(False) # Ignore warning for now
        GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 2 to be an input pin and set initial value to be pulled low (off)
        GPIO.add_event_detect(self.button_pin, GPIO.RISING,
                              callback=self.listen)

    @staticmethod
    def _convert_to_transcript(responses):
        """ convert cloud speech response to final transcript """
        finalize_transcript = ""
        for response in responses:
            for result in response.results:
                for alternative in result.alternatives:
                    if result.is_final:
                        finalize_transcript = result.alternatives[0].transcript
                        break
                        # stop
                    #end if
                else:
                    continue
                break
                #end for
            else:
                continue
            break
            #end for
        #end for
        return finalize_transcript

    def _convert_to_command(self, transcript):
        """
            match transcript to known command
            if its known executed it and if its not return an error
        """
        response = {
            "status"   : "RECOGNIZED",
            "feedback" : ""
        }
        sentences = []
        # first split result into "command and value"
        try:
            count = len(transcript.split(" "))
            if count < 2:
                response["status"] = "UNKNOWN"
                sentences.append("Perintah terlalu pendek")
                return response
            #end if
            command, value = transcript.split(" ")
        except ValueError:
            pass
        #end try

        # match first word with all registered command
        if re.search(r'\masuk|login\b', transcript, re.I):
            try:
                username = value
                access_token, user_name = VoteServices().get_token(username, os.environ.get("DEFAULT_PASSWORD"))
                # first greet user
                sentences.append(user_name)
                # second return insturction to continue
                sentences.append(SPEECH_RESPONSE["FIRST_STEP"].format(user_name))
                # dont forget set token here
                self._token = access_token
            except ResponseError as error:
                sentences.append(error.message)
            #end try
        elif re.search(r'\btampilkan\b', transcript, re.I):
            try:
                #authenticate as admin
                sound_feedback, candidates = \
                VoteServices(os.environ.get("DEFAULT_USERNAME"),
                             os.environ.get("DEFAULT_PASSWORD")).get_candidates(os.environ.get("ELECTION_ID"))
                # set sound feedbcak + instruction
                for feedback in sound_feedback:
                    sentences.append(feedback)
                #end for
                sentences.append(SPEECH_RESPONSE["SECOND_STEP"])
                # set candidates information so the function know the mapping
                print(candidates)
                self._candidates = candidates
            except ResponseError as error:
                sentences.append(error.message)
            #end try
        elif re.search(r'\bpilih\b', transcript, re.I):
            # first make sure value is integer not word
            order_no = None

            try:
                order_no = int(value)
            except ValueError:
                order_no = self._convert_word_to_number(value)
            #end try

            try:
                # convert order no to candidate_id
                candidate_id = self._order_no_to_candidate_id(self._candidates, order_no)
                response = VoteServices(token=self._token).cast_vote(candidate_id)
                sentences.append(SPEECH_RESPONSE["THIRD_STEP"])
            except ResponseError as error:
                sentences.append(error.message)
            #end try
        else:
            response["status"] = "UNKNOWN"
            sentences.append(SPEECH_RESPONSE["UNKNOWN"])

        # append result
        response["feedback"] = sentences
        return response

    @staticmethod
    def _process_feedback(command):
        # process the feedback
        if command["status"] == "RECOGNIZED":
            text_to_speech(command["feedback"])
        else:
            text_to_speech(command["feedback"])

    @staticmethod
    def _order_no_to_candidate_id(candidates, order_no):
        """ convert ord no to candidate id"""
        candidate_id = None
        for candidate in candidates:
            if candidate['order_no'] == str(order_no):
                candidate_id = candidate['id']
                break
            #end if
        #end for
        return candidate_id

    @staticmethod
    def _convert_word_to_number(word):
        known_number = ["nol", "satu", "dua", "tiga", "empat", "lima", "enam",
                        "tujuh", "delapan", "sembilan", "sepuluh"]
        value = {
            "nol"      : 0,
            "satu"     : 1,
            "dua"      : 2,
            "tiga"     : 3,
            "empat"    : 4,
            "lima"     : 5,
            "enam"     : 6,
            "tujuh"    : 7,
            "delapan"  : 8,
            "sembilan" : 9,
            "sepuluh"  : 10
        }
        if word not in known_number:
            raise ValueError
        #end if
        return value[word]


    def listen(self):
        """
            start listening microphone and initialize stream to google
        """
        # start speech client
        client = speech.SpeechClient()
        # initialize recogition config
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=RATE,
            language_code=LANGUAGE,
            speech_contexts=[speech.types.SpeechContext(phrases=HELPER_KEYWORD)],
            model=SPEECH_MODEL
        )
        # initialize streaming config
        streaming_config = types.StreamingRecognitionConfig(
            config=config,
            single_utterance=True,
            interim_results=True)

        with MicrophoneStream(RATE, CHUNK) as stream:
            audio_generator = stream.generator()
            requests = (types.StreamingRecognizeRequest(audio_content=content)
                        for content in audio_generator)

            responses = client.streaming_recognize(streaming_config, requests)
            print(responses)
            transcript = self._convert_to_transcript(responses)
            print(transcript)
            feedback = self._convert_to_command(transcript)
            print(feedback)
            final_result = self._process_feedback(feedback)
            stream.closed = True

    def start(self):
        message = input("press enter to quit")
        GPIO.cleanup()

if __name__ == '__main__':
    SpeechProcessing().start()
