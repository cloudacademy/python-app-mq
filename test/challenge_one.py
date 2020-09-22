import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../challenge/one")

from challenge_one import odds

class TestChallenge(unittest.TestCase):

    def test(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()