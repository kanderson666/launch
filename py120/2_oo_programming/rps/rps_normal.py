import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors')
    def __init__(self):
        self.move = None

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = input('Rock, paper, or scissors? ').lower()

        while self.move not in Player.CHOICES:
            print('Invalid choice. Pick again\n')
            self.move = input('Rock, paper, or scissors? ').lower()

class Computer(Player):
    def __init__(self):
        super().__init__()
    def choose(self):
        self.move = random.choice(Player.CHOICES)

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()
    def play(self):
        self._display_welcome_message()

        while True:
            self._human.choose()
            self._computer.choose()

            self._display_winner()
            if not self._play_again():
                break

        self._display_goodbye_message()

    def _display_welcome_message(self):
        print('Welcome to RPS')
    def _display_goodbye_message(self):
        print('Goodbye!')

    def _display_winner(self):
        WINS = {
            'rock' : 'scissors',
            'paper' : 'rock',
            'scissors' : 'paper'
        }
        human_move = self._human.move
        computer_move = self._computer.move

        print(f'You chose: {human_move}')
        print(f'The computer chose: {computer_move}')

        if human_move == computer_move:
            print('Its a tie')
        elif WINS[human_move] == computer_move:
            print('You win!')
        else:
            print('Computer wins!')

    def _play_again(self):
        answer = input('Play again? [y/n]: ').lower()
        return answer == 'y'

# RPSGame()
RPSGame().play()
