s = input()
n, a, b = s.split(maxsplit=2)
c = 0
for i in range(int(n)):
    t = sum(int(d) for d in str(i+1))
    if t>=int(a) and t<=int(b):
        c += (i+1)
print(c)