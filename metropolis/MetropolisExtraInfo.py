from math import inf


class MetropolisExtraInfo:
    def __init__(self, txt: str, needs: list = None, max_amount: int = inf, discounts: dict = None):
        self.txt = txt
        self.needs = needs if needs is not None else []
        self.max_amount = max_amount
        self.discounts = discounts if discounts is not None else {}
