import time
import os
from analysis import read_file, create_stats

PATH_CLASSIC = "..\\sample\\data\\classic\\"
PATH_FIBBO = "..\\sample\\data\\fibbo\\"

NAME_FILE_CLASIC = lambda x: f"1000_games_{x}_players.json"
NAME_FILE_FIBBO = lambda x: f"F{x}_fibbo_games.json"


def choice_what_analysis():

    ch = input()

    while True:
        if ch == '1':
            return 1
        elif ch == '2':
            return 2
        elif ch == 'q':
            return 'q'
        else:
            ch = input()

def choice_amount_players():

    while True:
        ch = input()
        try:
            ch = int(ch)
        except ValueError:
            continue
        if ch >= 2 and ch <= 100:
            break

    return ch

def create_path(catalog, amt_player):

    path = ''
    if catalog == 1:    path += PATH_CLASSIC + NAME_FILE_CLASIC(amt_player)
    elif catalog == 2:  path += PATH_FIBBO + NAME_FILE_FIBBO(amt_player)

    return path

def check_file_exist(path):

    isExist = os.path.exists(path)

    if not isExist:
        print("You must crate file with data. \nPlease run file sample\sample.py. ")
        return isExist
    return isExist



def main():

    hello_text = " Welcome to the simulation card game WAR analysis "
    print(f"{hello_text:*^200}")
    time.sleep(1)

    while True:
        #create path
        print("What do you want analysis?")
        print("[1] Classic simulations (1000 games)")
        print("[2] Fibbonaci simulations (n games)")
        catalog = choice_what_analysis()
        if catalog == 'q':  break
        if catalog == 2:
            print("Sorry it's not finish ;(")
            continue
        print("Choice amount players from 2 to 100: ")
        amt_players = choice_amount_players()
        path = create_path(catalog, amt_players)
        if not check_file_exist(path):      break

        data = read_file(path)
        # action
        print("{s:*^200}".format(s='    STATS    '))
        create_stats(data, amt_players, info=True)








if __name__ == '__main__':
    main()
