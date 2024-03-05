def ope(n, count=0):
    for i in range(len(n)):
        if n[i] % 2 == 1:
            return count
        else:
            n[i] /= 2
    else:
        return ope(n, count + 1)

s = input()
a = input()
n = [int(n) for n in a.split()]

print(ope(n))