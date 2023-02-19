from itertools import product

n = int(input())
w = [int(i) for i in input().split()]
s1 = max(w)
sall = sum(w)
w.remove(s1)
result = 1000
for el in product(range(2), repeat=n-1):
    s = s1
    for i in range(n-1):
        s += el[i] * w[i]
    result = min(result, abs(sall - s - s))
print(result)