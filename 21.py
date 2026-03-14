import random
import os

def clear_screen():
    os.system('clear')

class Card:
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit

    def __str__(self):
        return f'{self.num}, {self.suit}'

class Deck:
    SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs',]
    FACE_RANKS = ['Jack', 'Queen', 'King']
    RANKS = [num for num in range(2, 11)] + FACE_RANKS + ['Ace']
    
    def __init__(self):
        self.deck = self.new_shuffled_deck()
        
    def new_shuffled_deck(self):
        deck = [Card(num, suit) for suit in Deck.SUITS for num in Deck.RANKS]
        random.shuffle(deck)
        return deck

    def hit(self):
        return self.deck.pop()

    def __str__(self):
        result = []
        for card in self.deck:
            result.append(str(card))
        return str(result)

class Participant:
    def __init__(self):
        self.reset()

    def reset(self):
        self.score = 0
        self.hand = []
        
    def hit(self, deck):
        self.hand.append(deck.hit())

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score

    def is_busted(self):
        return self.score > TwentyOneGame.MAX

    def display_hand(self, hide_dealer=False):
        hand = ''
        for card in self.hand:
            if self.name == 'Dealer' and hide_dealer:
                hand += '[?] '
                hide_dealer = False
                continue

            hand += f'[{card.num}] '
        print(f'{self.name}: {self.score} {hand}')

class Human(Participant):
    def __init__(self):
        super().__init__()
        self.name = 'Human'
        self.money = 5

class Dealer(Participant):
    def __init__(self):
        super().__init__()
        self.name = 'Dealer'

class TwentyOneGame:
    MAX = 21

    def __init__(self):
        self.deck = Deck()
        self.human = Human()
        self.dealer = Dealer()
        self.hide_dealer = True

    def start(self):
        self.display_welcome_message()
        while True:
            self.deal_cards()
            self.sum_hands()
            self.show_cards('Fresh deal')

            self.human_turn()
            self.dealer_turn()

            self.display_result()
            
            if not self.play_again():
                break
            
            self.reset()

        self.display_goodbye_message()

    def play_again(self):
        if self.human.money == 0 or self.human.money == 10:
            return False
        
        if self.get_user_input('Play again?', ['y', 'n']) == 'n':
            return False
        return True

    def reset(self):
        self.human.reset()
        self.dealer.reset()
        self.deck = Deck()
        self.hide_dealer = True

    def deal_cards(self):
        self.human.hit(self.deck)
        self.human.hit(self.deck)
        self.dealer.hit(self.deck)
        self.dealer.hit(self.deck)

    def show_cards(self, message):
        clear_screen()
        print(message)
        self.human.display_hand()
        self.dealer.display_hand(self.hide_dealer)

    def sum_hands(self):
        self.sum_hand(self.human)
        self.sum_hand(self.dealer)

    def sum_hand(self, player):
        hide_first = True if self.hide_dealer else False
        total = 0
        aces = 0
        for card in player.hand:
            # skip totaling 1st card if want to hide dealer's 1st card
            if player.name == 'Dealer' and hide_first:
                hide_first = False
                continue

            elif card.num in Deck.FACE_RANKS:
                total += 10

            elif card.num == 'Ace':
                aces += 1

            else:
                total += int(card.num)

        total = self.compute_aces(total, aces)
        player.score = total
        
    def compute_aces(self, total, num_aces):
        num_ones = 0
        total += num_aces * 11

        while total > TwentyOneGame.MAX and num_ones != num_aces:
            num_ones += 1
            total -= 10
        return total

    def human_turn(self):
        hide_dealer = True
        self.sum_hands()

        while True:
            if self.get_user_input('Hit or stay?', ['h', 's']) == 's':
                break
            self.human.hit(self.deck)
            self.sum_hands()
            self.show_cards('Human hits')
            if self.human.is_busted():
                break
        
    def get_user_input(self, question, options):
        user_input = input(f'\n{question} [{'/'.join(options)}] ')

        while user_input not in options:
            print('Invalid input.')
            user_input = input(f'\n{question} [{'/'.join(options)}] ')
        return user_input

    def dealer_turn(self):
        self.hide_dealer = False
        self.sum_hands()

        if self.human.is_busted():
            return

        self.show_cards('Human stays. Dealer reveals:')
        input('\nPress enter to continue')

        while self.dealer.score < 17 and not self.dealer.is_busted():
            self.dealer.hit(self.deck)
            self.sum_hands()
            self.show_cards('Dealer hits')
            input('\nPress enter to continue')

        if self.dealer.is_busted():
            return

        self.show_cards('Dealer stays')
        input('\nPress enter to continue')

    def display_welcome_message(self):
        print('Welcome to 21')
        input('Press enter to continue')

    def display_goodbye_message(self):
        print('\nThanks for playing 21')

    def display_result(self):
        if self.human.is_busted():
            message = 'Human busts!'
            self.human.money -= 1

        elif self.dealer.is_busted():
            message = 'Dealer busts!'
            self.human.money += 1
            
        elif self.dealer.score > self.human.score:
            message = 'Dealer wins!'
            self.human.money -= 1
            
        elif self.dealer.score < self.human.score:
            message = 'Human wins!'
            self.human.money += 1
        
        else:
            message = 'Tie!'

        self.show_cards(message)
        print(f'Human has ${self.human.money}')

game = TwentyOneGame()
game.start()
