def coin(N, Y):
    for a in range(N + 1):
        for b in range(N-a + 1):
            c = N-a-b
            if c + 5*b + 10*a == Y:
                return a,b,c
    return -1,-1,-1
ny = input()
n, y = ny.split(maxsplit=1)
y = int(y) / 1000
n = int(n)
print(*coin(n,y))