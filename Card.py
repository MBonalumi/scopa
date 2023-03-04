import Utils


class Card:
    # seeds: 1.Diamonds, 2.Hearts, 3.Clubs, 4.Spades
    def __init__(self, seed, value):
        self.value = value
        self.seed = seed
        self.sign = Utils.card__val2sign[value]
        self.id = self.sign + self.seed[:1]

    def __eq__(self, other):
        return isinstance(other, Card) and self.value==other.value and self.seed==other.seed

    def debug_print(self):
        print(self.id, '---', self.value, self.sign, '---', self.seed)
