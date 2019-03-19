"""
    Configuration
"""
import os

RATE = 44100
CHUNK = int(RATE/10)
LANGUAGE = "id-ID" # set indonesian language
TIMEOUT = 10 # second time out
HELPER_KEYWORD = ["pilih", "masuk", "tampilkan", "kandidat"]
SPEECH_MODEL = "command_and_search"
BASE_URL = "http://34.80.69.106:5000/api/v1"
ROUTES = {
    "LOGIN"  : "/auth/login",
    "LOGOUT" : "/auth/logout",
    "CANDIDATES" : "/elections/{}/candidates/",
    "VOTE"       : "/votes/{}"
}
SPEECH_RESPONSE = {
    "UNKNOWN"    : "Perintah tidak dikenali, silahkan ulangi",
    "GREETING"   : "Halo {}",
    "FIRST_STEP" : "untuk dapat ke tahap selanjutnya silahkan katakan tampilkan\
    kandidat",
    "SECOND_STEP": "Pilih kandidat dengan katakan pilih kandidat",
    "THIRD_SETP" : "Suara anda telah terekam, terima kasih"
}
