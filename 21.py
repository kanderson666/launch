import random
from os import system
FACES = 'JQKA'
JQK_VALUE = 10
NUM_SUITS = 4

DECK = 0
DEALER = 1
DEALER_HIDDEN = 2
PLAYER = 3

HAND_SUM = 0
FIRST_CARD = 1
LIMIT = 21
DEALER_LIMIT = LIMIT - 4

YES_NO = 'yesno'
FIRST_TO = 3

def play():
    cards = initialize_game()
    display_hands(cards, DEALER_HIDDEN)

    player_turn(cards)
    if bust(cards, PLAYER):
        display_hands(cards, DEALER)
        print("\nPlayer bust! Dealer wins")
        return DEALER

    comp_turn(cards)
    if bust(cards, DEALER):
        display_hands(cards, DEALER)
        print("\nDealer bust! Player wins")
        return PLAYER

    return determine_winner(cards)

def initialize_game():
    cards = [[], [0], [0], [0]]
    cards[DECK] = fresh_deck()

    deal(cards)

    count_cards(cards, DEALER)
    count_cards(cards, DEALER_HIDDEN)
    count_cards(cards, PLAYER)

    return cards

def fresh_deck():
    deck = [str(num) for num in range(2, 11)] * NUM_SUITS + list(FACES) * NUM_SUITS
    random.shuffle(deck)
    return deck

def deal(cards):
    hit(cards, PLAYER)
    hit(cards, DEALER)
    hit(cards, PLAYER)
    hit(cards, DEALER)

    cards[DEALER_HIDDEN] = [0, cards[DEALER][FIRST_CARD], '?']

def hit(cards, player):
    cards[player].append(cards[DECK].pop())

def count_cards(cards, player):
    total = 0
    num_aces = 0
    for card in cards[player][FIRST_CARD:]:
        if card == '?':
            break
        if card not in FACES:
            total += int(card)
        elif card == 'A':
            num_aces += 1
        else:
            total += JQK_VALUE
    total = convert_aces(total, num_aces)
    cards[player][HAND_SUM] = total

def convert_aces(total, num_aces):
    highest_value = 11 * num_aces  # if 1 ace, max value 11. If 2 aces, max value 22, etc

    # repeat checks until all aces are of value 1
    while highest_value > num_aces:
        if total + highest_value <= LIMIT:
            break
        highest_value -= 10     # change 1 ace to value of 1
    return total + highest_value

def player_turn(cards):
    while not bust(cards, PLAYER):
        response = yes_or_no("\nHit? [y/n]: ")
        if response[0] == 'n':
            break

        hit(cards, PLAYER)
        count_cards(cards, PLAYER)
        display_hands(cards, DEALER_HIDDEN)

def comp_turn(cards):
    display_hands(cards, DEALER)
    input("Press Enter to continue ")

    while cards[DEALER][HAND_SUM] < DEALER_LIMIT:
        hit(cards, DEALER)
        count_cards(cards, DEALER)
        display_hands(cards, DEALER)
        input("Press Enter to continue ")

def bust(cards, player):
    return cards[player][HAND_SUM] > LIMIT

def yes_or_no(question):
    while True:
        response = input(question).casefold().strip()
        if response == '':
            pass
        elif response in YES_NO and (response[0] == 'y' or response[0] == 'n'):
            return response

        print("Please enter valid response.")

def display_hands(cards, dealer):
    system("clear")
    print("Dealer:")
    print(f"[{']['.join(cards[dealer][FIRST_CARD:]).rstrip('[')}] Total: {cards[dealer][HAND_SUM]}")
    print("\nPlayer:")
    print(f"[{']['.join(cards[PLAYER][FIRST_CARD:]).rstrip('[')}] Total: {cards[PLAYER][HAND_SUM]}")

def determine_winner(cards):
    display_hands(cards, DEALER)

    if cards[PLAYER][HAND_SUM] > cards[DEALER][HAND_SUM]:
        print("\nPlayer wins!")
        return PLAYER

    if cards[PLAYER][HAND_SUM] < cards[DEALER][HAND_SUM]:
        print("\nDealer wins!")
        return DEALER

    print("\nTie!")
    return None

def display_wins(wins):
    print(f'Player wins: {wins[PLAYER]}\tDealer wins: {wins[DEALER]}\n')

def check_match_win(wins):
    if wins[PLAYER] == FIRST_TO:
        print('Player wins the match!')
        wins[PLAYER] = 0
        wins[DEALER] = 0

    elif wins[DEALER] == FIRST_TO:
        print('Dealer wins the match!')
        wins[PLAYER] = 0
        wins[DEALER] = 0

wins = {PLAYER : 0,
        DEALER : 0,
        None : 0,
}

while True:
    winner = play()

    wins[winner] += 1
    display_wins(wins)
    check_match_win(wins)

    response = yes_or_no("Play again? [y/n]: ")
    if response[0] == 'n':
        break

print("Goodbye!")
