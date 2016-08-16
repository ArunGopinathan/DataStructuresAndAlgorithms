n = int(input())
table = {}
for _ in range(n):
    line = input()
    if ' ' in line:
        roll, name = line.split(' ')
        table[int(roll)] = name
t = int(input())
for _ in range(t):
    print(table[int(input())])
