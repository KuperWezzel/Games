from metropolis.MetropolisSign import MetropolisSign


class MetropolisCard:
    def __init__(self, name: str, cost: int, num_signs: dict[MetropolisSign, int], income: callable("MetropolisDeck"), points: callable("MetropolisDeck")):
        self.name = name
        self.cost = cost
        self.total_signs = sum(num_signs.values())
        self.num_signs = num_signs
        self.income = income
        self.points = points

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name
