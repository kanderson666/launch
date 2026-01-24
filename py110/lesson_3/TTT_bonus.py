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
import random
from os import system

WHO_FIRST = 'human'    # human, comp, choose
YES_NO = 'yesno'
PLAYERS = ["X", "O"]
HORIZONTAL = '----+---+----'
CHOICES = '123456789'
INDEX_OFFSET = 1
MIDDLE_SQUARE = 5
# WINNING_COMBOS = [
#     [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
#     [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
#     [0, 4, 8], [2, 4, 6]              # diagonals
# ]
WINNING_COMBOS = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
    [1, 5, 9], [3, 5, 7]              # diagonals
]
MATCH = 3

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
        
        response = yes_or_no("Play again? [y/n]: ")
        if response[0] == 'n':
            play_again = False

def yes_or_no(question):
    while True:
        response = input(question)
        if response.casefold() in YES_NO:
            return response.casefold()
        print("Please enter valid response.")

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
    moves = valid_moves(board)
    while True:
        if player == "X":
            while True:
                player_choice = input(f"Where you play? ({join_or(moves)}): ")
                if player_choice in [str(move) for move in moves]:
                    break
                print("Invalid choice, pick again")
            player_choice = int(player_choice) 
        # computer player
        else:
            player_choice = get_comp_move(board, player)

        row, column = get_idx(player_choice)
        board[row][column] = player
        break

def valid_moves(board):
    moves = []
    for position in range(9):
        row, column = get_idx(position + INDEX_OFFSET)
        if board[row][column] == " ":
            moves.append(position + INDEX_OFFSET)
    return moves

def get_idx(position):
    position -= INDEX_OFFSET
    row = position // 3
    column = position - (3 * row)
    return (row, column)

def join_or(lst, delim=', ', word="or"):
    # [1, 2, 3]
    # 1, 2, and 3
    lst = [str(item) for item in lst]
    if len(lst) < 2:
        return "".join(lst)
    if len(lst) == 2:
        return f"{lst[0]} {word} {lst[1]}"
    fixed = delim.join(lst[:-1])
    return f'{fixed}{delim}{word} {lst[-1]}'

def get_comp_move(board, player):
    moves = valid_moves(board)
    if MIDDLE_SQUARE in moves:
        return MIDDLE_SQUARE
    
    # offensive move
    move = tactical_move(board, player)
    if move:
        return move
    
    # defensive move
    if player == 'X':
        move = tactical_move(board, 'O')
    else:
        move = tactical_move(board, 'X')
    if move:
        return move

    return random.choice(moves)

def tactical_move(board, player):
    moves = valid_moves(board)
    for move in moves:
        row, column = get_idx(move)
        board[row][column] = player
        if check_for_winner(board, player):
            board[row][column] = " "
            return move
        else:
            board[row][column] = " "
    return None

def check_board(board, player):
    if check_for_winner(board, player):
        track_wins(player)
        return True
    
    elif board_full(board):
        print("Tie")
        return True
    return False

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

def track_wins(player, wins={'X':0, 'O':0}):
        wins[player] += 1
        if wins[player] == MATCH:
            print(f'{player} wins the match! Final score:')
            print(f'X: {wins['X']}, O: {wins['O']}')
            wins['X'] = 0
            wins['O'] = 0
        else:
            print(f'{player} wins! Total score:')
            print(f'X: {wins['X']}, O: {wins['O']}')

match WHO_FIRST:
    case 'comp':
        PLAYERS = ["O", "X"]
    case 'choose':
        response = yes_or_no("Player goes first? [y/n]: ")
        if response[0] == 'n':
            PLAYERS = ["O", "X"]
    case 'human' | _:
        pass

play()
print("Goodbye!")
