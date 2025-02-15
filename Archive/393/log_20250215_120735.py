S = input()
cnt = 0
for i in range(len(S)):
    for j in range(1, len(S)- i):
        if S[i] == "A" and S[i+j] == "B" and S[i+j+j] == "C":
            cnt += 1
print(cnt)