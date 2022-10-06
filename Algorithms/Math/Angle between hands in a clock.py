import math
t = int(input())
for _ in range(t):
    x,y = map(float,input().split())
    if y in [0, 60]:
        diff = abs((x*30)-(y*6))
    elif x in [0, 12]:
        diff = abs((y*6)-(y*0.5))
    else:
        diff = abs((y*6)-(x*30+y*0.5))
    diff = min(diff,360-diff)
    print (math.floor(diff))
