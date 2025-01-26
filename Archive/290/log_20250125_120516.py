L = list(map(int, input().split(" ")))
for i in range(len(L)-1):
    M = list()
    for j in range(len(L)):
        M.append(L[j])
    tmp = M[i]
    M[i] = M[i+1]
    M[i+1] = tmp
    flag = True
    for i in range(len(M)-1):
        if M[i] >= M[i+1]:
            flag = False
    if flag:
        print("Yes")
        exit()
print("No")