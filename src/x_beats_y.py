def x_beats_y(player_1, player_2):
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