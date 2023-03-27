n = int(input())
s = 0
x, y = map(int, input().split())
was = [(x,y)]
for i in range(n-1):
    x, y = map(int, input().split())
    for el in was:
        s += abs(el[0] - x) + abs(el[1] - y)
    was.append((x, y))
print( (s * 2) // ((n-1)*n))