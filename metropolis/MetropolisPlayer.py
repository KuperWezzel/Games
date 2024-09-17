from metropolis.MetropolisCard import MetropolisCard
from metropolis.MetropolisDeck import MetropolisDeck
from metropolis.MetropolisGame import MetropolisGame


class MetropolisPlayer:
    def __init__(self, hand: list[MetropolisCard], city: MetropolisDeck):
        self.hand = hand
        self.city = city
        self.score: int = 0
        self.game = None

    def points(self):
        pts = self.city.points()
        self.score += pts
        return pts

    def income(self):
        return self.city.income()

    def set_game(self, game: MetropolisGame):
        self.game = game

    def receive_card(self, card: MetropolisCard):
        self.hand.append(card)
