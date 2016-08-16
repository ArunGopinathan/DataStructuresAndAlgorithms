t = int(input())
for _ in range(t):
    n = int(input())
    boy = [int(x) - 1 for x in input().strip().split(' ')]
    girl = [int(x) - 1 for x in input().strip().split(' ')]
    boyCrush = {}
    girlCrush = {}
    # first check boy crush
    for i in range(0, len(boy)):
        if girl[boy[i]] != i:
            boyCrush[i] = boyCrush.get(i, 0) + 1  # boy gets beaten
    for i in range(0, len(girl)):
        if boy[girl[i]] != i:
            girlCrush[i] = girlCrush.get(i, 0) + 1  # boy gets beaten
    print(max(list(boyCrush.values()) + list(girlCrush.values())))
    print(boyCrush, girlCrush)
