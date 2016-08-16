t = int(input())
stack = []
for _ in range(t):
    line = input()
    if ' ' in line:
        qtype, cost = map(int, line.split(' '))
        stack.append(cost)
    else:  # means qtype is 1
        if len(stack) == 0:
            print("No Food")
        else:
            print(stack.pop())
