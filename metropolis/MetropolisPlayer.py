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
        self.discounts: dict[MetropolisCard, int] = {}
        self.builds_per_turn = 1

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
        # check if card may be played
        if self.may_play_card(card) and self.can_pay_for_card(card):
            # update discounts
            if card not in self.city:
                self.discounts.update(card.extra_info.discounts)
            # update number of cards that may be built per turn
            self.builds_per_turn = max(self.builds_per_turn, card.extra_info.builds_per_turn)
            # add card to city
            self.city.cards.append(card)

    def discard_cards(self, cards: list[MetropolisCard]):
        for card in cards:
            self.hand.remove(card)
            self.game.discard_pile.append(card)

    def may_play_card(self, card: MetropolisCard):
        if self.city.count(card) >= card.extra_info.max_amount:
            return False
        for c2 in card.extra_info.needs:
            if c2 in self.city:
                return True
        return False

    def can_pay_for_card(self, card: MetropolisCard):
        actual_price = self.calculate_card_price(card)
        return actual_price < len(self.hand)

    def calculate_card_price(self, card: MetropolisCard):
        return card.cost - self.discounts[card]
