n, m, q = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
for i in range(q):
    x, y, k = map(int, input().split())
    x -= 1; y -= 1
    answer = 0
    el = s[x][y]
    for j in range(m):
        if abs(el - s[x][j]) <= k and j != y:
            answer += 1
    for j in range(n):
        if abs(el - s[j][y]) <= k and j != x:
            answer += 1
    print(answer)