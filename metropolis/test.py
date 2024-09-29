from metropolis.MetropolisCity import MetropolisCity
from metropolis.MetropolisPlayer import MetropolisPlayer
from metropolis.MetropolisCard import MetropolisCard
from cards import stadsvilla, no_signs
from copy import copy

if __name__ == "__main__":
    deck = MetropolisCity([stadsvilla, stadsvilla, stadsvilla])
    player = MetropolisPlayer('Wessel', [], deck)
    print(deck.player.name)
    print(deck.income(), deck.points())

    card = MetropolisCard("Fiets", 5, no_signs, 0, 0)
    lijstje = [copy(card), copy(card)]
    lijstje[0].cost = 55
    print(card.cost, lijstje[0].cost, lijstje[1].cost)
    # print(c.cost for c in lijstje)
