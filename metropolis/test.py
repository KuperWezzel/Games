from metropolis.MetropolisDeck import MetropolisCity
from metropolis.MetropolisPlayer import MetropolisPlayer
from metropolis.MetropolisCard import MetropolisCard
from cards import stadsvilla, no_signs


if __name__ == "__main__":
    deck = MetropolisCity([stadsvilla, stadsvilla, stadsvilla])
    player = MetropolisPlayer('Wessel', [], deck)
    print(deck.player.name)
    print(deck.income(), deck.points())

    card = MetropolisCard("Fiets", 5, no_signs, 0, 0)
    lijstje = 2 * [card]
    lijstje[0].cost = 55
    print(lijstje[1].cost)
    # print(c.cost for c in lijstje)
