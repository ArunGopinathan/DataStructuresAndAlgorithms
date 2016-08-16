#!/bin/python3

import sys

n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]
minlist = []
for i in range(len(A)):
    for j in range(i, len(A)):
        if i != j:
            if A[i] == A[j]:
                minlist.append(abs(i - j))

print(min(minlist) if len(minlist) > 0 else "-1")
