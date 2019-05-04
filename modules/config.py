"""
    Configuration
"""
import os

RATE = 44100
CHUNK = int(RATE/10)
LANGUAGE = "id-ID" # set indonesian language
TIMEOUT = 10 # second time out
HELPER_KEYWORD = ["instruksi", "pilih", "masuk", "daftar", "kandidat"]
SPEECH_MODEL = "command_and_search"
GRPC_CHANNEL = "34.80.69.106:5001"
SPEECH_RESPONSE = {
    "INSTRUCTION": "Berikut adalah petunjuk penggunaan sistem: sistem mengenali 3 buah instruksi yaitu masuk nomor identitas, daftar kandidat, pilih kandidat ",
    "INSTRUCTION_FIRST": "Langkah pertama adalah autentikasi: untuk masuk kedalam sistem cukup katakan masuk nomor identitas yang nanti akan diberikan oleh admin contoh masuk satu",
    "INSTRUCTION_SECOND": "Langkah kedua adalah daftar kandidat: setelah masuk kedalam sistem cukup katakan daftar kandidat",
    "INSTRUCTION_THIRD": "Langkah ketiga adalah pilih kandidat: setelah mengetahui daftar kandidat cukup katakan pilih nomor kandidat yang diinginkan contoh pilih satu",
    "INSTRUCTION_FOUR": "Untuk mulai menggunakan silahkan tekan tombol",
    "UNKNOWN"    : "Perintah tidak dikenali, silahkan ulangi",
    "GREETING"   : "Halo {}",
    "FIRST_STEP" : "untuk ke tahap selanjutnya silahkan katakan daftar\
    kandidat",
    "SECOND_STEP": "Pilih kandidat dengan katakan pilih nomor kandidat",
    "THIRD_STEP" : "Suara anda telah terekam, terima kasih"
}
