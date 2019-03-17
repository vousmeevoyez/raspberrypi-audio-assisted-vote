"""
    Text To Speech
"""
import os

def speak(text):
    """
        wrapper function to execute espeak command in shell via python
    """
    os.system('espeak -vid+f1 -k5 -s150 "{}"'.format(str(text)))


if __name__ == "__main__":
    speak("Hai Kelvin, apa kabar?")
