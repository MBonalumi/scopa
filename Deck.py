from Card import Card
import Utils


class Deck:
    # num should be 40, maybe 52 or 108, but i'm using 40

    def __init__(self):
        self.deck = []
        self.initiate_deck()

    def initiate_deck(self):
        for seed in Utils.SEEDS:
            for value in range(Utils.CARDS_PER_SEED):
                self.deck.append(Card(value, seed))

    def get_card_by_position(self, position):
        return self.deck[position]

    def print_deck(self):
        ids = [card.id for card in self.deck]
        print(ids)

    def debug_print(self):
        for card in self.deck:
            card.debugPrint()


def get_card_by_id(id):
    value, seed = Utils.card__id2value_seed(id)
    seed_position = Utils.seed__ordering(seed)
    return Deck.get_card_by_position(seed_position * 10 + value - 1)
