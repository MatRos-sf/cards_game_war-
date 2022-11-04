from war_game import Game, Player


def test_correct_amt_cards():
    """
    Test sprqwdzający poprawną ilość kart w grze
    ** według założenia zaodnik musi mieć minimum 5 kart!

    """
    for i in range(2, 100):
        g = Game(i)
        assert len(g.create_cards()) // i >= 5

    print(test_correct_amt_cards.__name__, " + ")


def test_correct_deal_cards():
    """
    test sprawdzający czy karty zostały rozdzielone po równo
    """
    sample_cards = [(1, 'a') for _ in range(100)]
    for i in range(2, 51):
        g = Game(i)
        g.cards = sample_cards
        g.create_players()
        g.deal_cards()
        assert g.players[0].amt_all_cards() == g.players[0].amt_all_cards()
    print(test_correct_deal_cards.__name__, ' +')


def test_war_one_winner_simple():
    player_one = Player(1)
    player_two = Player(2)
    player_three = Player(3)

    # set cards player
    # simple
    player_one.player_cards = [(2, 'T'), (8, 'T')]
    player_two.player_cards = [(2, 'T'), ('K', 'T')]
    player_three.player_cards = [(2, 'T'), (8, 'T')]

    g = Game(3)
    g.players = [player_one, player_two, player_three]

    assert g.war([0, 1, 2]) == 1
    print(test_war_one_winner_simple.__name__, ' +')


def test_double_war_one_winner():
    player_one = Player(1)
    player_two = Player(2)
    player_three = Player(3)

    # set cards player
    # simple
    player_one.player_cards = [(2, 'T'), (8, 'T'), (2, 'T'), (2, 'T')]
    player_two.player_cards = [(2, 'T'), (8, 'T'), (2, 'T'), (8, 'T')]
    player_three.player_cards = [(2, 'T'), (8, 'T'), (2, 'T'), ('K', 'T')]

    g = Game(3)
    g.players = [player_one, player_two, player_three]

    assert g.war([0, 1, 2]) == 2  # 3th player win

    print(test_double_war_one_winner.__name__, ' +')


def test_war_none_of_players_won():
    player_one = Player(1)
    player_two = Player(2)
    player_three = Player(3)

    # set cards player
    # simple
    player_one.player_cards = [(2, 'T'), (8, 'T'), (2, 'T'), (2, 'T'), (2, 'T'), (2, 'T')]
    player_two.player_cards = [(2, 'T'), (8, 'T'), (2, 'T'), (2, 'T'), (2, 'T'), (2, 'T')]
    player_three.player_cards = [(2, 'T'), (8, 'T'), (2, 'T'), (2, 'T'), (2, 'T'), (2, 'T')]

    g = Game(3)
    g.players = [player_one, player_two, player_three]

    assert g.war([0, 1, 2]) == -1  # None of players won

    print(test_war_none_of_players_won.__name__, ' +')


def test_take_cards():
    """
    Sprawdzenie czy wszystkie karty które brały udział zostaną usunięte
    :return:
    """
    except_result = []
    player_one = Player(1)
    player_two = Player(2)
    player_three = Player(3)

    player_one.player_cards = [(2, 'T'), (8, 'T')]
    player_one.card = (2, 'T')
    player_one.card_face_up = (3, 'T')
    player_one.card_face_down = (4, 'T')
    except_result += [(2, 'T'), (3, 'T'), (4, 'T')]

    player_two.player_cards = [(2, 'T'), (8, 'T')]
    player_two.card = (5, 'T')
    player_two.war_cards = [(6, 'T'), (7, 'T')]
    except_result += [(5, 'T')]
    except_result += [(6, 'T'), (7, 'T')]

    player_three.card = (8, 'T')
    except_result += [(8, 'T')]

    g = Game(3)
    g.players = [player_one, player_two, player_three]

    assert except_result == g.take_cards()

    print(test_take_cards.__name__, ' +')


