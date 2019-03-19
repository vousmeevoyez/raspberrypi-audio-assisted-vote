"""
    Text To Speech
"""
import os
import time
from config import *

def text_to_speech(text):
    """
        wrapper function to execute espeak command in shell via python
    """
    os.system('espeak -vid+f1 -k5 -s200"{}"'.format(str(text)))

def greet_login(username):
    """
        shortcut function to greet user that successfully logged in
    """
    text_to_speech(SPEECH_RESPONSE["GREETING"].format(username))
    time.sleep(0.003)
    text_to_speech(SPEECH_RESPONSE["FIRST_STEP"])

def show_candidates(candidates):
    """
        shortcut function to show candidates via speech
    """
    for candidate in candidates:
        # access candidate name
        text_to_speech(candidate["name"])
