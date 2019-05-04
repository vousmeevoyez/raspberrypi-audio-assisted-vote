""" 
    Listen Stream
    ____________________
    this is module where we interact with microphone and open stream to google speech API
"""
# standard
from datetime import datetime
import os
import re
import io
# debugging
import logging
# audio processing
import pyaudio
import wave 
# external
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
# configuration
from config import *
# services
from services import *
# speak utility
from speak import *

logging.basicConfig(level=logging.INFO, filename="app.log",
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

class SpeechProcessing:
    """ processing all the speech here"""

    def __init__(self):
        self._token = None
        self._candidates = []

    @staticmethod
    def _convert_to_transcript(response):
        for result in response.results:
            print result.alternatives[0].transcript
            return result.alternatives[0].transcript

    @staticmethod
    def play_introduction():
        """ convert defined text to introduction speech """
        instruction_list = []
        instruction_list.append(SPEECH_RESPONSE["INSTRUCTION"])
        instruction_list.append(SPEECH_RESPONSE["INSTRUCTION_FIRST"])
        instruction_list.append(SPEECH_RESPONSE["INSTRUCTION_SECOND"])
        instruction_list.append(SPEECH_RESPONSE["INSTRUCTION_THIRD"])
        instruction_list.append(SPEECH_RESPONSE["INSTRUCTION_FOUR"])
        text_to_speech(instruction_list)

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
                response["feedback"] = sentences
                return response
            #end if
            command, value = transcript.split(" ")
        except ValueError:
            sentences.append("Perintah terlalu pendek")
        #end try

        # match first word with all registered command
        if re.search('masuk|login', transcript):
            try:
                username = value
                # get access token
                token = VoteServices().get_token(username, os.environ.get("DEFAULT_PASSWORD"))
                # get user information
                user = VoteServices(token).get_user()
                # first greet user
                sentences.append(user.name)
                # second return insturction to continue
                sentences.append(SPEECH_RESPONSE["FIRST_STEP"].format(user.name))
                # dont forget set token here
                self._token = token
            except ResponseError as error:
                sentences.append(error.message)
            #end try
        elif re.search('daftar|kandidat', transcript):
            try:
                #authenticate as admin
                admin_token = VoteServices().get_token(os.environ.get("ADMIN_USERNAME"),
                                                       os.environ.get("ADMIN_PASSWORD"))
                # get user information
                sound_feedback, candidates = \
                VoteServices(admin_token).get_candidates(os.environ.get("ELECTION_ID"))
                # set sound feedbcak + instruction
                for feedback in sound_feedback:
                    sentences.append(feedback)
                #end for
                sentences.append(SPEECH_RESPONSE["SECOND_STEP"])
                # set candidates information so the function know the mapping
                self._candidates = candidates
            except ResponseError as error:
                sentences.append(error.message)
            #end try
        elif re.search('pilih', transcript, re.I):
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
                result = VoteServices(self._token).cast_vote(candidate_id)
                sentences.append(SPEECH_RESPONSE["THIRD_STEP"])
            except ResponseError as error:
                sentences.append(error.message)
            #end try
        else:
            response["status"] = "UNKNOWN"
            sentences.append(SPEECH_RESPONSE["UNKNOWN"])
        #end if
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


    def translate(self, filename):
        """
            start listening microphone and initialize stream to google
        """
        with io.open(filename, 'rb') as audio_file:
            content = audio_file.read()

        # start speech client
        client = speech.SpeechClient()
        # build audio payload
        audio = types.RecognitionAudio(content=content)
        # initialize recogition config
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=RATE,
            language_code=LANGUAGE,
            speech_contexts=[speech.types.SpeechContext(phrases=HELPER_KEYWORD)],
            model=SPEECH_MODEL
        )

        responses = client.recognize(config, audio)
        transcript = self._convert_to_transcript(responses)
        logging.info(transcript)
        feedback = self._convert_to_command(transcript)
        logging.info(feedback)
        final_result = self._process_feedback(feedback)

    def record(self, channel):
        """ record audio here ...."""
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        CHUNK = 10
        RECORD_SECONDS = 3
        DIR = "record/"

        # generate file name
        filename = datetime.now().strftime("%Y%m%d-%H%M%S")

        audio = pyaudio.PyAudio()
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
        
        print("record here.....")
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        # end for
        print("stop recording.....")
        # close stream
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # write to file
        fullpath = DIR + filename + ".wav"
        wave_file = wave.open(fullpath, 'wb')
        wave_file.setnchannels(CHANNELS)
        wave_file.setsampwidth(audio.get_sample_size(FORMAT))
        wave_file.setframerate(RATE)
        wave_file.writeframes(b''.join(frames))
        wave_file.close()

        self.translate(fullpath)


if __name__ == '__main__':

    button_pin = 3

    speech_processing = SpeechProcessing()

    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 2 to be an input pin and set initial value to be pulled low (off)
    GPIO.add_event_detect(button_pin, GPIO.RISING,
                          callback=speech_processing.record)

    while True:
        text = raw_input("quit to exit")
        if text == "quit":
            break
            GPIO.cleanup()
        # end if
    # end while
