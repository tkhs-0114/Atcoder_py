N = int(input())
X, Y = map(int, input().split(" "))
L = [list(map(int, input().split(" "))) for _ in range(N)]
cnt = [0, 0]
for l in L:
    cnt[0] += l[0]
    cnt[1] += l[1]
if cnt[0] < X or cnt[1] < Y:
    print(-1)
    exit()
out = N
import itertools
for l in itertools.permutations(L):
    cnt = [0, 0]
    for i in range(N):
        cnt[0] += l[i][0]
        cnt[1] += l[i][1]
        if cnt[0] >= X and cnt[1] >= Y:
            out = min(out, i)
            break
print(out+1)