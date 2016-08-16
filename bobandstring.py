t = int(input())
for _ in range(t):
    team = {}
    n, k = map(int, input().split(' '))
    for _ in range(n):
        name = input()
        team[len(name)] = team.get(len(name), 0) + 1
    pos = True
    for i in team:
        if team[i] % k != 0:
            print('Not possible')
            pos = False
            break
    if pos:
        print("Possible")

