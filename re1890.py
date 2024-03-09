import sys
input = sys.stdin.readline

N = int(input().rstrip())

arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[0]*N for _ in range(N)]

DP[0][0] = 1

#   DP            arr
# 1 0 0 0       2 3 3 1
# 0 0 0 0       1 2 1 3
# 0 0 0 0       1 2 3 1
# 0 0 0 0       3 1 1 0

for i in range(N):
    for j in range(N):
        if DP[i][j] != 0 and arr[i][j] != 0:
            # 오른쪽 이동
            # 이동하면서 DP 배열에 1 삽입
            if j+arr[i][j] < N:
                DP[i][j+arr[i][j]] += DP[i][j]
            # 아래쪽 이동
            if i+arr[i][j] < N:
                DP[i+arr[i][j]][j] += DP[i][j]

# print(DP)
print(DP[N-1][N-1])
