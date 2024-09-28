from enum import Enum


class MetropolisSign(Enum):
    SOURCE = "\U000026F2"
    SHOP = "\U0001F6D2"
    CAR = "\U0001F697"


def signs(src: int, shop: int, car: int) -> dict[MetropolisSign, int]:
    return {MetropolisSign.SOURCE: src, MetropolisSign.SHOP: shop, MetropolisSign.CAR: car}
