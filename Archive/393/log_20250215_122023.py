N, M = map(int, input().split())
cnt = 0
G2 = [set() for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    if(b-1 in G2[a-1] or a-1 in G2[b-1] or a == b):
        cnt += 1
        continue
    G2[a-1].add(b-1)
print(cnt)