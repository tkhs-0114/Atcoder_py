N = int(input())
A = list(map(int, input().split(" ")))
X = int(input())

SUM = sum(A)
CNT = X //SUM * len(A)
x = int(X % SUM)
for a in A:
    x -= a
    CNT += 1
    if x < 0:
        print(CNT)
        exit()