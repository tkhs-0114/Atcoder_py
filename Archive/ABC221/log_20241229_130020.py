S = list(input())
T = list(input())

if S == T:
  print("Yes")
  exit()

for i in range(len(S)-1):
  X = S[:]
  X[i], X[i+1] = X[i+1], X[i]
  if X == T:
    print("Yes")
    exit()

print("No")