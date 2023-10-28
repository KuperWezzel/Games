from SetCard import *
import random as r


def make_full_deck() -> list[SetCard]:
    return [SetCard(col, am, sh, fill) for col in Colour for am in range(1, 4) for sh in Shape for fill in Filling]


def make_shuffled_deck() -> list[SetCard]:
    deck = make_full_deck()
    r.shuffle(deck)
    return deck


def update(window, card: SetCard, i: int = None, j: int = None, location: tuple = None):
    if i is not None and j is not None:
        location = ("b", i, j)



if __name__ == "__main__":
    deck = sorted(make_full_deck(), key=lambda c: c.value)
    for card in deck:
        print(card.value, str(card))