def test_battle_one_win():
    p_one_card = [(2, 'T')]
    p_two_card = [(10, 'T')]
    p_three_card = [(3, 'T')]

    p_one = Player(1)
    p_one.player_cards = p_one_card
    p_two = Player(2)
    p_two.player_cards = p_two_card
    p_three = Player(3)
    p_three.player_cards = p_three_card

    g = Game(3)
    g.players = [p_one, p_two, p_three]

    assert g.battle() == 2
    print(test_battle_one_win.__name__, ' +')


def test_battle_none_win():
    p_one_card = [(10, 'T')]
    p_two_card = [(10, 'T')]
    p_three_card = [(10, 'T')]

    p_one = Player(1)
    p_one.player_cards = p_one_card
    p_two = Player(2)
    p_two.player_cards = p_two_card
    p_three = Player(3)
    p_three.player_cards = p_three_card

    g = Game(3)
    g.players = [p_one, p_two, p_three]

    assert g.battle() == -1

    print(test_battle_none_win.__name__, ' +')


def test_game_win_one():
    p_one_card = [(2, 'T')]
    p_two_card = [(10, 'T')]
    p_three_card = [(3, 'T')]

    p_one = Player(1)
    p_one.player_cards = p_one_card
    p_two = Player(2)
    p_two.player_cards = p_two_card
    p_three = Player(3)
    p_three.player_cards = p_three_card

    g = Game(3)
    g.players = [p_one, p_two, p_three]

    assert g.game() == 2

    assert len(g.players) == 1
    assert g.players[0].card == None

    print(test_game_win_one.__name__, ' +')


def test_play():
    p_one_card = [(2, 'T')]
    p_two_card = [(10, 'T')]
    p_three_card = [(3, 'T')]

    p_one = Player(1)
    p_one.player_cards = p_one_card
    p_two = Player(2)
    p_two.player_cards = p_two_card
    p_three = Player(3)
    p_three.player_cards = p_three_card

    g = Game(3)
    g.players = [p_one, p_two, p_three]

    assert g.play() == [2]

    assert g.round == 1

    assert g.course_of_game == [2]

    print(test_play.__name__, ' +')


def test_play_none():
    p_one_card = [(3, 'T')]
    p_two_card = [(3, 'T')]
    p_three_card = [(3, 'T')]

    p_one = Player(1)
    p_one.player_cards = p_one_card
    p_two = Player(2)
    p_two.player_cards = p_two_card
    p_three = Player(3)
    p_three.player_cards = p_three_card

    g = Game(3)
    g.players = [p_one, p_two, p_three]

    assert g.play() == []

    assert g.round == 1

    assert g.course_of_game == [-1]

    assert len(g.players) == 0

    print(test_play_none.__name__, ' +')


def own_test():
    def create_players():

        p_one_card = [('A', 'D'), (2, 'H'), (5, 'S'), (6, 'C'), ('J', 'D'), (3, 'D'), (8, 'D')]
        p_two_card = [(4, 'H'), (7, 'C'), (4, 'S'), ('K', 'S'), (10, 'S'), (10, 'D')]
        p_three_card = [('A', 'C')]

        p_one = Player(1)
        p_one.player_cards = p_one_card
        p_two = Player(2)
        p_two.player_cards = p_two_card
        p_three = Player(3)
        p_three.player_cards = p_three_card
        return [p_one, p_two, p_three]

    def return_winer(game):
        winner, more_winners = g.show_winner()
        if not more_winners:
            won = str(winner.id_player)
        else:
            won = ";".join(str(p.id_player) for p in winner)

        return won

    # 1 round play
    g = Game(3, limit=2)
    g.players = create_players()
    # g.print_players_and_cards()
    g.play()

    # who won
    assert return_winer(g) == '1'
    print(own_test.__name__, ':')
    print('\tOne round = one winner +')

    # 10 round play
    g = Game(3, limit=10)
    g.players = create_players()
    g.play()

    # who won
    assert return_winer(g) == '1;2'
    print('\tTen round = two winners +')


def main():
    test_correct_amt_cards()
    test_correct_deal_cards()
    test_war_one_winner_simple()
    test_double_war_one_winner()
    test_war_none_of_players_won()
    test_take_cards()
    test_battle_one_win()
    test_battle_none_win()
    test_game_win_one()
    test_play()
    test_play_none()
    own_test()


if __name__ == '__main__':
    main()
