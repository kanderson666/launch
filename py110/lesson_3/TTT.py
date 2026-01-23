"""
1. Display the initial empty 3x3 board.
2. Ask the user to mark a square.
3.      Display the updated board state.
4.      If it's a winning board, display the winner.
5.      If the board is full, display tie.
6. Computer marks a square.
7.      Display the updated board state.
8.      If it's a winning board, display the winner.
9.      If the board is full, display tie.
10. If neither player won and the board is not full, go to #2
11. Play again?
12. If yes, go to #1
13. Goodbye!

  X | O | X  
----+---+---- 
  X | O | X
----+---+----
    | X |
"""
from random import randint
from os import system
HORIZONTAL = '----+---+----'
INDEX_OFFSET = 1
PLAYERS = ["X", "O"]
WINNING_COMBOS = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
    [1, 5, 9], [3, 5, 7]              # diagonals
]

def play():
    play_again = True
    while play_again == True:
        board = initialize_board()
        display_board(board)

        winner = False
        while winner == False:
            for player in PLAYERS:
                get_player_move(board, player)
                display_board(board)
                if check_board(board, player):
                    winner = True
                    break
        if input("Play again? [y/n]: ") != 'y':
            play_again = False

def initialize_board():
    # return [[' ', ' ', ' '],
    #         [' ', ' ', ' '],
    #         [' ', ' ', ' '],
    #         ]
    return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
    system('clear')
    num_horizontal = 0
    for row in board:
        print(f'  {row[0]} | {row[1]} | {row[2]}')
        if num_horizontal < 2:
            print(HORIZONTAL)
            num_horizontal += 1

def get_player_move(board, player):
    while True:
        if player == "X":
            player_choice = input("Where you play? (1-9): ")
            player_choice = int(player_choice) - INDEX_OFFSET  
        # computer player
        else:
            player_choice = randint(0, 8)  

        if move_is_valid(board, player_choice):
            row, column = get_idx(player_choice)
            board[row][column] = player
            break
        elif player == "X":
            print("Board space occupied, pick again.")

def move_is_valid(board, player_choice):
    row, column = get_idx(player_choice)
    return board[row][column] == " "

def get_idx(position):
    row = position // 3
    column = position - (3 * row)
    return (row, column)

def check_board(board, player):
    def check_for_winner(board, player):
        for winning_combo in WINNING_COMBOS:
            num_matches = 0
            for position in winning_combo:
                row, column = get_idx(position)
                if board[row][column] != player:
                    break
            
                num_matches += 1
                if num_matches == 3:
                    return True
        return False

    def board_full(board):
        for row in board:
            if " " in row:
                return False
        return True
    
    if check_for_winner(board, player):
        print(f"Player {player} wins")
        return True
    
    elif board_full(board):
        print("Tie")
        return True
    return False
    
play()
print("Goodbye!")
