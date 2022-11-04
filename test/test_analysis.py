from analysis.analysis import number_of_victories

def test_number_of_victories():

    data = {
        8: 1,
        2: 50,
        6: 30,
        1:10
    }
    amt_player = 10

    victories = number_of_victories(data, amt_player)
    assert victories[1] == 10 and victories[10] == 0
    data = {}
    victories = number_of_victories(data, amt_player)
    assert victories[1] == 0 and victories[2] == 0

    print(f"{test_number_of_victories.__name__: <50}+")

def main():
    test_number_of_victories()
if __name__ == '__main__':
    main()