import unittest
from src.choice import Choice

class TestChoice(unittest.TestCase):
    def setUp(self):
        self.scissors  = Choice('scissors')
        self.paper = Choice('paper')
        self.rock = Choice('rock')

    def test_Choice_has_description(self):
        self.assertEqual('scissors', self.scissors.choice)