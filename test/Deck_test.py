import unittest

import Deck


class MyTestCase(unittest.TestCase):

    deck = Deck.Deck()

    def test_length(self):
        self.assertEqual(len(self.deck.cards), 40)

    def test_deck_dictionary(self):
        # print(self.deck.deck['Qc'].debug_print())
        # print(self.deck.cards[28].debug_print())
        self.assertEqual(self.deck.deck['Qc'], self.deck.cards[28])  # 0-9 diamonds 10-19 hearts 20-29 clubs 30-39 spades

    def test_players_decks(self):
        self.assertEqual(len(self.deck.players_decks[0]), 10)
        self.assertEqual(len(self.deck.players_decks[1]), 10)
        self.assertEqual(len(self.deck.players_decks[2]), 10)
        self.assertEqual(len(self.deck.players_decks[3]), 10)

    def test_players_decks_different(self):
        grouped_players_cards = []
        for player_deck in self.deck.players_decks:
            for card in player_deck:
                grouped_players_cards.append(card)

        grouped_players_cards = [card.id for card in grouped_players_cards]
        set_players_decks = set(grouped_players_cards)
        print(set_players_decks)

        self.assertEqual(len(set_players_decks), 40)



if __name__ == '__main__':
    unittest.main()
