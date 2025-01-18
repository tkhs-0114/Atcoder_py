X, Y = input().split(".")

if 0 <= int(Y) <= 2:
    print(f"{X}-")
elif 3 <= int(Y) <= 6:
    print(f"{X}")
elif 7 <= int(Y) <= 9:
    print(f"{X}+")