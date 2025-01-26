N = int(input())
A = list(map(int, input().split(" ")))

N = A[0]
P = A[1] / N
if len(A) <= 2:
    print("Yes")
    exit()

for i in range(1, len(A)):
    N = N * P
    if A[i] != N:
        print("No")
        exit()
print("Yes")