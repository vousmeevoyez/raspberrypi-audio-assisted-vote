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
