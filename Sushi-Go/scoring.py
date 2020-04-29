# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 00:10:08 2020

@author: Nate
"""

class Scoring:

    def __init__(self, hand):
        self.hand = hand

    def total(self):

        self.maki_count = 0
        for _ in self.hand:
            if _ == 'maki_1':
                self.maki_count += 1
            elif _ == 'maki_2':
                self.maki_count += 2
            elif _ == 'maki_3':
                self.maki_count += 3
        
        self.tempura_score = 0            
        self.tempura_count = 0
        for _ in self.hand:
            if _ == 'tempura':
                self.tempura_count += 1
                if self.tempura_count == 2:
                    self.tempura_score += 5
                    self.tempura_count = 0

        self.sashimi_score = 0
        self.sashimi_count = 0
        for _ in self.hand:
            if _ == 'sashimi':
                self.sashimi_count += 1
                if self.sashimi_count == 3:
                    self.sashimi_score += 10
                    self.sashimi_count = 0

        self.dumpling_score = 0
        self.dumpling_count = 0
        for _ in self.hand:
            if _ == 'dumpling':
                self.dumpling_count += 1
        if self.dumpling_count == 1:
            self.dumpling_score = 1
        if self.dumpling_count == 2:
            self.dumpling_score = 3
        if self.dumpling_count == 3:
            self.dumpling_score = 6
        if self.dumpling_count == 4:
            self.dumpling_score = 10
        if self.dumpling_count >= 5:
            self.dumpling_score = 15

        self.nigiri_score = 0
        for _ in self.hand:
            if _ == 'nigiri_squid':
                self.nigiri_score += 3
            if _ == 'nigiri_salmon':
                self.nigiri_score += 2
            if _ == 'nigiri_egg':
                self.nigiri_score += 1
            if _ == 'wasabi_nigiri_squid':
                self.nigiri_score += 9
            if _ == 'wasabi_nigiri_salmon':
                self.nigiri_score += 6
            if _ == 'wasabi_nigiri_egg':
                self.nigiri_score += 3

        self.pudding_count = 0
        for _ in self.hand:
            if _ == 'pudding':
                self.pudding_count += 1

        self.score = int(self.tempura_score) + int(self.sashimi_score) + int(self.dumpling_score) + int(self.nigiri_score)
        return (self.score, self.maki_count, self.pudding_count)
