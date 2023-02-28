import Utils
from Deck import get_card_by_id

class Team:

    def __init__(self, id, name, player1, player2):
        self.id = id
        self.name = name
        self.player1 = player1
        self.player2 = player2
        self.cards = []
        self.scopaCards = []
        self.points = 0

    def takes(self, taken_cards, scopaCard=None):
        self.cards.append(taken_cards)
        if scopaCard is not None:
            self.scopaCards.append(scopaCard)

    def count_points(self):
        #settebello
        settebello = get_card_by_id('7d')
        if settebello in self.cards: self.points += 1
        #cards number
        if len(self.cards) > 20: self.points+=1
        #diamonds
        diamonds = [card for card in self.cards if card.seed=='diamonds']
        if len(diamonds) > 5: self.points += 1
        #primiera -> returned to game to be established
        primiera_points = 0
        for seed in Utils.SEEDS:
            seed_cards = [Utils.primiera__sign2points(card.sign) for card in self.cards if card.seed==seed]
            primiera_points += max(seed_cards) if len(seed_cards)>0 else 0

        #scopa
        self.points += len(self.scopaCards)
        #napola
        diamonds = set(diamonds.map(lambda x:x.value))
        all_diamonds = set(range(Utils.CARDS_PER_SEED))
        opponent_diamonds = all_diamonds.difference(diamonds)
        min_opponent_diamond = min(opponent_diamonds) if len(opponent_diamonds)>0 else 11 #11 because so you have until 10
        if min_opponent_diamond > 3: self.points += min_opponent_diamond-1 #if 4, your team has 1,2,3 and so on...
        #napoleone wins the match
        napoleone_check = True if len(opponent_diamonds)==0 else False

        return self.points, primiera_points, napoleone_check
