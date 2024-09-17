from metropolis.MetropolisPlayer import MetropolisPlayer
from metropolis.MetropolisSign import MetropolisSign
from metropolis.MetropolisCard import MetropolisCard


def constant(n: int) -> callable(MetropolisPlayer):
    def func(player: MetropolisPlayer) -> int:
        return n
    return func


def per_sign(sign: MetropolisSign) -> callable(MetropolisPlayer):
    def func(player: MetropolisPlayer) -> int:
        return player.city.num_sign(sign)
    return func


def with_card(n1: int, n2: int, card: MetropolisCard) -> callable(MetropolisPlayer):
    def func(player: MetropolisPlayer) -> int:
        out = n1
        if card in player.city:
            out += n2
        return out
    return func


def stadsvilla_pts(n1: int, n2: int, card: MetropolisCard) -> callable(MetropolisPlayer):
    def func(player: MetropolisPlayer) -> int:
        return n1 + n2 * (player.city.count(card) - 1)
    return func


def metro_ppr(sign: MetropolisSign) -> callable(MetropolisPlayer):
    def func(player: MetropolisPlayer) -> int:
        other_pts = player.game.other_player_with_max_value_sign(sign, player).city.num_sign(sign)
        return player.city.num_sign(sign) + other_pts
    return func


def in_game(n1: int, n2: int, card: MetropolisCard) -> callable(MetropolisPlayer):
    def func(player: MetropolisPlayer) -> int:
        out = n1
        if card in player.game.all_cards_in_cities():
            out += n2
        return out
    return func


def per_card_in_game(n1: int, n2: int, card: MetropolisCard) -> callable(MetropolisPlayer):
    def func(player: MetropolisPlayer) -> int:
        return n1 + n2 * player.game.all_cards_in_cities().count(card)
    return func
