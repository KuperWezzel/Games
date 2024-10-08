from metropolis.MetropolisCard import MetropolisCard
from metropolis.MetropolisPlayer import MetropolisPlayer
from metropolis.MetropolisSign import MetropolisSign
from metropolis.MetropolisCity import MetropolisCity
from random import shuffle


class MetropolisGame:
    def __init__(self, stack: list[MetropolisCard]):
        self.players: list[MetropolisPlayer] = []
        self.cards = stack
        self.discard_pile: list[MetropolisCard] = []
        shuffle(self.cards)
        self.unique_cards = list(set(stack))
        self.unique_cards.sort(key=lambda x: x.name)
        self.MAX_HAND_CARDS = 12
        self.MAX_SCORE = 50

    def all_cards_in_cities(self):
        cards = []
        for player in self.players:
            cards.extend(player.city)
        return MetropolisCity(cards)

    def other_players(self, player: MetropolisPlayer):
        copy_players = self.players[:]
        copy_players.remove(player)
        return copy_players

    def other_player_with_max_value_sign(self, sign: MetropolisSign, player: MetropolisPlayer):
        other_players = self.other_players(player)

        mx = -1
        mx_player = None
        for player in other_players:
            new_count = player.city.num_sign(sign)
            if new_count > mx:
                mx = new_count
                mx_player = player

        return mx_player

    def add_player(self, player: MetropolisPlayer):
        player.set_game(self)
        self.players.append(player)

    def deal_single_to_player(self, player):
        if not self.cards:
            self.cards = self.discard_pile
            shuffle(self.cards)
            self.discard_pile = []

        player.receive_card(self.cards.pop())

    def deal_n_to_player(self, n, player):
        for _ in range(n):
            self.deal_single_to_player(player)

    def deal_cards_income(self):
        for player in self.players:
            self.deal_n_to_player(player.income(), player)

    def start_game(self):
        for player in self.players:
            self.deal_n_to_player(7, player)

    def has_winner(self):
        return max(player.score for player in self.players) >= self.MAX_SCORE
