from metropolis.MetropolisDeck import MetropolisDeck
from metropolis.MetropolisPlayer import MetropolisPlayer
from cards import stadsvilla


if __name__ == "__main__":
    deck = MetropolisDeck([stadsvilla, stadsvilla, stadsvilla])
    player = MetropolisPlayer('Wessel', [], deck)
    print(deck.player.name)
    print(deck.income(), deck.points())
