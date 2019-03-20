"""
    Services
    ________________
    this is where we communicate with server
"""
import requests
import json

from config import *

class ResponseError(Exception):
    """ class raised when services error happen"""
    def __init__(self, message):
        self.message = message

class VoteServices:

    def __init__(self, username=None, password=None, token=None):
        if username and password:
            self._token = self.get_token(username, password)
        else:
            self._token = token

    def remote_call(self, routes, payload=None, identifier=None):
        """ remote call"""
        # append identifier to URL
        if identifier is not None:
            url = BASE_URL + ROUTES[routes]
            url = url.format(identifier)
        else:
            url = BASE_URL + ROUTES[routes]

        # set token only if its not login
        if routes != "LOGIN":
            headers = {
                "Authorization" : "Bearer {}".format(self._token)
            }
        else:
            headers = {}

        if payload is not None:
            response = requests.post(
                url,
                data=payload,
                timeout=TIMEOUT,
                headers=headers
            )
        else:
            response = requests.get(
                url,
                timeout=TIMEOUT,
                headers=headers
            )

        if response.ok:
            response = response.json()
        else:
            print(response.json())
            raise ResponseError(response.json()["error"])
        return response

    def get_token(self, username, password):
        routes = "LOGIN"
        payload = {
            "username" : username,
            "password" : password
        }
        try:
            response = self.remote_call(routes, payload)
        except ResponseError as error:
            if error.message == "USER_NOT_FOUND":
                message = "Pengguna tidak ditemukan"
            raise ResponseError(message)
        #end try
        name = response["data"]["user"]["name"]
        access_token = response["data"]["access_token"]
        # trim information here so it only return access token and user name
        return access_token, name

    def get_candidates(self, election_id):
        routes = "CANDIDATES"
        sound_feedback = []
        candidates = []
        try:
            response = self.remote_call(routes=routes, identifier=election_id)
        except ResponseError as error:
            if error.message == "ELECTION_NOT_FOUND":
                message = "Pemilihan tidak ditemukan"
            raise ResponseError(message)
        #end try
        # trim response
        candidates = response["data"]
        # build list for sound feedback order
        for candidate in candidates:
            if candidate['order_no']:
                sound_feedback.append(candidate['order_no'])
            elif candidate['name']:
                sound_feedback.append(candidate['name'])
                candidate.append({
                    "id" : candidate['id'],
                    "order_no" : candidate['order_no']
                })

        return sound_feedback, candidates

    def cast_vote(self, candidate_id):
        routes = "VOTE"
        try:
            response = self.remote_call(routes, {}, candidate_id)
        except ResponseError as error:
            raise ResponseError(error.message)
        #end try
        return response
