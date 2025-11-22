import json
import random

CHOICES_DICT = {
    'r' : 'rock',
    'p' : 'paper',
    'sc' : 'scissors',
    'sp' : 'spock',
    'l' : 'lizard'
}

CHOICES_LIST = list(CHOICES_DICT.values())

# Open the JSON file for reading
with open('rps.json', 'r') as file:
    MESSAGE = json.load(file)

def get_choice():
    while True:
        for key, value in CHOICES_DICT.items():
            print(f'{value} [{key}]')
            
        key = input(f'{", ".join(CHOICES_LIST)}? ').casefold().strip()
        try:
            weapon = CHOICES_DICT[key]
        except KeyError:
            print(MESSAGE['error'])
        else:
            return weapon

def get_comp():
    #randomly pick one of the 5 options
    choice = random.choice(CHOICES_LIST)
    return choice

def get_index(choice):
    #return index of chosen weapon in list of weapons
    for i, weapon in enumerate(CHOICES_LIST):
        if choice in weapon:
            return i
    return -1

def determine_winner(play_choice, com_choice):
    if play_choice == com_choice:
        return "Tie"

    play_index = get_index(play_choice)
    com_index = get_index(com_choice)

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
