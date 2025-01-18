def check(R, i, j):
    if (i+0.5)**2 + (j+0.5)**2 <= R**2 and (i-0.5)**2 + (j-0.5)**2 <= R**2 and (i+0.5)**2 + (j-0.5)**2 <= R**2 and (i-0.5)**2 + (j+0.5)**2 <= R**2:
        return True
    else:
        return False
import math
R = int(input())
CNT = 0
for i in range(0, R+1):
    j = int(math.sqrt(R**2 - i**2))+2
    while check(R, i, j) == False and j >= 0:
        j -= 1
    if j != -1:
        if i == 0:
            CNT += j*2+1
        else:
            CNT += j*4+2
print(CNT)