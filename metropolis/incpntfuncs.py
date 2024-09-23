from metropolis.MetropolisPlayer import MetropolisPlayer
from metropolis.MetropolisSign import MetropolisSign
from metropolis.MetropolisCard import MetropolisCard
from metropolis.MetropolisFunc import MetropolisFunc


def constant(n: int) -> callable(MetropolisPlayer):
    def func(player: MetropolisPlayer) -> int:
        return n
    return MetropolisFunc(str(n), func)


def per_sign(n: int, sign: MetropolisSign) -> callable(MetropolisPlayer):
    def func(player: MetropolisPlayer) -> int:
        return n * player.city.num_sign(sign)
    return MetropolisFunc(f"{n}/{sign}", func)


def with_card(n1: int, n2: int, card: MetropolisCard) -> callable(MetropolisPlayer):
    def func(player: MetropolisPlayer) -> int:
        out = n1
        if card in player.city:
            out += n2
        return out
    return MetropolisFunc(f"{n1} +{n2} with {card}", func)


def stadsvilla_pts(n1: int, n2: int, card: MetropolisCard) -> callable(MetropolisPlayer):
    def func(player: MetropolisPlayer) -> int:
        return n1 + n2 * (player.city.count(card) - 1)
    return MetropolisFunc(f"{n1} +{n2} for every other own {card}", func)


def metro_ppr(n1, n2, sign1: MetropolisSign, sign2: MetropolisSign) -> callable(MetropolisPlayer):
    def func(player: MetropolisPlayer) -> int:
        other_pts = player.game.other_player_with_max_value_sign(sign2, player).city.num_sign(sign2)
        return n1 * player.city.num_sign(sign1) + n2 * other_pts
    return MetropolisFunc(f"{n1}/{sign1}\n +{n2}/{sign2} of one other player", func)


def in_game(n1: int, n2: int, card: MetropolisCard) -> callable(MetropolisPlayer):
    def func(player: MetropolisPlayer) -> int:
        out = n1
        if card in player.game.all_cards_in_cities():
            out += n2
        return out
    return MetropolisFunc(f"{n1} +{n2} if {card} in game", func)


def per_card_in_game(n1: int, n2: int, card: MetropolisCard) -> callable(MetropolisPlayer):
    def func(player: MetropolisPlayer) -> int:
        return n1 + n2 * player.game.all_cards_in_cities().count(card)
    return MetropolisFunc(f"{n1} +{n2} per {card} in game", func)
