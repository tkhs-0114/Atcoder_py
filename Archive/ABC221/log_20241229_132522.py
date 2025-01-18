N = list(map(int, list(input())))
M = 0
for i in range((2 ** len(N)) // 2):
    A = []
    B = []
    for j in range(len(N)):
        if ((i >> j) & 1):
            A.append(N[j])
        else:
            B.append(N[j])
    A.sort()
    B.sort()
    a = 0
    b = 0
    for i in range(len(A)):
        a += 10**i * A[i]
    for i in range(len(B)):
        b += 10**i * B[i]
    M = max(M, a * b)
print(M)
    