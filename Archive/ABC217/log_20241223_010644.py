import bisect
L, Q = map(int , input().split(" "))
A = [0, L]
for i in range(Q):
    c, x = map(int, input().split(" "))
    j = bisect.bisect(A, x)
    if c == 1:
        A.insert(j, x)
        # ↑こいつがO(n)の犯人
    else:
        print(A[j] - A[j-1])