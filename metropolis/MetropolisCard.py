from metropolis.MetropolisSign import MetropolisSign
from metropolis.MetropolisFunc import MetropolisFunc
import PySimpleGUI as sg


class MetropolisCard:
    def __init__(self, name: str, cost: int, num_signs: dict[MetropolisSign, int], income: MetropolisFunc, points: MetropolisFunc):
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

    def __str__(self):
        return self.name

    def layout(self):
        return [[sg.Column([[sg.T(self.name)],
                           [sg.T("cost: " + str(self.cost))],
                           [sg.T("$ " + self.income.display)],
                           [sg.T("* " + self.points.display)]]
                           )]]
