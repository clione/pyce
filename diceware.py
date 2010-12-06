#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Author: Oscar Carballal <oscar.carballal@gmail.com>
#
# Contributions: Arnold Reinhold <reinhold@world.std.com>

import random
import sys

wordlist = 'wordlist.txt'
# This is the number of rolls (or words) you want for your password
# the highest, the better. 
rolls = 5

numbers = [[] for i in range(rolls)]
lists = 0
count = 0
ranges = rolls

myrg = random.SystemRandom

while rolls > 0:
    while count < 5:
        n = myrg(random).randint(1,6)
        numbers[lists].append(n)
        count += 1
    lists += 1
    count = 0
    rolls -= 1

print '\nSequences for Diceware password:\n'

for i in range(ranges):
    print 'Sequence', i, ':', numbers[i]

for number in range(ranges):
    numbers[number] = map(str, numbers[number])
    numbers[number] = ''.join(numbers[number])

sys.stdout.write('\nPassword: ')
f = open(wordlist, 'r')
for line in f:
    num = line.split()
    for i in range(ranges):
        if num[0] == numbers[i]:
            sys.stdout.write(num[1])

print '\n'
