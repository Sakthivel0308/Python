import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)
    return roll

while True:
    players = input("Enter the No of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Player Must be between 2 and 4.")
            
    else:
        print("Invalid Player, Try again.")

max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:
    for player_index in range(players):
        print(f"\n Player {player_index+1}'s Turn:")
        print("Your Total Score: ", player_score[player_index],"\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to Roll (y/n): ")
            if should_roll.lower() != "y":
                break
            
            value =  roll()
            if value == 1:
                current_score = 0
                print("You rolled a 1!, Turn Over")
                break
            else:
                current_score += value
                print(f"You rolled a {value}.")
            print(f"your Current Score: {current_score}.")
        player_score[player_index] += current_score
        print(f"\n Player {player_index+1}'s Score: {player_score[player_index]}")

max_score = max(player_score)
winning_index = player_score.index(max_score)
print(f"Player Number: {winning_index+1} id the Winner with the score of {max_score}!")


