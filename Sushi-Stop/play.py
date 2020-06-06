# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 01:40:09 2020

@author: Nate
"""

import random
from deck import deck
from scoring import Scoring
from hands import Hands


def player_reset():
    player_set_up = []
    player_count = range(0, players)
    player_num = 1
    for player in player_count:
        pile = []
        wasabi = 0
        chopsticks = 0
        player_name = input("Player {}'s name? ".format(player_num))
        hand = []
        puddings = 0
        score = 0
        player_state = [player_num, player_name, hand, pile, wasabi, chopsticks, puddings, score]
        player_set_up.append(player_state)
        player_num += 1
    return player_set_up

def deal_hand():
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
        points = Scoring(player[3])
        maki_count = points.total()[1]
        if maki_count >= maki_count_1st:
            if maki_count > maki_count_1st:
                if maki_count_1st >= maki_count_2nd and maki_count_1st != 0:
                    if maki_count_1st > maki_count_2nd:
                        maki_count_2nd = maki_count_1st
                        maki_score_2nd = maki_score_1st
                        maki_score_2nd_tie = maki_score_1st_tie
                    elif maki_count == maki_count_2nd:
                        maki_score_2nd_tie.append(maki_score_1st)
                        maki_score_2nd_tie.append(maki_score_1st_tie)
                maki_count_1st = maki_count
                maki_score_1st = player[1]
                maki_score_1st_tie = [player[1]]
            elif maki_count == maki_count_1st:
                maki_score_1st_tie.append(player[1])
                maki_score_1st = None
        elif maki_count >= maki_count_2nd:
            if maki_count > maki_count_2nd:
                maki_count_2nd = maki_count
                maki_score_2nd = player[1]
                maki_score_2nd_tie = [player[1]]
            elif maki_count == maki_count_2nd:
                maki_score_2nd_tie.append(player[1])
                maki_score_2nd = None
    maki_scores = (maki_score_1st, maki_score_2nd, maki_score_1st_tie, maki_score_2nd_tie)
    return maki_scores

def pudding_score():
    pudding_top = 1
    pudding_bottom = 0
    pudding_champ_tie = []
    pudding_loser_tie = []
    for player in player_set_up:
        if player[6] >= pudding_top:
            if player[6] > pudding_top:
                if pudding_loser_tie == []:
                    pudding_bottom = pudding_top
                    pudding_loser_tie = pudding_champ_tie
                pudding_top = player[6]
                pudding_champ_tie = [player[1]]
            elif player[6] == pudding_top:
                pudding_champ_tie.append(player[1])
        elif player[6] == pudding_bottom:
            pudding_loser_tie.append(player[1])
        elif player[6] < pudding_top and pudding_loser_tie == []:
            pudding_loser_tie.append(player[1])
        elif player[6] < pudding_bottom:
            pudding_bottom = player[6]
            pudding_loser_tie = [player[1]]
    for player in player_set_up:
        if player[1] in pudding_champ_tie:
            player[7] += int(6 / len(pudding_champ_tie))
        elif player[1] in pudding_loser_tie:
            player[7] -= int(6 / len(pudding_loser_tie))

def score_it():
    for player in player_set_up:
        points = Scoring(player[3])
        total_score = points.total()[0]
        player[6] += points.total()[2]
        if player[1] == maki_scores[0]:
            total_score += 6
        elif player[1] == maki_scores[1]:
            total_score += 3
        elif player[1] in maki_scores[2]:
            total_score += int(6 / len(maki_scores[2]))
        elif player[1] in maki_scores[3]:
            total_score += int(3 / len(maki_scores[3]))
        player[7] += total_score
    return

valid = False
while not valid:
    try:
        players = int(input('How many players(2-5)? '))
        if players < 2 or players > 5:
            raise ValueError('Sushi-Stop can only be played with 2 to 5 players')
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

turn = 1
while turn < 4:
    for player in player_set_up:
        player[2] = deal_hand()
        player[3] = []
        player[4] = 0
        player[5] = 0
    test = Hands(player_set_up, turn)
    test.play()
    maki_scores = maki_score()
    total_scores = score_it()
    turn += 1

pudding_score()
print("\n\n\nFinal Score: \n")
for player in player_set_up:
    print("{}: {}".format(player[1], player[7]))
