import os 

RATE = 44100
CHUNK = int(RATE/10)
LANGUAGE = "id-ID" # set indonesian language
TIMEOUT = 10 # second time out
BASE_URL = "http://34.80.84.152:5000/api/v1"
ROUTES = {
    "LOGIN"  : "/auth/login",
    "LOGOUT" : "/auth/logout",
    "CANDIDATES" : "/elections/{}/candidates/",
    "VOTE"       : "/votes/{}"
}
