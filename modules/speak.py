"""
    Text To Speech
"""
import os

def speak(text):
    """
        wrapper function to execute espeak command in shell via python
    """
    os.system('espeak -vid+f1 -k5 -s150 "{}"'.format(str(text)))
