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
GRPC_CHANNEL = "34.80.69.106:5001"
SPEECH_RESPONSE = {
    "UNKNOWN"    : "Perintah tidak dikenali, silahkan ulangi",
    "GREETING"   : "Halo {}",
    "FIRST_STEP" : "untuk ke tahap selanjutnya silahkan katakan tampilkan\
    kandidat",
    "SECOND_STEP": "Pilih kandidat dengan katakan pilih nomor kandidat",
    "THIRD_STEP" : "Suara anda telah terekam, terima kasih"
}
