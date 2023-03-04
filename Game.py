import Board
import Deck
import Player
import Team
import Utils


class Game:
    def __init__(self):
        self.board = Board.Board()
        self.deck = Deck.Deck()
        self.players = []
        for p in self.initiate_players():
            self.players.append(p)

        self.teams = [Team.Team(id=1, name='contro-mazzo', player1=self.players[0], player2=self.players[2]),
                      Team.Team(id=2, name='di-mazzo', player1=self.players[1], player2=self.players[3])]

        for i in range(Utils.PLAYERS_NUMBER):
            self.players[i].cards = self.deck.players_decks[i]

        self.startTurns()

    def initiate_players(self):
        # n1 = input("P1's name: ")
        # n2 = input("P2's name: ")
        # n3 = input("P3's name: ")
        # n4 = input("P4's name: ")
        n1 = 'a'
        n2 = 'b'
        n3 = 'c'
        n4 = 'd'

        p1 = Player.Player(nick=n1, pos=1)
        p2 = Player.Player(nick=n2, pos=2)
        p3 = Player.Player(nick=n3, pos=3)
        p4 = Player.Player(nick=n4, pos=4)

        return p1, p2, p3, p4

    def startTurns(self):
        print('\n')
        for player in self.players:
            print(player.nick, "'s cards:", [Utils.card__id2print(x.id) for x in player.cards])
        for i in range(Utils.TURNS):
            print('\n',
                  '---------------------------------------\n',
                  '              TURN NUMBER ',i+1,'\n',
                  '---------------------------------------',
                  )
            for player in self.players:
                self.ask_move(player)

        self.counting_points()

    def ask_move(self, player):
        print('\n', player.nick, "'s turn.")
        print("Your (", len(player.cards),") cards: ", [Utils.card__id2print(x.id) for x in player.cards])
        print("The board holds: ", [Utils.card__id2print(x.id) for x in self.board.cards])
        thrown_card = None
        while thrown_card is None:
            # thrown_card = input("Choose which card to play (h for help): ")
            # FOR DEBUG PUROSES, EACH PLAYER PLAYS ITS FIRST CARD EACH TIME
            thrown_card = player.cards[0].id
            if thrown_card in ['h', 'H']:
                print("you should type c for ♣, d for ♦, h for ♥ and s for ♠) \n",
                      "e.g. 7d for 7♦")
                thrown_card = None
            elif thrown_card not in [x.id for x in player.cards]:
                print("Don't cheat! You don't have that card in your hand. Try again.")
                thrown_card = None

        #TODO: check type of take, ask for choice, board.throw_card()
        thrown_card = self.deck.deck[thrown_card]
        # thrown_card.debug_print()
        available_takes, type_of_take = self.board.available_takes_and_type(thrown_card)
        chosen_take = None
        if type_of_take != 0:  # also means that len(available_takes) == 0
            if len(available_takes) > 1:
                print('The available Takes: \n')
                for i in range(len(available_takes)):
                    print(i+1, ') ', [Utils.card__id2print(x.id) for x in available_takes[i]], '\n')
                while chosen_take is None:
                    chosen_take = input("Choose what cards you want to take: ")
                    # print(chosen_take)
                    # for x in range(1, len(available_takes)+1): print(x)
                    if int(chosen_take) < 1 or int(chosen_take) > len(available_takes)+1:
                        print('Take number ', chosen_take, ' is not available. Choose again.')
                        chosen_take = None
                if type_of_take == 3: chosen_take = available_takes[int(chosen_take)] # take number 3 works differently
            else:  # just one take
                print('taking ', [Utils.card__id2print(x.id) for x in available_takes[0]])
                chosen_take = available_takes[0]

        player.cards.remove(thrown_card)
        taken_cards, scopa_card = self.board.throw_card(card=thrown_card, cards_to_take=chosen_take, type_of_take=type_of_take)
        if type_of_take !=0:
            player.team.takes(taken_cards=taken_cards, scopa_card=scopa_card)

    def counting_points(self):
        print('\n',
              '---------------------------------------\n',
              '              COUNTING POINTS\n',
              '---------------------------------------\n')


        stats_team1 = self.teams[0].count_points()
        stats_team2 = self.teams[1].count_points()

        # ret_names = ['cards', 'diamonds', 'settebello', 'primiera', 'scopa', 'napola', 'napoleone']
        points_team1 = 0
        points_team2 = 0
        print('The game is over.')
        print('TEAM 1 has taken: ', [Utils.card__id2print(x.id) for x in self.teams[0].cards])
        print('TEAM 2 has taken: ', [Utils.card__id2print(x.id) for x in self.teams[1].cards])
        print('\n')
        print('TEAM 1 vs TEAM 2')
        # cards
        print("CARDS:", stats_team1['cards'], ' vs ', stats_team2['cards'])
        if(stats_team1['cards'] > stats_team2['cards']): points_team1 += 1
        elif(stats_team1['cards'] < stats_team2['cards']) : points_team2 += 1
        # diamonds
        print("DIAMONDS:", stats_team1['diamonds'], ' vs ', stats_team2['diamonds'])
        if(stats_team1['diamonds'] > stats_team2['diamonds']): points_team1 += 1
        elif(stats_team1['diamonds'] < stats_team2['diamonds']) : points_team2 += 1
        # settebello
        print("SETTEBELLO:", stats_team1['settebello'], ' vs ', stats_team2['settebello'])
        if stats_team1['settebello'] is True: points_team1 += 1
        if stats_team2['settebello'] is True: points_team2 += 1
        # primiera
        print("PRIMIERA:", stats_team1['primiera'], ' vs ', stats_team2['primiera'])
        if (stats_team1['primiera'] > stats_team2['primiera']): points_team1 += 1
        elif (stats_team1['primiera'] < stats_team2['primiera']): points_team2 += 1
        # scopa
        print("SCOPA:", stats_team1['scopa'], ' vs ', stats_team2['scopa'])
        points_team1 += stats_team1['scopa']
        points_team2 += stats_team2['scopa']
        # napola
        print("NAPOLA:", stats_team1['napola'], ' vs ', stats_team2['napola'])
        points_team1 += stats_team1['napola']
        points_team2 += stats_team2['napola']
        # napoleone
        if stats_team1['napoleone'] is True: print('AAAAAAAAA TEAM 1 DID NAPOLEONE')
        if stats_team2['napoleone'] is True: print('AAAAAAAAA TEAM 2 DID NAPOLEONE')
        # total points
        print('\n')
        print("TOTAL POINTS: ", points_team1, " vs ", points_team2)
        if points_team1 > points_team2: print("Congratulations, Team 1, You won! All hail Team 1")
        elif points_team1 < points_team2: print("Congratulations, Team 2, You won! All hail Team 2")
        else: print("Very sad! It's a tie")








