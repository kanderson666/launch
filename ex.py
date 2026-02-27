import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors', 'lizard', 'spock')
    WINS = {
            'rock' : ['scissors', 'lizard'],
            'paper' : ['rock', 'spock'],
            'scissors' : ['paper', 'lizard'],
            'lizard' : ['paper', 'spock'],
            'spock' : ['rock', 'scissors'],
        }
    
    def __init__(self):
        self.move = None
        self.winner = False
        self.score = 0

    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        
        if other.move == self.move:
            return True
        return False

    def __gt__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        
        if other.move in Player.WINS[self.move]:
            return True
        return False
    
    def __lt__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        
        if self.move in Player.WINS[other.move]:
            return True
        return False

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = input('Rock, paper, scissors, lizard, or spock? ').lower()

        while self.move not in Player.CHOICES:
            print('Invalid choice. Pick again\n')
            self.move = input('Rock, paper, scissors, lizard, or spock? ').lower()

class Computer(Player):
    def __init__(self):
        super().__init__()
    def choose(self):
        self.move = random.choice(Player.CHOICES)

class History:
    def __init__(self):
        self.list = []
    def print(self):
        for num, item in enumerate(self.list):
            print(f'{num + 1}. {item}')

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self._history = History()
    
    def play(self):
        self._display_welcome_message()

        while True:
            self._human.choose()
            self._computer.choose()

            self._history.list.append((self._human.move, self._computer.move))

            self._determine_winner()
            self._display_winner()
            self._check_best_of_winner()

            # self._history.print()

            if not self._play_again():
                break

        self._display_goodbye_message()

    def _display_welcome_message(self):
        print('Welcome to RPS')

    def _display_goodbye_message(self):
        print('Goodbye!')
    
    def _determine_winner(self):
        if self._human < self._computer:
            self._computer.winner = True
            self._computer.score += 1
        elif self._human > self._computer:
            self._human.winner = True
            self._human.score += 1

    def _display_winner(self):

        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._computer.winner:
            print('Computer wins!')
        elif self._human.winner:
            print('You win!')
        else:
            print('Its a tie')

        print(f'\nYou won {self._human.score} games')
        print(f'Computer won {self._computer.score} games\n')

    def _play_again(self):
        if input('Play again? [y/n]: ').lower() != 'y':
            return False
        self._human.winner = False
        self._computer.winner = False
        return True
        
    def _check_best_of_winner(self):
        if self._human.score == 2:
            print('You have total victory!')
        elif self._computer.score == 2:
            print('Computer has total victory!')
        else:
            return
        self._human.score = 0
        self._computer.score = 0

# RPSGame()
RPSGame().play()
