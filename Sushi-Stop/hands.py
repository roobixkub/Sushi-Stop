# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 00:09:46 2020

@author: Nate
"""

class Hands:

    def __init__(self, player_set_up, turn):
        self.player_set_up = player_set_up
        self.turn = turn

    def display(self, player):
        print("\n\n\n\nPlayer {}, {}. Round {}. \nTotal points: {}, Total puddings: {}, Wasabi: {}, Chopsticks: {}\nCards in Hand:".format(self.player[0], self.player[1], self.turn, self.player[7], self.player[6], self.player[4], self.player[5]))
        for i, card in enumerate(self.player[2], 1):
            print(i, '. ' + card)
        print("\nCards in pile:\n")
        for i, card in enumerate(self.player[3], 1):
            print(i, '. ' + card)

    def play(self):
        while len(self.player_set_up[0][2]) > 0:
            for self.player in self.player_set_up:
                wasabi_tick = 0
                self.display(self.player)
                if self.player[5] > 0:
                    chopsticks = input("Would you like to use a chopsticks card? (Y/N) ")
                    if chopsticks.upper() == 'Y':
                        cards_1 = int(input("What is the number of the first card you would like to add to your pile? "))
                        if self.player[4] > 0 and 'nigiri' in self.player[2][cards_1 - 1]:
                            wasabi_count = 1
                            wasabi_card = 0
                            while wasabi_count == 1:
                                for _ in self.player[3]:
                                    if 'wasabi' in _:
                                        self.player[2][cards_1 - 1] += '_wasabi'
                                        self.player[3].pop(wasabi_card)
                                        wasabi_count = 0
                                    wasabi_card += 1
                            self.player[4] -= 1
                        elif self.player[2][cards_1 - 1] == 'wasabi':
                            wasabi_tick += 1
                        elif self.player[2][cards_1 - 1] == 'chopsticks':
                            self.player[5] += 1
                        self.player[3].append(self.player[2].pop(cards_1 - 1))
                        self.display(self.player)
                        cards_2 = int(input("What is the number of the second card you would like to add to your pile? "))
                        if self.player[4] > 0 and 'nigiri' in self.player[2][cards_2 - 1]:
                            wasabi_count = 1
                            wasabi_card = 0
                            while wasabi_count == 1:
                                for _ in self.player[3]:
                                    if 'wasabi' in _:
                                        self.player[2][cards_2 - 1] += '_wasabi'
                                        self.player[3].pop(wasabi_card)
                                        wasabi_count = 0
                                    wasabi_card += 1
                            self.player[4] -= 1
                        elif self.player[2][cards_2 - 1] == 'wasabi':
                            wasabi_tick += 1
                        elif self.player[2][cards_2 - 1] == 'chopsticks':
                            self.player[5] += 1
                        self.player[3].append(self.player[2].pop(cards_2 - 1))
                        self.player[2].append('chopsticks')
                        chopsticks_count = 1
                        chopsticks_card = 0
                        while chopsticks_count == 1:
                            for _ in self.player[3]:
                                if 'chopsticks' in _:
                                    self.player[3].pop(chopsticks_card)
                                    chopsticks_count = 0
                                chopsticks_card += 1
                        self.player[5] -= 1
                    else:
                        cards_1 = int(input("What is the number of the card you would like to add to your pile? "))
                        if self.player[4] > 0 and 'nigiri' in self.player[2][cards_1 - 1]:
                            wasabi_count = 1
                            wasabi_card = 0
                            while wasabi_count == 1:
                                for _ in self.player[3]:
                                    if 'wasabi' in _:
                                        self.player[2][cards_1 - 1] += '_wasabi'
                                        self.player[3].pop(wasabi_card)
                                        wasabi_count = 0
                                    wasabi_card += 1
                            self.player[4] -= 1
                        elif self.player[2][cards_1 - 1] == 'wasabi':
                            wasabi_tick += 1
                        elif self.player[2][cards_1 - 1] == 'chopsticks':
                            self.player[5] += 1
                        self.player[3].append(self.player[2].pop(cards_1-1))
                else:
                    cards_1 = int(input("What is the number of the card you would like to add to your pile? "))
                    if self.player[4] > 0 and 'nigiri' in self.player[2][cards_1 - 1]:
                        wasabi_count = 1
                        wasabi_card = 0
                        while wasabi_count == 1:
                            for _ in self.player[3]:
                                if 'wasabi' in _:
                                    self.player[2][cards_1 - 1] += '_wasabi'
                                    self.player[3].pop(wasabi_card)
                                    wasabi_count = 0
                                wasabi_card += 1
                        self.player[4] -= 1
                    elif self.player[2][cards_1 - 1] == 'wasabi':
                        wasabi_tick += 1
                    elif self.player[2][cards_1 - 1] == 'chopsticks':
                        self.player[5] += 1
                    self.player[3].append(self.player[2].pop(cards_1-1))
                self.player[4] += wasabi_tick
            self.pass_hands()

    def pass_hands(self):
        pass_hand = []
        for self.player in self.player_set_up:
            pass_hand.append(self.player[2])
        pass_hand.append(pass_hand.pop(0))
        for self.player in self.player_set_up:
            self.player[2] = pass_hand[self.player[0] -1]

#use try to simplify error handling

#help doc

#quit game command

#make a webapp or GUI
