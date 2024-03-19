n = int(input())
dp = [0]*(n+1)


for i in range(2, n+1):
    # dp : 1을 뺏을 때의 횟수(연산 3번 사용)
    dp[i] = dp[i-1]+1
    if(i % 2 == 0):
        # 연산2, 연산3 크기 비교
        dp[i] = min(dp[i], dp[i//2]+1)
    if(i % 3 == 0):
        # 연산1, 연산3 크기 비교
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[n])
