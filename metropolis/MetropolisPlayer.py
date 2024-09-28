from metropolis.MetropolisCard import MetropolisCard
from metropolis.MetropolisDeck import MetropolisCity


class MetropolisPlayer:
    def __init__(self, name: str, hand: list[MetropolisCard], city: MetropolisCity = None):
        self.name = name
        self.hand = hand

        if city is None:
            self.city = MetropolisCity([], self)
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

    def play_cards(self, cards: list[MetropolisCard]):
        # check if cards may be played
        if self.may_play_cards(cards) and self.can_pay_for_cards(cards):
            for card in cards:
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

    def may_play_cards(self, cards: list[MetropolisCard]):
        return len(cards) <= self.builds_per_turn and all(self.may_play_card(card) for card in cards)

    def can_pay_for_cards(self, cards: list[MetropolisCard]):
        actual_price = 0
        for card in cards:
            actual_price += self.calculate_card_price(card)
        return actual_price + len(cards) <= len(self.hand)

    def calculate_card_price(self, card: MetropolisCard):
        return max(0, card.cost - self.discounts[card])
