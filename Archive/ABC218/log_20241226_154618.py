S = list("abcdefghijklmnopqrstuvwxyz")
P = map(int, input().split(" "))
for p in P:
    print(S[p-1], end="")
print()