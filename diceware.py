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
import random
import sys
import pdb

wordlist = 'wordlist.txt'
# This is the number of rolls (or words) you want for your password
# the highest, the better. 
rolls = 5

numbers = [[] for i in range(rolls)]
lists = 0
count = 0
ranges = rolls

while rolls > 0:
    while count < 5:
        n = random.randint(1,6)
        numbers[lists].append(n)
        count += 1
    lists += 1
    count = 0
    rolls -= 1

print '\nSequences for Diceware password:\n'
#print numbers

for i in range(ranges):
    print 'Sequence', i, ': ', numbers[i]

for number in range(ranges):
    numbers[number] = map(str, numbers[number])
    numbers[number] = ''.join(numbers[number])
#    print numbers

sys.stdout.write('\nPassword: ')
f = open(wordlist, 'r')
for line in f:
    num = line.split()
    for i in range(ranges):
        if num[0] == numbers[i]:
            sys.stdout.write(num[1])

print '\n'