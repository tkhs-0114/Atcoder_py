N = int(input())
S = list(map(int, list(input())))
a = N
b = 0
l = 0
for i in range(N):
    if S[i] == 1:
        l += 1
        a = min(a, i)
        b = max(i, b)
if a == b or l == 0 or l ==b-a+1:
    print(0)
    exit()
c = a+b // 2
out = 0
cnt = 0
for i in range(c, -1, -1):
    if S[i] == 1:
        out += abs(c-i) - cnt
        cnt += 1
cnt = 1
for i in range(c, N):
    if S[i] == 1:
        out += abs(c-i) - cnt
        cnt += 1
out2 = 0
cnt = 1
for i in range(c, -1, -1):
    if S[i] == 1:
        out2 += abs(c-i) - cnt
        cnt += 1
cnt = 0
for i in range(c, N):
    if S[i] == 1:
        out2 += abs(c-i) - cnt
        cnt += 1
print(min(out, out2))