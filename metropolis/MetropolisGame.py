from metropolis.MetropolisCard import MetropolisCard
from metropolis.MetropolisPlayer import MetropolisPlayer
from metropolis.MetropolisSign import MetropolisSign


class MetropolisGame:
    def __init__(self, players: list["MetropolisPlayer"], stack: list[MetropolisCard]):
        self.players = players
        self.cards = stack

    def all_cards_in_cities(self):
        cards = []
        for player in self.players:
            cards.extend(player.city)

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
