#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright (c) 2010 Oscar Carballal Prego <info@oscarcp.com>
#
# Distributed under terms of the MIT license.

# WARNING: Pyce is meant to be used in non critical environments. Do not use
#          the generated passwords in your company or in critical environments!

import random
import sys

wordlist = 'wordlist.txt'
rolls = 5 # We assume that we use 5 dies in each roll
numbers = [[] for i in range(5)] # Store numbers in a list of lists
lists = 0 
count = 0

while rolls > 0:
    while count < 5:
        n = random.randint(1,6)
        numbers[lists].append(n)
        count += 1
    lists += 1
    count = 0
    rolls -= 1

print '\nSequences for Diceware password:\n'

for i in range(5):
    print 'Sequence', i, ': ' + str(numbers[i])

for number in range(5):
    numbers[number] = map(str, numbers[number])
    numbers[number] = ''.join(numbers[number])
#    print numbers

sys.stdout.write('\nPassword: ')
f = open(wordlist, 'r')
for line in f:
    num = line.split()
    if any([num[0] == numbers[0], num[0] == numbers[1], num[0] == numbers[2],
            num[0] == numbers[3], num[0] == numbers[4]]):
        sys.stdout.write(num[1])

print '\n'