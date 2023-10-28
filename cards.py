import random as r
from typing import Union, Tuple, Optional


class Suit:
    def __init__(self, name: str, colour: str = None):
        self.name = name
        self.colour = colour
        self.cards = []

    def __repr__(self):
        return self.name


class Card:
    def __init__(self, suit: Suit, value: Optional[int] = None, valname: str = None,
                 location: Tuple[int, int] = (-1, -1), hidden: bool = True):
        self.suit = suit
        self.value = value
        self.valname = valname
        self.location = location
        self.hidden = hidden
        self.deck = None
        suit.cards.append(self)

    def __repr__(self):
        if self.hidden:
            return "Gesloten kaart"
        elif self.value is None:
            return str(self.suit)
        else:
            return str(self.suit) + " " + self.valname

    def is_top(self) -> bool:
        return self.deck.cards[0] is self

    def is_bottom(self) -> bool:
        return self.deck.cards[-1] is self

    def numOnStack(self) -> int:
        return self.deck.cards.index(self)

    def is_hidden(self) -> bool:
        return self.hidden

    def colour(self) -> str:
        if self.hidden:
            return "grey"
        else:
            return self.suit.colour


class Deck:
    def __init__(self, cards: list[Card] = None, location: Tuple[int, int] = (0, 0)):
        if cards is None:
            cards = []
        self.cards = cards
        self.location = location

    def __repr__(self):
        return str(self.cards)

    def shuffle(self):
        r.shuffle(self.cards)

    def addCard(self, card: Card):
        self.cards.append(card)
        card.deck = self

    def addCards(self, cardList: list[Card]):
        for card in cardList:
            self.addCard(card)

    def removeCard(self, card: Card):
        self.cards.remove(card)
        card.deck = None

    def removeCards(self, cardList: list[Card]):
        for card in cardList:
            self.removeCard(card)

    def moveToSelf(self, cardList: list[Card]):
        other = cardList[0].deck
        other.removeCards(cardList)
        self.addCards(cardList)

    def moveTopToBottom(self, num: int):
        for i in range(num):
            top_card = self.cards.pop(0)
            self.cards.append(top_card)

    def moveBottomToTop(self, num: int):
        for i in range(num):
            bottom_card = [self.cards.pop()]
            bottom_card.extend(self.cards)
            self.cards = bottom_card

    def column(self) -> int:
        return self.location[0]

    def aceRow(self) -> int:
        return self.location[1]

    def copy(self):
        deck = Deck()
        deck.addCards(self.cards)
        deck.location = self.location
        return deck


def fullDeck(num_jokers: int = 0, ace_high: bool = False) -> Deck:
    Jokers = Suit("Joker")
    Harten = Suit("Harten", "red")
    Ruiten = Suit("Ruiten", "red")
    Schoppen = Suit("Schoppen", "black")
    Klaveren = Suit("Klaveren", "black")

    full_deck = Deck()
    names = {1: "Aas", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Boer", 12: "Vrouw", 13: "Heer", 14: "Aas"}
    for i in range(num_jokers):
        full_deck.addCard(Card(Jokers))
    if ace_high:
        min_v, max_v = 2, 14
    else:
        min_v, max_v = 1, 13
    for suit in [Harten, Ruiten, Schoppen, Klaveren]:
        for value in range(min_v, max_v+1):
            full_deck.addCard(Card(suit, value, names[value]))
    return full_deck
