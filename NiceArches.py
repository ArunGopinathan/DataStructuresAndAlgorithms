import sys

count = 0
n = int(sys.stdin.readline().strip())
string = ""
for _ in range(n):
    arr = []
    string = sys.stdin.readline().strip()
    if len(string) % 2 == 0:
        if string == string[::-1]:
            count += 1
        else:
            for i in range(len(string)):
                if len(arr) == 0:
                    arr.append(string[i])
                else:
                    if arr[-1] == string[i]:
                        arr.pop()
                    else:
                        arr.append(string[i])
            if len(arr) == 0:
                count += 1
print(count)
