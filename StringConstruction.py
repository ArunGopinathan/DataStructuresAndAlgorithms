#!/bin/python3

import sys

n = int(input().strip())

for a0 in range(n):
    table = {}
    word = list(input().strip())
    for c in word:
        table[c] = table.get(c, 0) + 1
    print(len(table))
