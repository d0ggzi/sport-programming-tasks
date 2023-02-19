from math import atan, pi

n = int(input())
s = []
x1, y1 = 9999999, 9999999
for i in range(n):
    x, y = map(int, input().split())
    if y < y1 or (y == y1 and x < x1):
        x1 = x
        y1 = y
        id = i
    s.append((x, y))
angles = []
for j, el in enumerate(s):
    if el[0] == x1 and el[1] == y1: continue
    elif el[0] == x1: angle = pi/2
    elif el[1] == y1: angle = 0
    else: 
        angle = atan((el[1] - y1) / (el[0] - x1))
        if angle < 0:
            angle += 2 * pi
    angles.append((angle, j))
angles.sort()
print(id+1, angles[n//2-1][1] + 1)
