N = int(input())
P = [list(map(int, input().split(" "))) for i in range(N)]
P = set(map(tuple, P))
import itertools
cnt = 0
for l in itertools.permutations(P, 2):
    if l[0][0] < l[1][0] and l[0][1] < l[1][1]:
        RU = [l[1][0], l[0][1]]
        LD = [l[0][0], l[1][1]]
        if tuple(RU) in P and tuple(LD) in P:
            cnt += 1
print(cnt)
