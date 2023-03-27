n = int(input())
s = 0
x, y = [], []
for i in range(n):
    x1, y1 = map(int, input().split())
    x.append(x1)
    y.append(y1)
x.sort()
y.sort()

s = sum([(x[i+1]-x[i] + y[i+1]-y[i]) * (i+1) * (n-i-1) for i in range(n-1)])
print( (s * 2) // ((n-1)*n))