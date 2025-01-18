X = list(input())
N = int(input())
S = [list(input()) for _ in range(N)]
import copy
Sl = copy.deepcopy(S)
for i in range(len(S)):
    num = 0
    for j in range(len(S[i])):
        for k in range(len(X)):
            if S[i][j] == X[k]:
                S[i][j] = k
L = sorted(S)
for l in L:
    for i in range(len(S)):
        if l == S[i]:
            print("".join(Sl[i]))