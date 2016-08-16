input()
binary = list(input())
length = len(binary)
i = 0
count = 0
while i + 2 <= length - 1:
    if binary[i] == '0' and binary[i + 1] == '1' and binary[i + 2] == '0':
        count += 1
        i += 3
    else:
        i += 1
print(count)
