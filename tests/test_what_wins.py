# import unittest
# from src.what_wins import beats
# from src.choice import Choice


# class TestPlayerChoice(unittest.TestCase):
#     def setUp(self):
#         self.scissors  = Choice('scissors') 
#         self.paper = Choice('paper')
#         self.rock = Choice('rock')


       
#     def test_scissors__beats__paper(self):
#         self.assertEqual('scissors', beats(self.scissors, self.paper))
#     def test_scissors__beats__paper_order_swap(self):
#         self.assertEqual('scissors', beats(self.paper, self.scissors))

        

#     def test_paper__beats__rock_order_swap(self):
#         self.assertEqual('paper', beats(self.rock, self.paper))
#     def test_paper__beats__rock(self):
#         self.assertEqual('paper', beats(self.paper, self.rock))
    


#     def test_rock__beats__scissors(self):
#         self.assertEqual('rock', beats(self.rock, self.scissors))    
#     def test_rock__beats__scissors_order_swap(self):
#         self.assertEqual('rock', beats(self.scissors, self.rock))