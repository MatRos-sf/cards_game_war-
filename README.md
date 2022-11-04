# War (card game)

## Table of contents
* [General info](#general-info)
* [Description](#description)
* [Data Analysis](#data-anlysis)
* [Setup](#setup)

## General info
The war is simple card game using a standard card deck. You don't need any skills to play it. You need only compare cards value.

I created simulation this game to check who win game And whether we can predict winner.

Repository consist:
* **sample** it's directory when we keep some data
* **test** it's directory when there are file with simple tests
* **war_game** it's a file with game simulation the war

## Description

In game I used own rules. But first if you want start game you should give amount players:

`g = Game(5)`

In this case I created game with 5 players. Extra variable is: 
* _limit = None_ You can set limit rounds. 
* _curse=True_ This variable protect us to play infinity. If value is True and we have 100 rounds the game delete one cards each players.
* _info=False_ If true we can see extra info with game.

Next step you have to set the game. Use commend:

`g.set_game()`

Now game create players, cards and deal cards. Last step you have to do:

`winner = g.play()`

You get array with players who survived. Be careful result is list of Players if you want more information e.g. id player you have to call it:

`winner[0].id_player`

Own rules. If two cards or more are equal value then is war. Rules war:
>If the two cards played are of equal value, then there is a "war".
> Both players place the next three cards face down and then another card face-up. 
> The owner of the higher face-up card wins the war and adds all the cards on the table to the bottom of their deck. 
> If the face-up cards are again equal then the battle repeats with another set of face-down/up cards. 
> This repeats until one player's face-up card is higher than their opponent's.

**the worst case** If war don't settle  all cards with round disappear.

####Extra Function

`g.show_winner()` -  The function show winner or winners who have the most cards. It return list of player and True(more than 1 winner)/ False (1 winner )

## Data Analysis

### sample
In this catalog are:
* _data_ - There're data with games
* _sample.py_ File who create data

#### **sample.py**

The most important things in this file is function main(). This function create:
1. `create_game()` Tworzę zwykłą gry  od 2 do 100 graczy. W każdej ilości gracze zagrają po 1000 gier 
np. 2 graczy x 1000 Gier, 3 graczy x 1000 gier ... . Po każdej rozgrywce (np. 2 graczy x 1000 Gier) zapisuje statystyki 
z rozegranych.

`
{
    "min_time": 0.0,
    "max_time": 0.048998355865478516,
    "all_time": 0.002890998840332031,
    "min_round": 38,
    "max_round": 2500,
    "all_rounds": 834330,
    "more_winner": 0,
    "winner": [
        1, 1 ... 2, 1,2],
    "win_stats": {
        "1": 557,
        "2": 443
    }
}
`


2. `create_game_fibbo()` Tworzy grę od 5 do 20 graczy oraz ustawia limit rund na gre według ciągu fibonacciego. 

#### **analysis\main_analysis.py**
It's a simple scripts where you can find: 
* Avg time and rounds in 1000 games
* min and max in 1000 games
* predicts last 20 games ( AutoReg )

## Setup

The requirements.txt have list all Python libraries. They will be installed using:

`pip install -r requirements.txt`

