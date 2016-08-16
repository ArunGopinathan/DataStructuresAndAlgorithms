string = list(input())
count = {}
sorted(string)
for item in string:
    count[ord(item)] = count.get(ord(item), 0) + 1
val = min([k for k in count if count[k] == max(count.values())])
print(chr(val), count[val])
