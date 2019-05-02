"""
    Test Vote Services
"""
import unittest

from modules.services import VoteServices

class TestVoteServices(unittest.TestCase):

    def test_get_token(self):
        result = VoteServices().get_token("admin", "p4ssw0rd")
        print(result)

if __name__ == "__main__":
    unittest.main()
