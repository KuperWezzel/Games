from metropolis.MetropolisCard import MetropolisCard
from metropolis.MetropolisDeck import MetropolisDeck
from metropolis.MetropolisSign import MetropolisSign


if __name__ == "__main__":
    no_signs = {MetropolisSign.SOURCE: 0, MetropolisSign.CAR: 0, MetropolisSign.SHOP: 0}
    c1 = MetropolisCard("Woonhuis", 1, no_signs, 1, 0)
    c2 = MetropolisCard("Woonhuis", 1, no_signs, 1, 0)
    deck = MetropolisDeck([c1])
    print(c2 in deck)
