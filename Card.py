import Utils


class Card:
    # seeds: 1.Diamonds, 2.Hearts, 3.Clubs, 4.Spades
    def __init__(self, value, seed):
        self.value = value
        self.seed = seed
        self.sign = Utils.card__val2sign(value)
        self.id = self.seed[:1] + self.sign

    def debug_print(self):
        print(self.id, '---', self.value, self.sign, '---', self.seed)
