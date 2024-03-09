# n   i
# 1   0
# 1   1
# 1   2

# 2   3
# 2   4

# 3   5   (0 + 4)

# 4   6   (1 + 5)

# 5   7   (2 + 6)

# 7   8   (3 + 7)

# 9   9   (4 + 8)

# 12  10  (5 + 9)

# 16  11  (6 + 10)

T = int(input())
arr = [1, 1, 1, 2, 2]*(100)
for i in range(T):
    N = int(input())
    for i in range(4, N+1):
        arr[i+1] = arr[i-4]+arr[i]
    print(arr[N-1])
