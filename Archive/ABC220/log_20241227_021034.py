A, B, C = map(int, input().split(" "))
D = 1
while C * D <= B:
    if C * D >= A:
        print(C * D)
        exit()
    D += 1 
print(-1)