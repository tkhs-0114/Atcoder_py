def loop(s):
    while 1:
        for i in range(len(s)):
            if s[i][0] == '#':
                return
        for i in range(len(s)):
            for j in range(1, len(s[i])):
                s[i][j-1] = s[i][j]
                if j == len(s[i])-1:
                    s[i][j] = '.'
def loop2(s):
    while 1:
        for i in range(len(s)):
            if s[0][i] == '#':
                return
        for i in range(1, len(s)):
            for j in range(len(s[i])):
                s[i-1][j] = s[i][j]
                if i == len(s)-1:
                    s[i][j] = '.'


import copy
N = int(input())
S = []
T = []
for i in range(N):
    S.append(list(input()))
for i in range(N):
    T.append(list(input()))

loop(S)
loop2(S)

t = copy.deepcopy(T)
loop(t)
loop2(t)
if S == t:
    print("Yes")
    exit()

t = [["." for i in range(N)] for j in range(N)]
for Y in range(N):
    for X in range(N):
        t[Y][N - X - 1] = T[X][Y]
loop(t)
loop2(t)
if S == t:
    print("Yes")
    exit()

t = [["." for i in range(N)] for j in range(N)]
for Y in range(N):
    for X in range(N):
        t[N - X - 1][N - Y - 1] = T[X][Y]
loop(t)
loop2(t)
if S == t:
    print("Yes")
    exit()

t = [["." for i in range(N)] for j in range(N)]
for Y in range(N):
    for X in range(N):
        t[N - Y - 1][X] = T[X][Y]
loop(t)
loop2(t)
if S == t:
    print("Yes")
    exit()

print("No")