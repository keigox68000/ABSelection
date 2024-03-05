n = input()
a = list(map(int,input().split()))
sorted_a = sorted(a)
alice = sum(sorted_a[::2])
bob = sum(sorted_a[1::2])
if len(a) % 2 == 0:
    alice, bob = bob, alice
print (alice - bob)