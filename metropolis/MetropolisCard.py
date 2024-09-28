from metropolis.MetropolisSign import MetropolisSign
from metropolis.MetropolisFunc import MetropolisFunc
from metropolis.MetropolisExtraInfo import MetropolisExtraInfo
import PySimpleGUI as sg


class MetropolisCard:
    def __init__(self, name: str, cost: int, num_signs: dict[MetropolisSign, int], income: MetropolisFunc, points: MetropolisFunc, extra_info: MetropolisExtraInfo = None):
        self.name = name
        self.cost = cost
        self.total_signs = sum(num_signs.values())
        self.num_signs = num_signs
        self.extra_info = extra_info if extra_info is not None else MetropolisExtraInfo("")
        self.income = income
        self.points = points

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def layout(self):
        symbols = ""
        if self.total_signs > 0:
            spaces = 5
            for sgn, amount in self.num_signs.items():
                for _ in range(amount):
                    symbols += f"{sgn.value}" + spaces * " "
            else:
                symbols = symbols[:-spaces]
        return [[sg.Frame("", [[sg.Push(), sg.T(str(self.cost) + "  " + self.name + "  " + str(self.cost)), sg.Push()],
                               [sg.Push(), sg.T(symbols), sg.Push()],
                               [sg.Push(), sg.T(self.extra_info.txt), sg.Push()],
                               [sg.T("$" + self.income.display)],
                               [sg.T("*" + self.points.display)]]
                          )]]
