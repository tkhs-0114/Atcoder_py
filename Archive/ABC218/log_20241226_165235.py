N = int(input())
P = [list(map(int, input().split(" "))) for _ in range(N)]
import itertools
cnt = 0
for p in itertools.combinations(P, 4):
    xmin = min(p[0][0], p[1][0], p[2][0], p[3][0])
    xmax = max(p[0][0], p[1][0], p[2][0], p[3][0])
    ymin = min(p[0][1], p[1][1], p[2][1], p[3][1])
    ymax = max(p[0][1], p[1][1], p[2][1], p[3][1])
    xminc = 0
    xmaxc = 0
    yminc = 0
    ymaxc = 0
    for i in p:
        if xmin == i[0]:
            xminc += 1
        if xmax == i[0]:
            xmaxc += 1
        if ymin == i[1]:
            yminc += 1
        if ymax == i[1]:
            ymaxc += 1
        if xminc == 2 and xmaxc == 2 and yminc == 2 and ymaxc == 2:
            cnt += 1
print(cnt)