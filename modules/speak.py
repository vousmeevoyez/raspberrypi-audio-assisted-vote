"""
    Text To Speech
"""
import time
from subprocess import call
from config.config import *

def text_to_speech(sentences):
    """
        wrapper function to execute espeak command in shell via python
    """
    for sentence in sentences:
        call(["espeak", "-vid+f5", "-k5", "-s150", sentence])

'''
if __name__ == "__main__":
    text_to_speech("Hallo kelvin")
    text_to_speech("untuk dapat ke tahap selanjutnya silahkan katakan tampilkan\
                kandida")
'''
