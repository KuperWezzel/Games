from math import inf


class MetropolisExtraInfo:
    def __init__(self, txt: str, needs: list = None, max_amount: int = inf, discounts: dict = None, builds_per_turn: int = 1):
        self.txt = txt
        self.needs = needs if needs is not None else []
        self.max_amount = max_amount
        self.discounts = discounts if discounts is not None else {}
        self.builds_per_turn = builds_per_turn
