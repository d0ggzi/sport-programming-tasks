n = int(input())
curr = 1
print(0, end = " ")
for i in range(2, n+1):
    h = 2*i - 1
    curr += h*h
    print(h**3 - curr, end = " ")