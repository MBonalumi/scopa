import unittest

import Board
import Card
import Deck
# import Utils


class MyTestCase(unittest.TestCase):
    deck = Deck.Deck()

    def test_card_throws(self):
        board = Board.Board()
        queen_clubs = self.deck.deck['Qc']
        king_spades= self.deck.deck['Ks']
        board.throw_card(queen_clubs)
        board.throw_card(king_spades)
        self.assertEqual(board.cards, [queen_clubs, king_spades])

    def test_sameValue_oneChoice(self):
        board = Board.Board()
        queen_clubs = self.deck.deck['Qc']
        five_spades = self.deck.deck['5s']
        thrown_card = self.deck.deck['Qd']

        taken_cards, scopa_card = board.throw_card(queen_clubs)
        self.assertIs(taken_cards, None)
        self.assertIs(scopa_card, None)
        board.throw_card(five_spades)

        takes, take_type = board.available_takes_and_type(thrown_card)
        self.assertEqual(take_type, 1)  # same value take
        self.assertEqual(len(takes), 1) # one choice
        first_take = takes[0]
        self.assertIn(queen_clubs, first_take) #choice is queen of clubs

        taken_cards, scopa_card = board.throw_card(thrown_card, first_take, take_type)
        self.assertEqual(len(taken_cards), 2)
        self.assertEqual(taken_cards[0], thrown_card)
        self.assertEqual(taken_cards[1], first_take[0])
        self.assertIs(scopa_card, False)
        self.assertEqual(len(board.cards), 1)
        self.assertIn(five_spades, board.cards)

    def test_ace_take(self):
        board = Board.Board()
        queen_clubs = self.deck.deck['Qc']
        five_spades = self.deck.deck['5s']
        thrown_card = self.deck.deck['Ad']

        board.throw_card(queen_clubs)
        board.throw_card(five_spades)

        takes, take_type = board.available_takes_and_type(thrown_card)
        self.assertEqual(take_type, 2)  # ace take
        self.assertEqual(len(takes), 1)  # one take
        first_take = takes[0]
        self.assertEqual(len(first_take), len(board.cards))  # take all cards
        self.assertIn(queen_clubs, first_take)  # choice is all
        self.assertIn(five_spades, first_take)  # choice is all

        taken_cards, scopa_card = board.throw_card(thrown_card, first_take, take_type)
        self.assertEqual(taken_cards[0], thrown_card)
        self.assertIn(queen_clubs, taken_cards)
        self.assertIn(five_spades, taken_cards)
        self.assertIs(scopa_card, False)
        self.assertEqual(len(board.cards), 0)

    def test_ace_emptyBoard(self):
        board = Board.Board()
        thrown_card = Card.Card(value=1, seed='diamonds')

        takes, take_type = board.available_takes_and_type(thrown_card)
        self.assertEqual(take_type, 2)  # ace take
        self.assertEqual(len(takes), 1)  # one take

        taken_cards, scopa_card = board.throw_card(thrown_card, [], take_type)
        self.assertEqual(taken_cards[0], thrown_card)
        self.assertIs(scopa_card, False)
        self.assertEqual(len(board.cards), 0)

    def test_takesSum_scopa(self):
        board = Board.Board()
        five_spades = self.deck.deck['5s']
        four_spades = self.deck.deck['4s']
        thrown_card = self.deck.deck['Qd']

        board.throw_card(four_spades)
        board.throw_card(five_spades)

        takes, take_type = board.available_takes_and_type(thrown_card)
        self.assertEqual(take_type, 3)  # sum take
        self.assertEqual(len(takes), 1)  # one take
        first_take = takes[0]
        first_take_sum = 0
        for x in first_take: first_take_sum += x.value
        self.assertEqual(first_take_sum, thrown_card.value)  # respected sum
        self.assertIn(four_spades, first_take)
        self.assertIn(five_spades, first_take)

        taken_cards, scopa_card = board.throw_card(thrown_card, first_take, take_type)
        self.assertEqual(taken_cards[0], thrown_card)
        self.assertIn(four_spades, taken_cards)
        self.assertIn(five_spades, taken_cards)
        self.assertEqual(len(board.cards), 0)
        self.assertIs(scopa_card, True)

    def test_sameValue_overSum(self):
        # throw Qclubs, Qspades, 5spades, 4clubs
        # then takes of throw Qdiamonds must be the two queens, not the sum
        board = Board.Board()
        thrown_card = self.deck.deck['Qc']
        queen_spades = self.deck.deck['Qs']
        five_spades = self.deck.deck['5s']
        four_spades = self.deck.deck['4s']

        board.throw_card(queen_spades)
        board.throw_card(five_spades)
        board.throw_card(four_spades)

        takes, take_type = board.available_takes_and_type(thrown_card)
        self.assertEqual(take_type, 1)  # same value take over sum take
        self.assertEqual(len(takes), 1)  # one take, sum should be an option
        first_take = takes[0]
        self.assertIn(queen_spades, first_take)
        self.assertNotIn(four_spades, first_take)  # choice is all
        self.assertNotIn(five_spades, first_take)  # choice is all

    def test_sameValue_twoChoices(self):
        board = Board.Board()
        thrown_card = self.deck.deck['Qc']
        queen_spades = self.deck.deck['Qs']
        queen_diamonds = self.deck.deck['Qd']

        board.throw_card(queen_spades)
        board.throw_card(queen_diamonds)

        takes, take_type = board.available_takes_and_type(thrown_card)
        self.assertEqual(take_type, 1)  # same value takes
        self.assertEqual(len(takes), 2)  # two takes
        first_take = takes[0]
        second_take = takes[1]
        self.assertIn(queen_spades, first_take)
        self.assertNotIn(queen_spades, second_take)
        self.assertIn(queen_diamonds, second_take)

    def test_sumTake_twoChoices(self):
        board = Board.Board()
        thrown_card = self.deck.deck['Kc']
        six_spades = self.deck.deck['6s']
        five_spades = self.deck.deck['5s']
        four_spades = self.deck.deck['4s']
        three_spades = self.deck.deck['3s']
        two_spades = self.deck.deck['2s']

        board.throw_card(six_spades)
        board.throw_card(five_spades)
        board.throw_card(four_spades)
        board.throw_card(three_spades)
        board.throw_card(two_spades)

        takes, take_type = board.available_takes_and_type(thrown_card)
        # for t in takes:
        #     print('take: ', [x.id for x in t], '\n')
        self.assertEqual(take_type, 3)  # sum takes
        self.assertEqual(len(takes), 2)  # two takes

        first_take = takes[0]
        self.assertEqual(len(first_take), 2)
        self.assertIn(six_spades, first_take)
        self.assertIn(four_spades, first_take)
        second_take = takes[1]
        self.assertEqual(len(second_take), 3)
        self.assertIn(five_spades, second_take)
        self.assertIn(three_spades, second_take)
        self.assertIn(two_spades, second_take)


if __name__ == '__main__':
    unittest.main()
