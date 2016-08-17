t = int(input())
for _ in range(t):
    n, pid = map(int, input().strip().split(' '))
    stack = [pid]
    for _ in range(n):
        line = input().strip()
        if ' ' in line:  # means p id type
            p, pid = line.split(' ')
            stack.append(int(pid))
        else:
            prevpid = stack.pop()
            stack.insert(len(stack)-1, prevpid)
    print('Player '+str(stack.pop()))
