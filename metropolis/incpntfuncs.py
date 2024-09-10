from metropolis.MetropolisDeck import MetropolisDeck
from metropolis.MetropolisSign import MetropolisSign
from metropolis.MetropolisCard import MetropolisCard


def constant(n: int) -> callable(MetropolisDeck):
    def func(deck: MetropolisDeck):
        return n
    return func


def per_sign(sign: MetropolisSign) -> callable(MetropolisDeck):
    def func(deck: MetropolisDeck):
        return deck.num_sign(sign)
    return func


def with_card(n1: int, n2: int, card: MetropolisCard) -> callable(MetropolisDeck):
    def func(deck: MetropolisDeck):
        out = n1
        if card in deck:
            out += n2
        return out
    return func


def stadsvilla_pts(n1: int, n2: int, card: MetropolisCard) -> callable(MetropolisDeck):
    def func(deck: MetropolisDeck):
        return n1 + n2 * (deck.count(card) - 1)
    return func

