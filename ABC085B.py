d=[]
nd = []
n = int(input())
for _ in range(n):
    d.append(input())
sorted_d = sorted(d)
prev = None
for num in sorted_d:
    if num != prev:
        nd.append(num)
        prev = num
print (len(nd))