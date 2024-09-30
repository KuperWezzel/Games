from metropolis.MetropolisCard import MetropolisCard
from metropolis.MetropolisCity import MetropolisCity
from helper import text_generator as tg


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

    def city_points(self):
        return self.city.points()

    def update_score(self):
        self.score += self.city_points()
        return self.score

    def income(self):
        return self.city.income()

    def set_game(self, game):
        self.game = game

    def receive_card(self, card: MetropolisCard):
        self.hand.append(card)

    def play_cards(self, cards: list[MetropolisCard]):
        for card in cards:
            # update discounts
            if card not in self.city:
                self.discounts.update(card.extra_info.discounts)
            # update number of cards that may be built per turn
            self.builds_per_turn = max(self.builds_per_turn, card.extra_info.builds_per_turn)
            # add card to city
            self.city.cards.append(card)
            # remove card from hand
            if card.name != "Architect":
                self.hand.remove(card)
            print([card.name for card in self.hand])

    def discard_cards(self, cards: list[MetropolisCard]):
        for card in cards:
            self.hand.remove(card)
            self.game.discard_pile.append(card)

    def may_play_card(self, card: MetropolisCard):
        if card not in self.hand and card.name != "Architect":
            print(f'may not play {card} because it is not in hand')
            return False
        if self.city.count(card) >= card.extra_info.max_amount:
            print(f'may not play {card} because we already have the max amount of this card')
            return False
        if card.extra_info.needs:
            for c2 in card.extra_info.needs:
                if c2 in self.city:
                    return True
            print(tg(card.extra_info.needs, f'may not play {card} because we dont have ', '', final_sep=' or '))
            return False
        else:
            # we have no necessary cards, so return True
            return True

    def may_play_cards(self, cards: list[MetropolisCard]):
        if not self.can_pay_for_cards(cards):
            print('cards are too expensive')
            return False
        if len(cards) > max([card.extra_info.builds_per_turn for card in cards] + [self.builds_per_turn]):
            print('playing too many cards')
            return False
        for card in cards:
            if not self.may_play_card(card):
                return False
        return True

    def can_pay_for_cards(self, cards: list[MetropolisCard]):
        actual_price = 0
        for card in cards:
            if card.name == "Architect":
                actual_price -= 1  # offset for Architect not being in your hand
            actual_price += self.calculate_card_price(card)
        return actual_price + len(cards) <= len(self.hand)

    def calculate_card_price(self, card: MetropolisCard):
        return max(0, card.cost - self.discounts.get(card, 0))

    def calculate_total_card_price(self, cards: list[MetropolisCard]):
        return sum(self.calculate_card_price(card) for card in cards)

    def has_too_many_cards(self):
        return len(self.hand) > self.game.MAX_HAND_CARDS
