#!/bin/python3

import sys

t = int(input().strip())
prev = -1
prev_i = -1
current = 3
current_i = 1
if t == current_i:
    print(current)
else:
    while current_i < t:
        prev = current
        prev_i = current_i
        current = prev * 2
        current_i = current - 2
    if current_i == t:
        print(current)
    else:
        print(prev - (t - prev_i))
