from enum import Enum


class MetropolisSign(Enum):
    SOURCE = 0
    SHOP = 1
    CAR = 2


def signs(src: int, shop: int, car: int) -> dict[MetropolisSign, int]:
    return {MetropolisSign.SOURCE: src, MetropolisSign.SHOP: shop, MetropolisSign.CAR: car}
