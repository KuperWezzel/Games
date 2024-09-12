from metropolis.MetropolisCard import MetropolisCard
from metropolis.MetropolisDeck import MetropolisDeck


class MetropolisPlayer:
    def __init__(self, hand: list[MetropolisCard], city: MetropolisDeck):
        self.hand = hand
        self.city = city
        self.score: int = 0

    def points(self):
        pts = self.city.points()
        self.score += pts
        return pts

    def income(self):
        return self.city.income()
