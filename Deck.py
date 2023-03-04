import random

from Card import Card
import Utils


class Deck:
    # num should be 40, maybe 52 or 108, but i'm using 40

    def __init__(self):
        self.cards = [Card(seed, value) for seed in Utils.SEEDS for value in Utils.VALUES]
        self.deck = dict(zip([c.id for c in self.cards], self.cards))
        self.players_decks = []
        self.distribute_cards()

    def distribute_cards(self):
        cards = self.cards.copy()
        for _ in range(Utils.PLAYERS_NUMBER):
            player_deck = random.sample(cards, Utils.CARDS_PER_PLAYER)
            cards = [card for card in cards if card not in player_deck]
            self.players_decks.append(sorted(player_deck, key=lambda x: x.value))

    # def get_card_by_position(self, position):
    #     return self.cards[position]

    def print_deck(self):
        ids = [card.id for card in self.cards]
        print(ids)

    def debug_print(self):
        print(self.players_decks.map(lambda x: x.id))
        print(self.cards.map(lambda x: x.id))
