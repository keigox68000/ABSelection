n = int(input())
txy=[list(map(int,input().split())) for _ in range(n)]
p = [0,0,0]

for i in range(n):
    step = abs(txy[i][1]-p[1])+abs(txy[i][2]-p[2])
    time = txy[i][0]-p[0]
    if time>=step and (time-step)%2 == 0:
        p = txy[i]
        continue
    else:
        print("NO")
        exit(0)
print("YES")