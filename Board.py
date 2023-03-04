class Board:

    def __init__(self):
        self.cards = []

    def available_takes_and_type(self, card):
        # (a) thrown card is an Ace
        if card.sign == 'A': return [self.cards.copy()], 2

        # if no cards just throw --> avoids problems when cycling through cards, but ace take has priority
        if len(self.cards) == 0: return [], 0

        # (b) if same value card
        takes = []
        for c in self.cards:
            if c.value == card.value:
                takes.append([c])
        if len(takes)>0: return takes, 1

        # (c) cards_to_take are in self.cards & they sum to thrown card
        cards_for_sums = sorted(
            [c for c in self.cards if c.value < card.value],
            key=lambda x: -x.value)
        sums = self.calculate_sum_takes(card.value, cards_for_sums)
        if len(sums) > 0: return sums, 3

        return [], 0

    # TODO: this function should be rewritten
    def calculate_sum_takes(self, value, cards, sums=None):
        if sums is None:
            sums = []
        if value == 0: return sums
        if len(cards) == 0: return sums
        # useful_cards = [c for c in cards if c.value <= value]
        # if len(useful_cards) == 0: return sums

        for card in cards:
            partial_value = value - card.value
            if partial_value < 0: continue
            if partial_value == 0: sums.append([card])
            if partial_value > 0:
                partial_cards = cards.copy()
                partial_cards = [c for c in partial_cards if c.value<card.value]
                partial_sums = self.calculate_sum_takes(partial_value, partial_cards.copy(), [])
                for p in partial_sums:
                    p.insert(0, card)
                    sums.append(p)

        return sums

    def throw_card(self, card, cards_to_take=None, type_of_take=0):
        if type_of_take == 0:
            self.cards.append(card)
            return None, None

        else:
            self.cards = [card for card in self.cards if card not in cards_to_take]
            taken_cards = cards_to_take.copy()

            taken_cards.insert(0, card)
            scopa_card = True if len(self.cards)==0 and type_of_take!=2 else False
            return taken_cards, scopa_card
            # else:
            #     raise Exception('Prohibited Take')
            #     exit(1)