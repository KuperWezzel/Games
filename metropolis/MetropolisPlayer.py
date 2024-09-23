from metropolis.MetropolisCard import MetropolisCard
from metropolis.MetropolisDeck import MetropolisDeck


class MetropolisPlayer:
    def __init__(self, name: str, hand: list[MetropolisCard], city: MetropolisDeck = None):
        self.name = name
        self.hand = hand

        if city is None:
            self.city = MetropolisDeck([], self)
        else:
            city.player = self
            self.city = city

        self.score: int = 0
        self.game = None

    def points(self):
        pts = self.city.points()
        self.score += pts
        return pts

    def income(self):
        return self.city.income()

    def set_game(self, game):
        self.game = game

    def receive_card(self, card: MetropolisCard):
        self.hand.append(card)

    def play_card(self, card: MetropolisCard):
        self.city.cards.append(card)

    def discard_cards(self, cards: list[MetropolisCard]):
        for card in cards:
            self.hand.remove(card)
            self.game.discard_pile.append(card)
