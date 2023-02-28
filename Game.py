import Deck
import Player


class Game:
    def __init__(self):
        self.deck = Deck.Deck()
        self.players = []
        for p in self.initiate_players():
            self.players.append(p)

        (team1, team2, team1, team2) = self.players
        print(team1)

    def initiate_players(self):
        n1 = input("P1's name: ")
        n2 = input("P2's name: ")
        n3 = input("P3's name: ")
        n4 = input("P4's name: ")

        p1 = Player.Player(n1, 1)
        p2 = Player.Player(n2, 2)
        p3 = Player.Player(n3, 3)
        p4 = Player.Player(n4, 4)

        return p1, p2, p3, p4

    def deal_cards(self):
        pass