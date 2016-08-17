n = int(input())
for _ in range(n):
    word = input()
    if len(word) <= 1:
        print("No")
    else:
        table = {}
        found = False
        for a in word:
            if table.get(a, -1) != -1:
                print("Yes")
                found = True
                break
            else:
                table[a] = 1
        if not found:
            print("No")
