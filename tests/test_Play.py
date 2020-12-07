import unittest
from src.player import Player
from src.play import Play

class TestPlayClass(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player('Robin', 'scissors')
        self.player_2 = Player('Computer', 'paper')
        self.game_1 = Play()


    def test_player_has_name(self):
        self.assertEqual('Robin', self.player_1.name)

    def test_player_has_choice(self):
        self.assertEqual('paper', self.player_2.choice)

    def test_play_game_logic(self):
        winner = self.game_1.game_logic(self.player_1.choice, self.player_2.choice)
        print(winner)