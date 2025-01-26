MAX = 5
N = int(input())
A = list(map(int, input().split()))
L0 = [0 for i in range(MAX)]
L1 = [0 for i in range(MAX)]


for i in A:
    S = format(i, 'b')[::-1]
    print(S)
    for i in range(len(S)):
        if S[i] == '1':
            L1[i] += 1
        else:
            L0[i] += 1
    print()
print(L0)
print(L1)        
