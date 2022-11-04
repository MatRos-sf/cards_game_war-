"""
Walet - Jack
Dama - Queen
Król - King
As
2,3,4,5,6,7,8,9,10,J,Q,K,A
pik - Spades
kier - Hearts
trefl - Clubs
karo - Diamonds
"""
import random

# Errors
class NoneOfCards(Exception):
    pass


def create_deck_of_cards(amt=1):
    """
    The function create deck of cards
    :param amt: number deck of cards
    :return: deck_of_cards
    """
    colors = list('SHCD')
    figure_number = list(range(2, 11)) + list('JQKA')
    deck_of_cards = [(cards, c) for c in colors for cards in figure_number]

    return deck_of_cards * amt


def power_card(card):
    if type(card) == int:
        return card
    dic_arr = {
        'A': 14, 'K': 13, 'Q': 12, 'J': 11,
    }
    return dic_arr[card]


class Player:

    def __init__(self, id_player):

        self.id_player = id_player
        self.player_cards = []
        self.card = None
        self.power = None
        self.in_game = True
        # war
        self.card_face_up = None
        self.card_face_down = None
        self.war_cards = []

    def amt_all_cards(self):
        return len(self.player_cards)

    def reveal_card(self):
        """
        Odsłania pierwszą kartę z brzegu
        :return: wartość karty
        """
        self.card = self.player_cards[0]
        self.player_cards.pop(0)
        self.power = power_card(self.card[0])
        return self.power

    def reveal_card_war(self):
        if self.card_face_up and self.card_face_down:
            # another war
            self.war_cards.append(self.card_face_up)
            self.card_face_up = None
            self.war_cards.append(self.card_face_down)
            self.card_face_down = None

        if self.amt_all_cards() >= 2:
            self.card_face_down = self.player_cards.pop(0)
            self.card_face_up = self.player_cards.pop(0)
            self.power = power_card(self.card_face_up[0])
            return self.power
        elif self.amt_all_cards() == 1:
            self.war_cards.append(self.player_cards.pop(0))
            return -1
        else:
            return -1

    def take_win_cards(self, cards):
        self.player_cards += cards


