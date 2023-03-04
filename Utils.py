import Card

PLAYERS_NUMBER = 4
CARDS_PER_PLAYER = 10
SEED_NUMBER = 4
CARDS_PER_SEED = 10
SEEDS = ['diamonds', 'hearts', 'clubs', 'spades']
VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
TURNS = 10

card__val2sign = {1: 'A',
                  2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                  8: 'J',
                  9: 'Q',
                  10: 'K'}

card__sign2val = dict((v, k) for k, v in card__val2sign.items())

seed__ordering = {'diamonds': 0,
                  'hearts': 1,
                  'clubs': 2,
                  'spades': 3}

seed__id2name = {'d': 'diamonds',
                 'h': 'hearts',
                 'c': 'clubs',
                 's': 'spades'}

seed__name2id = dict((v, k) for k, v in seed__id2name.items())


def card__id2value_seed(id):
    card_sign = id[:1]
    seed_id = id[1:]
    return card__sign2val[card_sign], seed__id2name[seed_id]


def card__value_seed2id(value, seed):
    card_sign = card__val2sign[value]
    seed_id = seed__name2id[seed]
    return card_sign + seed_id


primiera__sign2points = {'A': 16, '2': 12, '3': 13, '4': 14, '5': 15, '6': 18, '7': 21, 'J': 10, 'Q': 10, 'K': 10}


seed__id2print = {'d': '♦',
                  'h': '♥',
                  'c': '♣',
                  's': '♠'}

def card__id2print(id):
    sign = id[:1]
    seed = id[1:]
    return sign+seed__id2print[seed]


# DONT LIKE IT, CARDS SHOULD BE JUST 40, ONE INSTANCE EACH, IM MAKING DECK GETTABLE
# def get_card_by_id(id):
#     value, seed = card__id2value_seed(id)
#     seed_position = seed__ordering[seed]
#     return Card.Card(value, seed)
