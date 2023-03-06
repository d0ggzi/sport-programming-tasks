from math import atan2, pi

n = int(input())
x1, y1 = map(int, input().split())
angles = []

for i in range(n - 1):
    x, y = map(int, input().split())
    angle = atan2((y - y1) , (x - x1))
    dist = ((x - x1)**2 + (y-y1)**2)**0.5
    if (y - y1) < 0:
        angle += 2 * pi
    angles.append((angle, dist, i + 2))

print(n)
print(1)
angles.sort(key = lambda x: (x[0], x[1]))

start = 0
max_angle = angles[0][0] - angles[n-2][0] + 2*pi
for i in range(n - 2):
    if (angles[i+1][0] - angles[i][0] > max_angle):
        max_angle = angles[i+1][0] - angles[i][0]
        start = i + 1
for i in range(start, n - 1):
    print(angles[i][2])
for i in range(start):
    print(angles[i][2])
