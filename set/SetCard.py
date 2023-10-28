from enum import Enum


class Colour(Enum):
    RED = 0
    PURPLE = 1
    GREEN = 2


class Shape(Enum):
    OVAL = 0
    RECTANGLE = 1
    WAVE = 2


class Filling(Enum):
    NONE = 0
    FULL = 1
    HALF = 2


class SetCard:
    def __init__(self, colour: Colour, amount: int, shape: Shape, filling: Filling):
        self.colour = colour
        self.amount = amount
        self.shape = shape
        self.filling = filling
        self.location = ('b', 0, 0)
        self.active = False
        self.value = (amount - 1) + 3 * shape.value + 3**2 * filling.value + 3**3 * colour.value
        self.image = f"images/card{self.value}.png"

    def __repr__(self):
        return f"card {self.value}"

    def __str__(self):
        return f"{self.colour.name} {self.amount} {self.shape.name} {self.filling.name}"

    # def all_colours_match(self, card2: "SetCard", card3: "SetCard"):
    #     return self.colour is card2.colour is card3.colour
    #
    # def no_colours_match(self, card2: "SetCard", card3: "SetCard"):
    #     return all([self.colour is not card2.colour,
    #                 self.colour is not card3.colour,
    #                 card2.colour is not card3.colour])

    def is_colour_set(self, card2: "SetCard", card3: "SetCard"):
        return len({self.colour, card2.colour, card3.colour}) != 2

    # def all_amounts_match(self, card2: "SetCard", card3: "SetCard"):
    #     return self.amount is card2.amount is card3.amount
    #
    # def no_amounts_match(self, card2: "SetCard", card3: "SetCard"):
    #     return all([self.amount is not card2.amount,
    #                 self.amount is not card3.amount,
    #                 card2.amount is not card3.amount])

    def is_amount_set(self, card2: "SetCard", card3: "SetCard"):
        return len({self.amount, card2.amount, card3.amount}) != 2

    # def all_shapes_match(self, card2: "SetCard", card3: "SetCard"):
    #     return self.shape is card2.shape is card3.shape
    #
    # def no_shapes_match(self, card2: "SetCard", card3: "SetCard"):
    #     return all([self.shape is not card2.shape,
    #                 self.shape is not card3.shape,
    #                 card2.shape is not card3.shape])

    def is_shape_set(self, card2: "SetCard", card3: "SetCard"):
        return len({self.shape, card2.shape, card3.shape}) != 2

    # def all_fillings_match(self, card2: "SetCard", card3: "SetCard"):
    #     return self.filling is card2.filling is card3.filling
    #
    # def no_fillings_match(self, card2: "SetCard", card3: "SetCard"):
    #     return all([self.filling is not card2.filling,
    #                 self.filling is not card3.filling,
    #                 card2.filling is not card3.filling])

    def is_filling_set(self, card2: "SetCard", card3: "SetCard"):
        return len({self.filling, card2.filling, card3.filling}) != 2

    def is_set(self, card2: "SetCard", card3: "SetCard"):
        return all([self.is_colour_set(card2, card3),
                    self.is_amount_set(card2, card3),
                    self.is_shape_set(card2, card3),
                    self.is_filling_set(card2, card3)])
