import sys

# 입력
N, K = map(int, input().split(" "))

# N의 약수 리스트 생성
X = []
for x in range(1, N + 1):
    if N % x == 0:
        X.append(x)

# K번째 약수 출력
if len(X) < K:
    print(-1)
else:
    print(X[K - 1])


