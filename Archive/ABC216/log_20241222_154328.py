N = int(input())
T = [ input() for i in range(N)]

for i in range(0, N-1):
    for j in range(i+1, N):
        if(T[i] == T[j]):
            print("Yes")
            exit()
print("No")