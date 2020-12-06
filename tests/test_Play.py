import unittest
from src.player import Player
from src.play import Play

class TestPlayClass(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player('Robin', 'scissors')
        self.player_2 = Player('Computer', 'paper')


    def test_player_has_name(self):
        self.assertEqual('Robin', self.player_1.name)

    def test_player_has_choice(self):
        self.assertEqual('paper', self.player_2.choice)