N = int(input())
S = list(map(int, list(input())))
# print(S)
G = []
for i in range(N):
    if S[i] == 1:
        G.append(i)
print(G)
L = []
for i in range(len(G)-1):
    L.append(G[i+1]-G[i]-1)
print(L)
sumL = sum(L)
# print(sumL)
c = sumL//2
cnt =0
for i in range(len(L)):
    cnt += L[i]
    if cnt >= c:
        c = i
        break
# print(c)
out = N * N
H = [-1, 0 ,1]
for h in H:
    q = c + h
    cntL = 0
    cntR = 0
    for i in range(len(L)):
        if i < q:
            cntL *= 2
            cntL += L[i]
        elif i > q:
            cntR *= 2
            cntR += L[i]
    out = min(out, cntL + cntR + 2)
    print(q, out)
if out == N * N:
    out = 0
print(out)
