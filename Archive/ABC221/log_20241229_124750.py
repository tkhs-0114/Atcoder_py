A, B = map(int, input().split(" "))

C = A - B
sum = 1
for i in range(C):
    sum *= 32
print(sum)