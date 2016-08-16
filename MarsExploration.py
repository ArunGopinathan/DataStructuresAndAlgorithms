#!/bin/python3

import sys


S = input().strip()
length = int(len(S)/3)
expected = "SOS"*length
diff = [i for i in range(len(expected)) if S[i]!=expected[i]]
print(len(diff))