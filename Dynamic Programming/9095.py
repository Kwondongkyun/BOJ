t=int(input())
n=[0]*t
r=[0]*11

r[0]=1
r[1]=2
r[2]=4
for j in range(3, 11):
    r[j]=r[j-3]+r[j-2]+r[j-1]

# 테스트 케이스 입력(개수 : t개)
for i in range(t):
    n[i]=int(input())

for i in range(len(n)):
    print(r[n[i]-1])