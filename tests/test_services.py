"""
    Test Vote Services
"""
import requests
import unittest
from unittest.mock import Mock, patch

from modules.services import VoteServices

class TestMockVoteServices(unittest.TestCase):

    @patch("requests.post")
    def test_remote_call(self, mock_post):
        payload = {
            "username" : "someusername",
            "password" : "somepassword"
        }

        expected_data = {
            "data": {
                "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTIxODEzOTEsImlhdCI6MTU1MTk2NTM5MSwic3ViIjoiY2ZmZmQ5MTAtNjA2MC00MGNiLTg0NTktM2U0ODcxZDYwYzNkIiwidHlwZSI6IkFDQ0VTUyIsInJvbGUiOiJTVVBFUkFETUlOIn0.4MhVXBX3QkIuZtTyRArDT21jtRaiKriL2Bd2h6lNuxE"
                }
        }
        mock_post.return_value = Mock()
        mock_post.return_value.json.return_value = expected_data

        result = VoteServices().remote_call("LOGIN", payload)
        self.assertEqual(result, expected_data)

    @patch.object(VoteServices, "remote_call")
    def test_get_token(self, mock_remote_call):
        expected_data = {
            "data": {
                "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTIxODEzOTEsImlhdCI6MTU1MTk2NTM5MSwic3ViIjoiY2ZmZmQ5MTAtNjA2MC00MGNiLTg0NTktM2U0ODcxZDYwYzNkIiwidHlwZSI6IkFDQ0VTUyIsInJvbGUiOiJTVVBFUkFETUlOIn0.4MhVXBX3QkIuZtTyRArDT21jtRaiKriL2Bd2h6lNuxE"
                }
        }
        mock_remote_call.return_value = expected_data

        result = VoteServices().get_token("EVOTESUPERADMIN", "password")
        self.assertEqual(result, expected_data["data"]["access_token"])

    @patch.object(VoteServices, "remote_call")
    def test_get_candidates(self, mock_remote_call):
        token = \
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTIxODEzOTEsImlhdCI6MTU1MTk2NTM5MSwic3ViIjoiY2ZmZmQ5MTAtNjA2MC00MGNiLTg0NTktM2U0ODcxZDYwYzNkIiwidHlwZSI6IkFDQ0VTUyIsInJvbGUiOiJTVVBFUkFETUlOIn0.4MhVXBX3QkIuZtTyRArDT21jtRaiKriL2Bd2h6lNuxE"

        expected_data = {
            "data": [
                {
                    "description": "candidates description",
                    "images": "N/A",
                    "users": [
                        {
                            "status": "ACTIVE",
                            "username": "ketuakandidat1",
                            "id": "bad6b2fe-4c34-4540-9e4a-53c815f7bc21",
                            "identity_id": "123456",
                            "msisdn": "0812081211",
                            "created_at": "2019-03-07 13:10:56",
                            "role": "PARTICIPANT",
                            "email": "ketuakandidat1@test.com",
                            "name": "ketuakandidat1"
                        },
                        {
                            "status": "ACTIVE",
                            "username": "wakilkandidat1",
                            "id": "923160ea-abe3-47f0-9d23-a9631d5b3321",
                            "identity_id": "123457",
                            "msisdn": "0812081212",
                            "created_at": "2019-03-07 13:10:55",
                            "role": "PARTICIPANT",
                            "email": "wakilkandidat1@test.com",
                            "name": "wakilkandidat1"
                        }
                    ],
                    "votes": 0,
                    "id": "7f84ba87-ac5f-4aa3-813d-2443e5c723b3",
                    "created_at": "2019-03-07 13:10:56",
                    "status": "ACTIVE",
                    "name": "Kandidat1"
                },
                {
                    "description": "candidates description",
                    "images": "N/A",
                    "users": [
                        {
                            "status": "ACTIVE",
                            "username": "ketuakandidat2",
                            "id": "4df14577-cdb6-4956-8ed3-d79fd77f2a83",
                            "identity_id": "123458",
                            "msisdn": "0812081213",
                            "created_at": "2019-03-07 13:10:55",
                            "role": "PARTICIPANT",
                            "email": "ketuakandidat2@test.com",
                            "name": "wakilkandidat2"
                        },
                        {
                            "status": "ACTIVE",
                            "username": "wakilkandidat2",
                            "id": "e489cc2e-6912-4b03-a90d-d3b5cbb5dcb3",
                            "identity_id": "123459",
                            "msisdn": "0812081214",
                            "created_at": "2019-03-07 13:10:55",
                            "role": "PARTICIPANT",
                            "email": "wakilkanddiat2@test.com",
                            "name": "sayawakilkandidat2"
                        }
                    ],
                    "votes": 0,
                    "id": "efe3ac2c-22df-4ea6-9353-f7b9c53410e7",
                    "created_at": "2019-03-07 13:10:55",
                    "status": "ACTIVE",
                    "name": "Kandidat2"
                    }
                ]
        }
        mock_remote_call.return_value = expected_data

        result = VoteServices(token).get_candidates("election_id")
        self.assertEqual(result, expected_data)

    @patch.object(VoteServices, "remote_call")
    def test_cast_vote(self, mock_remote_call):
        token = \
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTIxODEzOTEsImlhdCI6MTU1MTk2NTM5MSwic3ViIjoiY2ZmZmQ5MTAtNjA2MC00MGNiLTg0NTktM2U0ODcxZDYwYzNkIiwidHlwZSI6IkFDQ0VTUyIsInJvbGUiOiJTVVBFUkFETUlOIn0.4MhVXBX3QkIuZtTyRArDT21jtRaiKriL2Bd2h6lNuxE"

        expected_data = {}

        mock_remote_call.return_value = expected_data

        result = VoteServices(token).cast_vote("12345646")
        self.assertEqual(result, expected_data)

class TestVoteServices(unittest.TestCase):

    def test_get_candidates(self):
        election_id = "651e3a24-5d49-40bb-b737-d27b52ca7858"
        result = VoteServices("EVOTESUPERADMIN",
                              "password").get_candidates(election_id)
        self.assertTrue(result["data"])
        self.assertTrue(len(result["data"]) > 0)

    def test_vote_candidates(self):
        election_id = "651e3a24-5d49-40bb-b737-d27b52ca7858"
        result = VoteServices("EVOTESUPERADMIN",
                              "password").get_candidates(election_id)
        self.assertTrue(result["data"])
        self.assertTrue(len(result["data"]) > 0)

        candidate_id = result["data"][0]["id"]

        result = VoteServices("EVOTESUPERADMIN",
                              "password").cast_vote(candidate_id)
        print(result)
