from src.player import Player

class Play():
    # def __init__(self, player_1_name, player_2_name, player_1_choice, player_2_choice):
    #     player_1 = Player(player_1_name, player_1_choice)
    #     player_2 = Player(player_2_name, player_2_choice)


    def game_logic(self, player_1, player_2):
        
        if player_1.choice == 'scissors' and player_2.choice  == 'paper':
            return player_1.name
        elif player_2.choice == 'scissors' and player_1.choice  == 'paper':
            return player_2.name

        elif player_1.choice == 'paper' and player_2.choice == 'rock':
            return player_1.name
        elif player_2.choice == 'paper' and player_1.choice == 'rock':
            return player_2.name

        elif  player_1.choice == 'rock' and player_2.choice == 'scissors':
            return player_1.name
        elif  player_2.choice == 'rock' and player_1.choice == 'scissors':
            return player_2.name

        
        elif player_1.choice == 'rock' and player_2.choice == 'rock':
            return None
        elif player_2.choice == 'rock' and player_1.choice == 'rock':
            return None

        elif player_1.choice == 'scissors' and player_2.choice == 'scissors':
            return None
        elif player_2.choice == 'scissors' and player_1.choice == 'scissors':
            return None

        elif player_1.choice == 'paper' and player_2.choice == 'paper':
            return None
        elif player_2.choice == 'paper' and player_1.choice == 'paper':
            return None