""" 
    Listen Stream
    ____________________
    this is module where we interact with microphone and open stream to google speech API
"""
from __future__ import division

import os
import re
import sys
import six

from six.moves import queue
from ctypes import *
from contextlib import contextmanager

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import pyaudio
# configuration
from config import *
# services
from services import *
# speak utility
from speak import *

"""
    CONSUME ERROR CODE HERE SO IT DISPLAY LOG CORRECTLY
"""
ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def py_error_handler(filename, line, function, err, fmt):
    pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

@contextmanager
def noalsaerr():
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)

class MicrophoneStream:
    """Opens a recording stream as a generator yielding the audio chunks."""
    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        with noalsaerr():
            self._audio_interface = pyaudio.PyAudio()
            self._audio_stream = self._audio_interface.open(
                format=pyaudio.paInt16,
                # The API currently only supports 1-channel (mono) audio
                # https://goo.gl/z757pE
                channels=1, rate=self._rate,
                # select devices here
                input_device_index=2,
                input=True, frames_per_buffer=self._chunk,
                # Run the audio stream asynchronously to fill the buffer object.
                # This is necessary so that the input device's buffer doesn't
                # overflow while the calling thread makes network requests, etc.
                stream_callback=self._fill_buffer,
            )

            self.closed = False
            return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b''.join(data)

class SpeechProcessing:
    """ processing all the speech here"""

    def __init__(self):
        self._token = None
        self._candidates = []

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
            command, value = transcript.split(" ")
        except ValueError:
            pass

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
        elif re.search(r'\b(tampilkan)\b', transcript, re.I):
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
        elif re.search(r'\b(pilih)\b', transcript, re.I):
            # first make sure value is integer not word
            order_no = None

            try:
                order_no = int(value)
            except ValueError:
                order_no = self._convert_word_to_number(value)
            #end try

            try:
                # convert order no to candidate_id
                candidate_id = self._order_no_to_candidate_id(str(order_no))
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

    def _order_no_to_candidate_id(self, order_no):
        candidate_id = None
        for candidate in self._candidates:
            if candidate[order_no]:
                candidate_id = candidate['candidate_id']
                break

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

        return value[word]


    def stream_and_listen(self):
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

        command = ""
        while command != "exit":
            command = six.moves.input("enter command ")
            with MicrophoneStream(RATE, CHUNK) as stream:
                audio_generator = stream.generator()
                requests = (types.StreamingRecognizeRequest(audio_content=content)
                            for content in audio_generator)

                responses = client.streaming_recognize(streaming_config, requests)
                transcript = self._convert_to_transcript(responses)
                print(transcript)
                feedback = self._convert_to_command(transcript)
                print(feedback)
                final_result = self._process_feedback(feedback)
                stream.closed = True

if __name__ == '__main__':
    SpeechProcessing().stream_and_listen()
