OUT = set()
LSET = set()
MAX = 0

def FUNC(A):
    global OUT, LSET, MAX
    A.sort()
    if len(A) == 0:
        return
    G = A[0]
    for i in range(1, len(A)):
        G ^= A[i]
    MAX = max(MAX, G)
    if G not in OUT:
        OUT.add(G)
    else:
        if G > MAX:
            return
    S = "".join(map(str, A))
    if S in LSET:
        return
    LSET.add(S)
    
    # print(G, A)
    # if(G == 91):
    #     exit()
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            NUM = list()
            for k in range(len(A)):
                if k != j:
                    NUM.append(A[k])
                else:
                    NUM[i] += A[j]
            FUNC(NUM)
        

N = int(input())
A = list(map(int, input().split()))
FUNC(A)
# print(OUT)
print(len(OUT))