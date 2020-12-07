import unittest
from src.x_beats_y import x_beats_y
from src.player import Player


class Test_X_Beats_Y(unittest.TestCase):
    def setUp(self):
        self.player_1  = Player('Robin', 'scissors') 
        self.player_2 = Player('Computer', 'paper')
        self.player_3  = Player('The Rock', 'rock') 
        self.player_4 = Player('Rocky', 'rock')

       
    def test_scissors__beats__paper(self):
        self.assertEqual('Robin', x_beats_y(self.player_1, self.player_2))
    def test_scissors__beats__paper_order_swap(self):
        self.assertEqual('Robin', x_beats_y(self.player_2, self.player_1))

        

    def test_paper__beats_rock_swap(self):
        self.assertEqual('Computer', x_beats_y(self.player_3, self.player_2))
    def test_paper__beats_rock(self):
        self.assertEqual('Computer', x_beats_y(self.player_2, self.player_3))
    


    def test_rock__beats__scissors(self):
        self.assertEqual('The Rock', x_beats_y(self.player_3, self.player_1))    
    def test_rock__beats__scissors_order_swap(self):
        self.assertEqual('The Rock', x_beats_y(self.player_1, self.player_3))


    def test_rock_v_rock__none(self):
        self.assertEqual(None, x_beats_y(self.player_3, self.player_4))
    def test_rock_v_rock__none_swap(self):
        self.assertEqual(None, x_beats_y(self.player_4, self.player_3))