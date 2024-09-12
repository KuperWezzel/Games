from metropolis.MetropolisCard import MetropolisCard
from metropolis.MetropolisSign import MetropolisSign


class MetropolisDeck:
    def __init__(self, cards: list[MetropolisCard]):
        self.cards = cards

    def points(self) -> int:
        return sum(card.points() for card in self.cards)

    def income(self) -> int:
        return sum(card.income() for card in self.cards)

    def num_sign(self, sign: MetropolisSign) -> int:
        return sum(card.num_signs[sign] for card in self.cards)

    def __contains__(self, item):
        return item in self.cards

    def count(self, card: MetropolisCard) -> int:
        return self.cards.count(card)

    def __iter__(self):
        return self.cards

