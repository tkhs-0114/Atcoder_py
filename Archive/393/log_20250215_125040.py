N = int(input())
S = list(map(int, list(input())))
min_ = N
max_ = 0
for i in range(N):
    if S[i] == 1:
        min_ = min(min_, i)
        max_ = max(i, max_)
# print(min_, max_)
G = []
for i in range(min_, max_+1):
    if S[i] == 0:
        G.append(i)
if len(G) == 0:
    print(0)
    exit()
c = G[len(G)//2]
# print(c)
out = 0
cnt = 1
cntL = 0
for i in range(c, -1, -1):
    if S[i] == 1:
        cntL += 1
        out += abs(c-i) - cnt
        cnt += 1
cnt = 1
cntR = 0
for i in range(c, N):
    if S[i] == 1:
        cntR += 1
        out += abs(c-i) - cnt
        cnt += 1
print(out + min(cntL, cntR))