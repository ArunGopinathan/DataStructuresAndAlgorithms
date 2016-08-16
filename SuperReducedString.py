from collections import deque

word, result = input(), deque()

for ch in word:
    if result and result[-1] == ch:
        result.pop()
    else:
        result.append(ch)

print(*result if result else 'Empty String', sep='')