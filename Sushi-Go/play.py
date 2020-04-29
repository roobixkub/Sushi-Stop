# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 01:40:09 2020

@author: Nate
"""

import random
from deck import deck
from scoring import Scoring
#import hands


def player_reset():
    player_set_up = []
    player_count = range(0, players)
    player_num = 1
    for player in player_count:
        pile = []
        wasabi = False
        chopsticks = False
        player_state = [player_num, pile, wasabi, chopsticks]
        player_set_up.append(player_state)
        player_num += 1
    return player_set_up

def player_names():
    player_num = 1
    for player in player_set_up:
        player_name = input("Player {}'s name? ".format(player_num))
        player[0] = player_name
        player_num += 1
    return player_set_up

def deal_hand():
    for player in player_set_up:
        hand = []
        while len(hand) < hand_size:
            hand.append(game_deck.pop())
        return hand

def maki_score():
    maki_count_1st = 0
    maki_score_1st = None
    maki_count_2nd = 0
    maki_score_2nd = None
    maki_score_1st_tie = []
    maki_score_2nd_tie = []
    for player in player_set_up:
        points = Scoring(player[1])
        maki_count = points.total()[1]
        if maki_count >= maki_count_1st:
            if maki_count > maki_count_1st:
                if maki_count_1st >= maki_count_2nd:
                    if maki_count_1st > maki_count_2nd:
                        maki_count_2nd = maki_count_1st
                        maki_score_2nd = maki_score_1st
                        maki_score_2nd_tie = maki_score_1st_tie
                    elif maki_count == maki_count_2nd:
                        maki_score_2nd_tie.append(maki_score_1st)
                        maki_score_2nd_tie.append(maki_score_1st_tie)
                maki_count_1st = maki_count
                maki_score_1st = player[0]
                maki_score_1st_tie = [player[0]]
            elif maki_count == maki_count_1st:
                maki_score_1st_tie.append(player[0])
                maki_score_1st = None
        elif maki_count >= maki_count_2nd:
            if maki_count > maki_count_2nd:
                maki_count_2nd = maki_count
                maki_score_2nd = player[0]
                maki_score_2nd_tie = [player[0]]
            elif maki_count == maki_count_2nd:
                maki_score_2nd_tie.append(player[0])
                maki_score_2nd = None
    maki_scores = (maki_score_1st, maki_score_2nd, maki_score_1st_tie, maki_score_2nd_tie)
    return maki_scores

def score_it():
    for player in player_set_up:
        points = Scoring(player[1])
        total_score = points.total()[0]
        pudding_count = points.total()[2]
        if player[0] == maki_scores[0]:
            total_score += 6
        elif player[0] == maki_scores[1]:
            total_score += 3
        elif player[0] in maki_scores[2]:
            total_score += int(6 / len(maki_scores[2]))
        elif player[0] in maki_scores[3]:
            total_score += int(3 / len(maki_scores[3]))    
        print(player[0], ': {} points and {} puddings'.format(total_score, pudding_count))
        print(player[1])
    return (total_score, pudding_count)


valid = False
while not valid:
    try:
        players = int(input('How many players(2-5)? '))
        if players < 2 or players > 5:
            raise ValueError('Sushi-Go can only be played with 2 to 5 players')
        valid = True
    except ValueError as ve:
        print(ve)

if players == 2:
    hand_size = 10
elif players == 3:
    hand_size = 9
elif players == 4:
    hand_size = 8
elif players == 5:
    hand_size = 7

game_deck = list(deck)
shuffled_deck = random.shuffle(game_deck)
player_set_up = player_reset()
player_set_up = player_names()
player_set_up[0][1] = deal_hand()
player_set_up[1][1] = deal_hand()
maki_scores = maki_score()
player_score = score_it()
