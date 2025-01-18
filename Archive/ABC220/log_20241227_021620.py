K = int(input())
A, B = input().split(" ")
A10 = 0
B10 = 0
for i in range(len(A)):
    a = int(A[len(A) - i - 1])
    A10 += a * K**i
for i in range(len(B)):
    a = int(B[len(B) - i - 1])
    B10 += a * K**i

print(A10 * B10)