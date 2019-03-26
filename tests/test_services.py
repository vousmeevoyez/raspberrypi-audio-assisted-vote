"""
    Test Vote Services
"""
import requests
import unittest

try:
        from unittest.mock import MagicMock
except ImportError:
        from mock import Mock, patch

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
                                "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTMzMzgzNTQsImlhdCI6MTU1MzEyMjM1NCwic3ViIjoiODIzMDY4ODMtN2M0Zi00YWVhLThkN2YtNDU3MmVmZTdiZjllIiwidHlwZSI6IkFDQ0VTUyIsInJvbGUiOiJQQVJUSUNJUEFOVCJ9.ouDSy9w1yfex4mifIw82ow8_2kKU777Gjb6e2j8O6po",
                                        "user": {
                                                        "name": "Kim jennie",
                                                                    "id": "82306883-7c4f-4aea-8d7f-4572efe7bf9e",
                                                                                "username": "1",
                                                                                            "created_at": "2019-03-20 00:03:22",
                                                                                                        "identity_id": "111111",
                                                                                                                    "email": "jeje@bp.com",
                                                                                                                                "role": "PARTICIPANT",
                                                                                                                                            "status": "ACTIVE",
                                                                                                                                                        "msisdn": "081208121212"
                                                                                                                                                                }
                                                                                                                                                                    }
                                                                                                                                                                    }
        mock_remote_call.return_value = expected_data

        access_token, name = VoteServices().get_token("EVOTESUPERADMIN", "password")
        self.assertEqual(access_token, expected_data["data"]["access_token"])

    @patch.object(VoteServices, "remote_call")
    def test_get_candidates(self, mock_remote_call):
        token = \
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTIxODEzOTEsImlhdCI6MTU1MTk2NTM5MSwic3ViIjoiY2ZmZmQ5MTAtNjA2MC00MGNiLTg0NTktM2U0ODcxZDYwYzNkIiwidHlwZSI6IkFDQ0VTUyIsInJvbGUiOiJTVVBFUkFETUlOIn0.4MhVXBX3QkIuZtTyRArDT21jtRaiKriL2Bd2h6lNuxE"

        expected_data = {
                    "data": [
                                {
                                                "name": "contoh kandidat uin jakarta",
                                                            "users": [
                                                                                {
                                                                                                        "name": "ketuakandidat1",
                                                                                                                            "id": "bad6b2fe-4c34-4540-9e4a-53c815f7bc21",
                                                                                                                                                "username": "ketuakandidat1",
                                                                                                                                                                    "created_at": "2019-03-07 13:10:56",
                                                                                                                                                                                        "identity_id": "123456",
                                                                                                                                                                                                            "email": "ketuakandidat1@test.com",
                                                                                                                                                                                                                                "role": "PARTICIPANT",
                                                                                                                                                                                                                                                    "status": "ACTIVE",
                                                                                                                                                                                                                                                                        "msisdn": "0812081211"
                                                                                                                                                                                                                                                                                        },
                                                                                                                                                                                                                                                                                                        {
                                                                                                                                                                                                                                                                                                                            "name": "wakilkandidat1",
                                                                                                                                                                                                                                                                                                                                                "id": "923160ea-abe3-47f0-9d23-a9631d5b3321",
                                                                                                                                                                                                                                                                                                                                                                    "username": "wakilkandidat1",
                                                                                                                                                                                                                                                                                                                                                                                        "created_at": "2019-03-07 13:10:55",
                                                                                                                                                                                                                                                                                                                                                                                                            "identity_id": "123457",
                                                                                                                                                                                                                                                                                                                                                                                                                                "email": "wakilkandidat1@test.com",
                                                                                                                                                                                                                                                                                                                                                                                                                                                    "role": "PARTICIPANT",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        "status": "ACTIVE",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            "msisdn": "0812081212"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    "id": "7f84ba87-ac5f-4aa3-813d-2443e5c723b3",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                "images": "N/A",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            "order_no": "2",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        "votes": 1,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    "created_at": "2019-03-07 13:10:56",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                "status": "ACTIVE",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            "description": "deskripsi"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    },
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        "name": "contoh kandidat uin jakarta 2",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    "users": [
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        "name": "wakilkandidat2",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            "id": "4df14577-cdb6-4956-8ed3-d79fd77f2a83",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                "username": "ketuakandidat2",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    "created_at": "2019-03-07 13:10:55",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        "identity_id": "123458",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            "email": "ketuakandidat2@test.com",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                "role": "PARTICIPANT",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    "status": "ACTIVE",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        "msisdn": "0812081213"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        },
                                                                                                {
                                                                                                                        "name": "sayawakilkandidat2",
                                                                                                                                            "id": "e489cc2e-6912-4b03-a90d-d3b5cbb5dcb3",
                                                                                                                                                                "username": "wakilkandidat2",
                                                                                                                                                                                    "created_at": "2019-03-07 13:10:55",
                                                                                                                                                                                                        "identity_id": "123459",
                                                                                                                                                                                                                            "email": "wakilkanddiat2@test.com",
                                                                                                                                                                                                                                                "role": "PARTICIPANT",
                                                                                                                                                                                                                                                                    "status": "ACTIVE",
                                                                                                                                                                                                                                                                                        "msisdn": "0812081214"
                                                                                                                                                                                                                                                                                                        }
                                                                                                            ],
                                                                                                                        "id": "efe3ac2c-22df-4ea6-9353-f7b9c53410e7",
                                                                                                                                    "images": "N/A",
                                                                                                                                                "order_no": "1",
                                                                                                                                                            "votes": 2,
                                                                                                                                                                        "created_at": "2019-03-07 13:10:55",
                                                                                                                                                                                    "status": "ACTIVE",
                                                                                                                                                                                                "description": "deskripsi"
                                                                                                                                                                                                        }
                                                                                                                                                                                                            ]
                                                                                                                                                                                                            }
        mock_remote_call.return_value = expected_data

        sound_feedback, candidates = VoteServices(token).get_candidates("election_id")
        self.assertTrue(len(sound_feedback) > 0)
        self.assertTrue(len(candidates) > 0)

    @patch.object(VoteServices, "remote_call")
    def test_cast_vote(self, mock_remote_call):
        token = \
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTIxODEzOTEsImlhdCI6MTU1MTk2NTM5MSwic3ViIjoiY2ZmZmQ5MTAtNjA2MC00MGNiLTg0NTktM2U0ODcxZDYwYzNkIiwidHlwZSI6IkFDQ0VTUyIsInJvbGUiOiJTVVBFUkFETUlOIn0.4MhVXBX3QkIuZtTyRArDT21jtRaiKriL2Bd2h6lNuxE"

        expected_data = {}

        mock_remote_call.return_value = expected_data

        result = VoteServices(token).cast_vote("12345646")
        self.assertEqual(result, expected_data)

'''
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
    '''

if __name__ == "__main__":
    unittest.main()
