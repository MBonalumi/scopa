class Board:

    def __init__(self):
        self.cards = []

    def triggered_take_type(self, thrown_card, cards_to_take):
        card_values = [card.value for card in self.cards].sort()
        if thrown_card.value in card_values:
            return 1  # (a) same value card on board
        if thrown_card.value == 1:
            return 2  # (b) thrown card is an Ace
        if cards_to_take.map(lambda x: x.value).sum() == thrown_card.value and cards_to_take in self.cards:
            return 3  # (c) cards_to_take are in self.cards & they sum to thrown card
        # else
        return 0

    def throw_card(self, player, card, cards_to_take=None):
        if cards_to_take is None:
            self.cards.append(card)
            return None, None
        else:
            type_of_take = self.triggered_take_type(card, cards_to_take)
            if type_of_take != 0:
                self.cards = [card for card in self.cards if card not in cards_to_take]
                taken_cards = [card].append(cards_to_take)
                scopa_card = True if self.cards is None and type_of_take is not 2 else False #ace take shouldn't trigger scopa
                return taken_cards, scopa_card
            else:
                raise Exception('Prohibited Take')
                exit(1)