import json
import time
from statsmodels.tsa.ar_model import AutoReg
from matplotlib import pyplot


def read_file(path):
    """
    Read data with file.
    :param name_file: name file
    :return:
    """
    path = f'{path}'
    data = None
    with open(path) as f:
        data = json.load(f)
    return data

def number_of_victories(data, amt_player, info=False):
    victories = {}
    print(data)
    for i in range(1,amt_player+1):
        try:
            amt_victories = data[str(i)]
        except KeyError:
            victories[i] = 0
            continue

        victories[i] = amt_victories

    if info:
        print("Stats of victories:")
        for i in victories.keys():
            print(f"\t\t{i: <4} -> {victories[i]}")

    return victories

def answer_yes_or_no():

    while True:
        a = input().lower()
        if a == 'y':    return 'yes'
        elif a=='n':    return 'no'
        elif a == 'q':  return 'q'

def show_plot(data):

    pyplot.plot(data[-100:])
    pyplot.show()

def predictions_ar(data):
    # analisys game

    extent = len(data) - 20
    train, test = data[:extent], data[extent:]
    # # train autoregresion
    model = AutoReg(train, lags=29)
    model_fit = model.fit()
    print('Coefficients: %s' % model_fit.params)
    # make predictions
    predictions = model_fit.predict(start=len(train), end=len(train) + len(test) - 1, dynamic=False)
    print(len(predictions), len(test))
    x = 0
    for p, t in zip(predictions, test):
        print(f"Predicted: {round(p): >5}, excepted: {t: >5}")
        if round(p) == t:
            x += 1
    print('Amount good predict ', x)
    time.sleep(5)
    #plot
    pyplot.title("The Predict 20 games (red)")
    pyplot.xlabel("Games")
    pyplot.ylabel('ID players')

    pyplot.plot(test)
    pyplot.plot(predictions, color='red')
    pyplot.show()

def create_stats(data, amt_player,info=False):

    # numbers of victories
    victories = number_of_victories(data['win_stats'], amt_player, info=info)

    # min time
    print(f"\nMinimal time of one round in 1000 games\t{data['min_time']} s")

    #max time
    print(f"\nMaximum time of one round in 1000 games\t{round(data['max_time'],5)} s")

    # avg time
    print(f"\nAverage time rounds \t{round(data['all_time'], 5)} s")

    # min rounds
    print(f"\nMinimum rounds in 1000 games \t{data['min_round']}")

    #max round
    print(f"\nMaximum rounds in 1000 games \t {data['max_round']}")

    # All rounds
    print(f"\nAll rounds in 1000 games \t{data['all_rounds']}")

    #avg rounds
    print(f"\nAverage rounds in 1000 games\t{data['all_rounds']//1000}")

    # more winner
    print(f"\nMore winner in one game\t{data['more_winner']}")

    #
    print("\nDo you want see graph with last 100 games? [y/n]")
    if answer_yes_or_no() == 'yes':
        #plot
        show_plot(data['winner'])
    # AR
    predictions_ar(data['winner'])



