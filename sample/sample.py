import time
import json
from war_game import Game, Player
from math import inf

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibo(n-1) + fibo(n-2)
    else:
        print("N must be large or equal 0")
        return
def create_game(amt_games=1000):

    # create game from 2 to 100 players
    winner = None
    list_winner = []
    min_time, min_round = inf, inf
    max_time, max_round = -inf, -inf
    all_time = 0
    all_rounds = 0
    more_winner = 0
    amt_games = amt_games

    for amt in range(2, 101):
        # play 1000 gammes
        for _ in range(amt_games):

            start_time = time.time()
            g = Game(amt)
            g.set_game()
            winner = g.play()
            complete_time = time.time() - start_time
            # time
            if min_time > complete_time:
                min_time = complete_time
            if max_time < complete_time:
                max_time = complete_time
            all_time += complete_time

            # rounds
            if min_round > g.round:
                min_round = g.round
            if max_round < g.round:
                max_round = g.round
            all_rounds += g.round

            # add winner
            if len(winner) == 1:
                list_winner.append(winner[0])
            else:
                list_winner += winner
                more_winner += 1

        stats = create_stats(list_winner, min_time, max_time, all_time,
                             min_round, max_round, all_rounds, more_winner, amt_games)

        path = f"data\\classic\\{amt_games}_games_{amt}_players.json"
        write_to_json_file(path, stats)

        print(f"Done: Game with {amt} players.")

        # set default setting
        list_winner = []
        min_time, min_round = inf, inf
        max_time, max_round = -inf, -inf
        all_time = 0
        all_rounds = 0
        more_winner = 0

def create_game_fibbo(max_ammt_players, amt_games=1000):
    winner = None
    list_winner = []
    min_time, min_round = inf, inf
    max_time, max_round = -inf, -inf
    all_time = 0
    all_rounds = 0
    more_winner = 0
    all_stats = {}

    # test fibbo f(5) to f(19)
    for no_fibo in range(5, 20):
        limit_round = fibo(no_fibo)
        for amt in range(2, max_ammt_players+1):
            # play 1000 gammes
            for _ in range(amt_games):

                start_time = time.time()
                g = Game(amt, limit=limit_round, curse=False)
                g.set_game()
                winner = g.play()
                complete_time = time.time() - start_time
                # time
                if min_time > complete_time:
                    min_time = complete_time
                if max_time < complete_time:
                    max_time = complete_time
                all_time += complete_time

                # rounds
                if min_round > g.round:
                    min_round = g.round
                if max_round < g.round:
                    max_round = g.round
                all_rounds += g.round

                # add winner
                won, more_won = g.show_winner()
                if more_won:
                    list_winner.append([p.id_player for p in won])
                    more_winner += 1
                else:
                    list_winner.append(won.id_player)

            stats = create_stats(list_winner, min_time, max_time, all_time,
                                 min_round, max_round, all_rounds, more_winner, no_fibo)
            all_stats[amt] = stats

            # set default setting
            list_winner = []
            min_time, min_round = inf, inf
            max_time, max_round = -inf, -inf
            all_time = 0
            all_rounds = 0
            more_winner = 0

        path = f"data\\fibbo\\F{no_fibo}_fibbo_games.json"

        write_to_json_file(path, all_stats)
        print(f"Done: Fibbo({no_fibo})")



def create_stats(
        winner, min_time, max_time, all_time, min_round, max_round, all_rounds, more_winner, amt_game
):
    # check if all_timme == 0 than avg 0. We can't divide 0
    avg_time = 0
    if all_time == 0:   avg_time = 0
    else:   avg_time = all_time/amt_game

    stats = {
        'min_time': min_time,
        'max_time': max_time,
        'all_time': avg_time,
        'min_round': min_round,
        'max_round': max_round,
        'all_rounds': all_rounds,
        'more_winner': more_winner,
        'winner': winner,
    }

    if more_winner == 0:
        from collections import Counter
        win_stats = Counter(winner)
        stats['win_stats'] = win_stats

    return stats

def write_to_json_file(path, stats):
    # convert dic to json
    json_stats = json.dumps(stats, indent=4)

    # write to n_games_n_players.json
    with open(path, 'w') as f:
        f.write(json_stats)

def main():
    print("Start: \n")
    print(create_game.__name__, '\n')
    s = time.time()
    create_game()
    print("End ", create_game.__name__, ' time: ', time.time() - s, ' s')

    print(create_game_fibbo.__name__, '\n')
    s = time.time()
    create_game_fibbo(10)
    print("End ", create_game_fibbo.__name__, ' time: ', time.time() - s, ' s')


if __name__ == '__main__':
    main()












