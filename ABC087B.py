def coin(A, B, C, X):
    count = 0
    for a in range(A + 1):
        for b in range(B + 1):
            for c in range(C + 1):
                if 500*a + 100*b + 50*c == X:
                    count += 1
    return count
A = input()
B = input()
C = input()
X = input()
print(coin(int(A),int(B),int(C),int(X)))