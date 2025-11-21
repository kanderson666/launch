import json
import random

CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']

# Open the JSON file for reading
with open('rps.json', 'r') as file:
    MESSAGE = json.load(file)

def get_choice():
    while True:
        weapon = input(f'{", ".join(CHOICES)}? ').casefold()
        if weapon in CHOICES:
            return weapon
        print(MESSAGE['error'])

def get_comp():
    return CHOICES[random.randint(0, 4)]

def determine_winner(play_choice, com_choice):
    if play_choice == com_choice:
        return "Tie"

    play_index = CHOICES.index(play_choice)
    com_index = CHOICES.index(com_choice)

    #adding any of these index offsets to your choice results in a win
    WIN_INDEXES = [-3, -1, 2, 4]
    for win_index in WIN_INDEXES:
        if com_index + win_index == play_index:
            return "Comp wins"

    return "Player wins"

def print_results(play_choice, com_choice, winners, com_wins, play_wins):
    print(f'\nPlayer chose: {play_choice}\nComp chose: {com_choice}\n'
        f'Result: {winners}\nComp/Player wins: {com_wins}/{play_wins}\n')

play = input(MESSAGE["ready?"])
player_wins = 0
comp_wins = 0

while 'y' in play:
    player_choice = get_choice()
    comp_choice = get_comp()

    winner = determine_winner(player_choice, comp_choice)
    if "Comp" in winner:
        comp_wins += 1
    elif "Player" in winner:
        player_wins += 1

    print_results(player_choice, comp_choice, winner, comp_wins, player_wins)

    if (comp_wins == 5) or (player_wins == 5):
        print(f'{winner}! Game Over')
        break

    play = input(MESSAGE["again?"])
