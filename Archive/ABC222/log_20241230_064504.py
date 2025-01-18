N, M = map(int, input().split(" "))
A = []
for _ in range(2*N):
    A.append(input().split(" "))
print(A)

L = []
for i in range(1, 2*N+1):
    L.append(tuple((0, i)))
    # 勝利数　No
    
print(L)