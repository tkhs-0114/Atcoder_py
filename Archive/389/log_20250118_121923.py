Q = int(input())
L = [0]
S = 0
for _ in range(Q):
    Q = input()
    if(Q[0] == "1"):
        _, l = map(int, Q.split(" "))
        L.append(L[-1]+l)
    elif(Q[0] == "2"):
        S += 1
    elif(Q[0] == "3"):
        _, k = map(int, Q.split(" "))
        print(L[S+k-1] - L[S])