import random

def roll_dice():
    return random.randint(1, 6)

def snake_ladder(player_position, snakes, ladders):
    # updates player position and checks for snakes or ladders
    if player_position in snakes:
        print("Oops! Snake bite!")
        return snakes[player_position]
    elif player_position in ladders:
        print("Yay! You found a ladder!")
        return ladders[player_position]
    else:
        return player_position

def play_game():
    # main code
    snakes = {17: 7, 54: 34, 62: 19, 98: 79}
    ladders = {3: 16, 8: 31, 20: 38, 28: 84, 40: 59, 63: 81, 71: 91}
    player1_position = 1
    player2_position = 1
    turn = 1 # 1 for player 1, 2 for player 2

    while True:
        input(f"Player {turn}, press Enter to roll the dice.")
        dice_roll = roll_dice()
        print(f"Dice roll: {dice_roll}")

        if turn == 1:
            player1_position += dice_roll
            player1_position = snake_ladder(player1_position, snakes, ladders)
            if player1_position > 100:
                player1_position -= dice_roll
            print(f"Player 1 position: {player1_position} \nPlayer 2 position: {player2_position}")
            if player1_position == 100:
                print("Player 1 wins!")
                break
            turn = 2
        else:
            player2_position += dice_roll
            player2_position = snake_ladder(player2_position, snakes, ladders)
            if player2_position > 100:
                player2_position -= dice_roll
            print(f"Player 1 position: {player1_position} \nPlayer 2 position: {player2_position}")
            if player2_position == 100:
                print("Player 2 wins!")
                break
            turn = 1

play_game()