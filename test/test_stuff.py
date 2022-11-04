from war_game import create_deck_of_cards, power_card

def test_create_deck_of_cards():
    # 52 cards
    cards = create_deck_of_cards()
    assert len(cards) == 52
    # 104 cards
    cards = create_deck_of_cards(2)
    assert len(cards) == 104
    # 520 cards
    cards = create_deck_of_cards(100)
    assert len(cards) == 5200
    print("Ok: ", test_create_deck_of_cards.__name__)


def main():
    test_create_deck_of_cards()


if __name__ == '__main__':
    main()
