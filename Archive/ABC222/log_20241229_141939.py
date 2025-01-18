N, P = map(int, input().split(" "))
cnt = 0
A = list(map(int, input().split(" ")))
for a in A:
    if a < P:
        cnt += 1
print(cnt)