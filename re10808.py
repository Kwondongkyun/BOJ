li = [0]*26
for c in input():
    li[ord(c)-ord('a')] += 1
print(*li)
