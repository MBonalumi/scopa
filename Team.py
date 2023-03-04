import Card
import Utils


class Team:

    def __init__(self, id, name, player1, player2):
        self.id = id
        self.name = name
        self.player1 = player1
        self.player2 = player2
        self.player1.team = self
        self.player2.team = self
        self.cards = []
        self.scopa_cards = []
        self.points = 0

    def takes(self, taken_cards, scopa_card=None):
        for card in taken_cards:
            self.cards.append(card)
        if scopa_card is not None:
            self.scopa_cards.append(scopa_card)

    # ret_names = ['cards', 'diamonds', 'settebello', 'primiera', 'scopa', 'napola', 'napoleone']
    def count_points(self):
        # settebello
        settebello = Card.Card(value=7, seed='diamonds')
        settebello_check = True if settebello in self.cards else False
        # cards number
        my_cards = len(self.cards)
        # if len(self.cards) > 20: self.points+=1
        # diamonds
        diamonds = [card for card in self.cards if card.seed == 'diamonds']
        my_diamonds = len(diamonds)
        # if len(diamonds) > 5: self.points += 1
        # primiera
        primiera_points = 0
        for seed in Utils.SEEDS:
            seed_cards = [Utils.primiera__sign2points[card.sign] for card in self.cards if card.seed == seed]
            primiera_points += max(seed_cards) if len(seed_cards) > 0 else 0

        # scopa
        my_scopa = len(self.scopa_cards)
        # self.points += len(self.scopaCards)
        # napola
        diamonds = set([x.value for x in diamonds])
        all_diamonds = set(range(1, 11)) # get all values for diamond suit cards
        opponent_diamonds = all_diamonds.difference(diamonds)
        min_opponent_diamond = min(opponent_diamonds) if len(opponent_diamonds) > 0 else 11  # 11 because so you have until 10
        # if min_opponent_diamond > 3: self.points += min_opponent_diamond-1 #if 4, your team has 1,2,3 and so on...
        my_napola = min_opponent_diamond - 1 if min_opponent_diamond > 3 else 0  # if 4, your team has 1,2,3 and so on...
        # napoleone wins the match
        napoleone_check = True if len(opponent_diamonds) == 0 else False
        ret_names = ['cards', 'diamonds', 'settebello', 'primiera', 'scopa', 'napola', 'napoleone']
        ret_tuple = [my_cards, my_diamonds, settebello_check, primiera_points, my_scopa, my_napola, napoleone_check]

        return dict(zip(ret_names, ret_tuple))
