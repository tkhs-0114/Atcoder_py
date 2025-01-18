import itertools
S,K = input().split(" ")
K = int(K)

L = sorted(set((itertools.permutations(S))))
print("".join(L[K-1]))