N = int(input())
S = []
for _ in range(N):
    A, B = map(int, input().split(" "))
    S.append(tuple((A, 1)))
    S.append(tuple((A+B, -1)))
S.sort()

C = [0] * (N + 1)
cnt = 0
for i in range(len(S) - 1):
    cnt += S[i][1]
    C[cnt] += S[i+1][0] - S[i][0]
for i in range(1, N+1):
    print(C[i], end=" ")
print()
