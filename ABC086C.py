def can_go(N, plans):
    t0,x0,y0 = 0,0,0
    for t, x, y in plans:
        dist = abs(x - x0) + abs(y - y0)
        time = t - t0
        if dist > time or (dist % 2) != (time % 2):
            return False
        x0, y0, t0 = x, y, t
    return True

N = int(input())
plans = [tuple(map(int, input().split())) for _ in range(N)]

if can_go(N,plans):
    print("Yes")
else:
    print("No")