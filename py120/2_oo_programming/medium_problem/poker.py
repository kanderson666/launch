import random

class Card:
    RANKS = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
    SUITS = {'Diamond' : 0, 'Club' : 1, 'Heart' : 2, 'Spade' : 3}


    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    @property
    def convert_rank(self):
        return Card.RANKS.get(self.rank, self.rank)
    @property
    def convert_suit(self):
        return Card.SUITS.get(self.suit, self.suit)

    def __lt__(self, other):
        if self.convert_rank == other.convert_rank:
            return self.convert_suit < other.convert_suit
        return self.convert_rank < other.convert_rank

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    def __init__(self):
        self._shuffle()

    def _shuffle(self):
        self._deck = [Card(rank, suit) for suit in self.SUITS for rank in self.RANKS]
        random.shuffle(self._deck)
        # [print(card) for card in self._deck]

    def draw(self):
        if not self._deck:
            self._shuffle()
        return self._deck.pop()

# Include Card and Deck classes from the last two exercises.

class PokerHand:
    def __init__(self, deck):
        self.hand = [deck.draw() for _ in range(5)]
        self.hand.sort(key=self._sorting, reverse=True)
        self.count_cards()

    def _sorting(self, card):
        return card.convert_rank

    def count_cards(self):
        count_dict = {}
        for card in self.hand:
            rank = card.convert_rank
            count_dict[rank] = count_dict.get(rank, 0) + 1
        self.count = sorted(count_dict.values(), reverse=True)

    def print(self):
        for card in self.hand:
            print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"


    def _is_royal_flush(self):
        if sum([card.convert_rank for card in self.hand]) == 60 and self._is_flush():
            return True
        return False

    def _is_straight_flush(self):
        if self._is_straight() and self._is_flush():
            return True
        return False

    def _is_four_of_a_kind(self):
        return self.count[0] == 4

    def _is_full_house(self):
        return self.count[0] == 3 and self.count[1] == 2

    def _is_flush(self):
        suit = self.hand[0].suit
        if all([card.suit == suit for card in self.hand]):
            return True

    def _is_straight(self):
        last_rank = self.hand[0].convert_rank 
        for card in self.hand[1:]:
            if last_rank - card.convert_rank != 1:
                return False
            last_rank = card.convert_rank
        return True

    def _is_three_of_a_kind(self):
        return self.count[0] == 3

    def _is_two_pair(self):
        return self.count[0] == 2 and self.count[1] == 2

    def _is_pair(self):
        return self.count[0] == 2
    


hand = PokerHand(Deck())

hand.print()
print(hand.evaluate(), '\n')

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")  # @

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")  # @

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")
