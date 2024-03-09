N, M = map(int, input().split())
arr = [int(x) for x in input().split()]

for x in range(M):
    sum = 0
    i, j = map(int, input().split())
    for y in range(i-1, j):
        sum = sum + arr[y]
    print(sum)
