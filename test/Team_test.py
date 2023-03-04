import unittest

import Card
import Deck
import Player
import Team


class MyTestCase(unittest.TestCase):
    def test_points(self):
        team = Team.Team(id=1, name='di-mazzo',
                         player2=Player.Player(pos=1, nick='g'),
                         player1=Player.Player(pos=2, nick='h'))
        team.cards.append(Card.Card('diamonds', 7))

        # ret_names = ['cards', 'diamonds', 'settebello', 'primiera', 'scopa', 'napola', 'napoleone']
        points_stats = team.count_points()

        self.assertEqual(points_stats['cards'], 1)
        self.assertEqual(points_stats['diamonds'], 1)
        self.assertTrue(points_stats['settebello'])
        self.assertEqual(points_stats['primiera'], 21)  # value for just a 7
        self.assertEqual(points_stats['scopa'], 0)
        self.assertEqual(points_stats['napola'], 0)
        self.assertFalse(points_stats['napoleone'])

    def test_primiera_oneScopa(self):
        team = Team.Team(id=1, name='di-mazzo',
                         player2=Player.Player(pos=1, nick='g'),
                         player1=Player.Player(pos=2, nick='h'))

        six_diamonds = Card.Card('diamonds', 6)
        six_spades = Card.Card('spades', 6)
        seven_clubs = Card.Card('clubs', 7)
        three_hearts = Card.Card('hearts', 3)
        king_spades = Card.Card('spades', 10)

        team.takes(taken_cards=[six_diamonds, six_spades], scopa_card=six_diamonds)
        team.takes(taken_cards=[king_spades, seven_clubs, three_hearts], scopa_card=None)

        # ret_names = ['cards', 'diamonds', 'settebello', 'primiera', 'scopa', 'napola', 'napoleone']
        points_stats = team.count_points()

        self.assertEqual(points_stats['cards'], 5)
        self.assertEqual(points_stats['diamonds'], 1)
        self.assertEqual(points_stats['settebello'], False)
        self.assertEqual(points_stats['primiera'], sum([18,13,21,18]))  # value for 6diamonds, 3hearts, 7clubs, 6spades
        self.assertEqual(points_stats['scopa'], 1)
        self.assertEqual(points_stats['napola'], 0)
        self.assertEqual(points_stats['napoleone'], False)

    def test_napola_untilFive(self):
        team = Team.Team(id=1, name='di-mazzo',
                         player2=Player.Player(pos=1, nick='g'),
                         player1=Player.Player(pos=2, nick='h'))

        deckObj = Deck.Deck()
        deck = deckObj.deck

        team.takes(taken_cards=[deck['5d'], deck['5s']], scopa_card=deck['5d'])
        team.takes(taken_cards=[deck['Ad'], deck['2d'], deck['6c'], deck['4d']], scopa_card=None)
        team.takes(taken_cards=[deck['Jh'], deck['3d'], deck['5c']], scopa_card=None)

        # ret_names = ['cards', 'diamonds', 'settebello', 'primiera', 'scopa', 'napola', 'napoleone']
        points_stats = team.count_points()

        self.assertEqual(points_stats['cards'], 9)
        self.assertEqual(points_stats['diamonds'], 5)
        self.assertEqual(points_stats['settebello'], False)
        self.assertEqual(points_stats['primiera'], sum([16, 10, 18, 15]))  # value for 1diamonds, Jhearts, 6clubs, 5spades
        self.assertEqual(points_stats['scopa'], 1)
        self.assertEqual(points_stats['napola'], 5)
        self.assertEqual(points_stats['napoleone'], False)

    def test_napoleone(self):
        team = Team.Team(id=1, name='di-mazzo',
                         player2=Player.Player(pos=1, nick='g'),
                         player1=Player.Player(pos=2, nick='h'))

        deckObj = Deck.Deck()
        deck = deckObj.deck

        team.takes(taken_cards=[deck['Ad'], deck['2d'], deck['3d'], deck['4d'],
                                deck['5d'], deck['6d'], deck['7d'], deck['Jd'],
                                deck['Qd'], deck['Kd']], scopa_card=None)

        # ret_names = ['cards', 'diamonds', 'settebello', 'primiera', 'scopa', 'napola', 'napoleone']
        points_stats = team.count_points()

        self.assertEqual(points_stats['cards'], 10)
        self.assertEqual(points_stats['diamonds'], 10)
        self.assertEqual(points_stats['settebello'], True)
        self.assertEqual(points_stats['primiera'], 21)  # just 7diamonds, no clubs,spades,hearts
        self.assertEqual(points_stats['scopa'], 0)
        self.assertEqual(points_stats['napola'], 10)
        self.assertEqual(points_stats['napoleone'], True)

if __name__ == '__main__':
    unittest.main()
