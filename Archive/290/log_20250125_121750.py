H, W = map(int, input().split(" "))
M = [[] for _ in range(H)]
for i in range(H):
    M[i] = list(input())
U = H
D = 0
L = W
R = 0
for i in range(H):
    for j in range(W):
        if M[i][j] == "#":
            U = min(U, i)
            D = max(D, i)
            L = min(L, j)
            R = max(R, j)
for i in range(U, D + 1):
    for j in range(L, R + 1):
        if M[i][j] == ".":
            print("No")
            exit()
print("Yes")
