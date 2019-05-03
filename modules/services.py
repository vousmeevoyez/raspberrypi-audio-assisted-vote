"""
    Services
    ________________
    this is where we communicate with server
"""
import os
import jwt
import grpc

from google.protobuf.json_format import MessageToDict

from rpc import auth_pb2
from rpc import auth_pb2_grpc
from rpc import user_pb2
from rpc import user_pb2_grpc
from rpc import candidate_pb2
from rpc import candidate_pb2_grpc

from config import *

class ResponseError(Exception):
    """ class raised when services error happen"""
    def __init__(self, message):
        self.message = message

class VoteServices:

    def __init__(self, token=None):
        self.channel = grpc.insecure_channel(GRPC_CHANNEL)
        self._access_token = token

    def get_token(self, username, password):
        stub = auth_pb2_grpc.AuthStub(self.channel)
        request = auth_pb2.AccessTokenRequest()
        # build request body
        request.username = username
        request.password = password
        try:
            response = stub.GetAccessToken(request)
        except grpc.RpcError as error:
            print(error.code())
            print(error.details())
            message = "Token tidak valid"
            raise ResponseError(message)
        #end try
        access_token = response.body.access_token
        return access_token

    def get_user(self):
        # decode token and extract user id
        payload = jwt.decode(self._access_token, os.getenv("JWT_SECRET"),
                             algorithms="HS256")

        user_id = payload["sub"]
        stub = user_pb2_grpc.UserStub(self.channel)
        request = user_pb2.GetUserRequest()
        # build request body
        request.header.access_token = self._access_token
        request.header.user_id = user_id
        try:
            response = stub.GetUser(request)
        except grpc.RpcError as error:
            print(error.code())
            print(error.details())
            message = "Pengguna tidak ditemukan"
            raise ResponseError(message)
        #end try
        return response.body

    def get_candidates(self, election_id):
        sound_feedback = []
        trimmed_candidates = []

        stub = candidate_pb2_grpc.CandidateStub(self.channel)
        request = candidate_pb2.GetCandidatesRequest()
        request.header.access_token = self._access_token
        request.header.election_id = election_id

        try:
            result = stub.GetCandidates(request)
        except grpc.RpcError:
            message = "Pemilihan tidak ditemukan"
            raise ResponseError(message)
        #end try

        # trim response
        # build list for sound feedback order
        for candidate in result.body:
            candidate = MessageToDict(candidate, preserving_proto_field_name=True)

            sound_feedback.append(candidate["order_no"])
            sound_feedback.append(candidate["name"])

            trimmed_candidates.append({
                "id" : candidate["id"],
                "order_no" : candidate["order_no"]
            })

        #print(sound_feedback)
        #print(trimmed_candidates)
        return sound_feedback, trimmed_candidates

    def cast_vote(self, candidate_id):
        """ cast a vote """
        stub = candidate_pb2_grpc.CandidateStub(self.channel)
        request = candidate_pb2.CastVoteRequest()
        request.header.access_token = self._access_token
        request.header.candidate_id = candidate_id
        try:
            response = stub.CastVote(request)
        except grpc.RpcError as error:
            raise ResponseError(error.details())
        #end try
        return True