class Game:

    def __init__(self, amt_player, limit=None, curse=True, info=False):
        self.amt_player = amt_player
        self.players = []

        self.cards = []
        # this cards doesn't play
        self.cards_out = []
        # number of round
        self.round = 0
        self.course_of_game = []  # przebieg gry

        # extra setting
        self.limit = limit  # limits of rounds
        self.curse = curse  # delete carts when rounds is above 100
        self.info = info    # if True show extra info

    def print_players_and_cards(self) -> None:

        max_len_cards = 0  # max amt cards
        # Calculate max amt cards
        for p in self.players:
            len_cards = p.amt_all_cards()
            if len_cards > max_len_cards:
                max_len_cards = len_cards

        # Player 1, cards: [('A', 'D'), (2, 'H'), (5, 'S'), (6, 'C'), ('J', 'D'), (3, 'D'), (8, 'D')
        # Player 1, cards: [   ===> 20 chars
        # ('A', 'D'),    ===> 10 chars
        # ] ===> 1 char

        amt_stars = 20 + (10 * max_len_cards) + 1
        print('*' * amt_stars)
        for p in self.players:
            print(f"Player {p.id_player}, cards: {p.player_cards}")
        print('*' * amt_stars)

    def show_winner(self):
        """
        The function show winner or winners
        :return: Tummples :
                    First element: single winner (class Player) or list of winners (list of Players)
                    Second element: bool variable if more than one winner show true else False
        """
        if self.len_players() == 1:
            return self.players[0], False
        else:
            max_amt_player_cards = -1
            winners = []
            for p in self.players:
                amt_player_cards = p.amt_all_cards()
                if amt_player_cards > max_amt_player_cards:
                    if winners:
                        winners = []
                        winners.append(p)
                    else:
                        winners.append(p)
                    max_amt_player_cards = amt_player_cards
                elif amt_player_cards == max_amt_player_cards:
                    winners.append(p)

            if len(winners) == 1:
                return winners[0], False
            else:
                return winners, True

    def len_players(self):
        return len(self.players)

    def create_players(self) -> None:
        for i in range(self.amt_player):
            self.players.append(Player(i + 1))

    def create_cards(self):
        amt = 1
        cards = []

        if 52 // self.amt_player >= 5:
            cards = create_deck_of_cards(amt)
        else:
            while True:
                amt += 1
                if (amt * 52) // self.amt_player >= 5:
                    break
            cards = create_deck_of_cards(amt)

        return cards

    def shuffling(self) -> None:
        """
        Function shuffleing all cards
        """
        if self.cards:
            random.shuffle(self.cards)
            random.shuffle(self.cards)
            random.shuffle(self.cards)
        else:
            raise NoneOfCards("You can't shuffling card if you didn't create ones")

    def deal_cards(self):

        # First cards must be shufflinfg
        self.shuffling()

        amt_cards_of_player, del_card = divmod(len(self.cards), len(self.players))
        # if you don't have enough cards
        if del_card > 0:
            self.cards_out = self.cards[:del_card]
            self.cards = self.cards[del_card:]

        # deal cards
        for p in self.players:
            p.player_cards = self.cards[:amt_cards_of_player]
            self.cards = self.cards[amt_cards_of_player:]
        # print("Deal carts done!")
        # print_players_and_cards(self.players)

    def set_game(self):
        # create players and deal cards
        self.create_players()
        self.cards = self.create_cards()
        self.deal_cards()

    def baned_cards(self):
        """
        Usuwa karty pierwsze karty każdego z graczy
        """
        cards = []
        for p in self.players:
            cards.append(p.player_cards.pop(0))
        return cards

    def delete_player(self, player_out):
        """
        Function remove players
        :param player_out: List of players who will be remove
        :return:
        """
        for p in player_out:
            self.players.remove(p)

    def check_able_to_game(self) -> None:
        players_out = []
        for p in self.players:
            if p.amt_all_cards() == 0:
                players_out.append(p)

        if players_out:
            self.delete_player(players_out)
            if self.info:
                print("Player out: ", " ".join(str(p.id_player) for p in players_out), "Round ", self.round)

    def war(self, winners):
        """
        War
        :param winners:list of competitor war (index number)
        :return:
        """
        power_max = 0
        win = None  # None of the players won.
        list_winner = []
        more_than_one_winner = False

        for i in winners:
            current_card = self.players[i].reveal_card_war()
            if power_max < current_card:
                power_max = current_card
                win = i
                more_than_one_winner = False
                if list_winner:
                    list_winner = []
            elif power_max == current_card:
                if not list_winner:
                    more_than_one_winner = True
                    list_winner.append(win)
                list_winner.append(i)
        if more_than_one_winner:
            return self.war(list_winner)
        if win == None:     return -1

        return win

    def take_cards(self):
        """
        funkcja bierze karty które brały udział w rundzie
        i ustawia wartości domyślne
        :return: lista kart która brala udział w 1 walce
        """
        cards = []
        for p in self.players:

            cards.append(p.card)
            p.card = None

            if p.card_face_up:
                cards.append(p.card_face_up)
                p.card_face_up = None

                cards.append(p.card_face_down)
                p.card_face_down = None

            if p.war_cards:
                cards += p.war_cards
                p.war_cards = []

        return cards

    def battle(self):
        """
        It's single round.
        :return:
        """

        power_max = 0
        more_than_one_winner = False
        win = None
        winners = []

        # szukanie najlepszej karty

        for index, c in enumerate(self.players):
            current_card = c.reveal_card()  # power currently card
            if power_max < current_card:
                power_max = current_card
                win = index
                more_than_one_winner = False
                if winners:
                    winners = []
            elif power_max == current_card:
                more_than_one_winner = True
                if not winners:     winners.append(win)
                winners.append(index)

        # check if win more than one Player
        if more_than_one_winner:
            win = self.war(winners)

        # take cards
        cards_for_round = self.take_cards()

        if win == -1:
            # jeżeli gracze po wojnie nie wyłoni zwycięzcy, wygrane karty kończą w karcie do usuwania.
            if cards_for_round:
                self.cards_out += cards_for_round

            return win

        # The winner take all card with round
        self.players[win].take_win_cards(cards_for_round)

        return self.players[win].id_player

    def game(self):

        winner = self.battle()  # id_player or -1
        # przebieg gry
        if winner == -1:
            # nie rozstrzygnięto zwycięscy dodajemy -1
            self.course_of_game.append(winner)

        else:

            self.course_of_game.append(winner)

        # check if player don't have cards, player must be deleted.
        # able to game
        player_out = self.check_able_to_game()

        if player_out:
            self.delete_player(player_out)

        return winner

    def result_game(self):
        """
        All players who survi
        :return:
        """
        result = [p.id_player for p in self.players]
        return result

    def play(self):
        win = None  # we don't use this veriable
        while self.len_players() > 1:

            self.round += 1

            # when is limit rounds
            if self.limit:
                if self.limit <= self.round:
                    break

            if self.curse:
                # delete one card for all players - > reason -> the game would be play infinity
                if self.round % 100 == 0:
                    c = self.baned_cards()
                    self.check_able_to_game()
                    self.cards_out += c

            win = self.game()

        # funkcja ma zwracać listę zwycięsców
        return self.result_game()
        # return win # tutaj kto wygrał gre


