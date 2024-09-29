from math import inf, isinf
from helper import text_generator


class MetropolisExtraInfo:
    def __init__(self, txt: str, needs: list = None, max_amount: int = inf, discounts: dict = None, builds_per_turn: int = 1):
        self.txt = txt
        self.needs = needs if needs is not None else []
        self.max_amount = max_amount
        self.discounts = discounts if discounts is not None else {}
        self.reverse_discounts = None
        self.builds_per_turn = builds_per_turn

    def generate_txt(self, corresponding_card):
        new_txt = ""

        if not isinf(self.max_amount):
            new_txt += f"max. {self.max_amount}/speler\n\n"

        if self.needs:
            new_txt += text_generator(self.needs, "Voorwaarde:\n", "\n\n", " of ", " of ")

        if self.discounts:
            self.get_reverse_discounts()
            for discount, cards in self.reverse_discounts.items():
                new_txt += text_generator(cards, f"-{discount} bouwkosten voor ", " en ", " en ", " en ")
            else:
                new_txt = new_txt[:-4] + f" als je ten minste 1 {corresponding_card} hebt\n\n"

        if self.builds_per_turn > 1:
            new_txt += f"Je mag elke ronde {self.builds_per_turn} gebouwen bouwen\n" \
                       f"die elk niet meer dan 4 (vóór kortingen)\n" \
                       f"kosten (inclusief een {self.builds_per_turn}e gebouw\n" \
                       f"in de ronde dat je deze kaart bouwt)"

        self.txt = new_txt
        return new_txt

    def get_reverse_discounts(self):
        if self.reverse_discounts is None:
            self.reverse_discounts = {}
            for card, discount in self.discounts.items():
                if discount not in self.reverse_discounts.keys():
                    self.reverse_discounts[discount] = [card]
                else:
                    self.reverse_discounts[discount].append(card)
        else:
            return self.reverse_discounts


if __name__ == "__main__":
    testinfo = MetropolisExtraInfo("fiets haha", ["fietsers", "Zakencentrum"], 5, {"fiets": 5, "kat": 6, "ik": 5}, 55)
    print(testinfo.txt)
    print("----------------------")
    testinfo.generate_txt("UltraKaart")
    print(testinfo.txt)
