def f(x, y, size, start, dx, dy):
    global maxk
    if size == 2:
        for i in range(size):
            for j in range(size):
                if s[dx + i][dy + j] == -1:
                    s[dx + i][dy + j] = maxk
        maxk += 1
        return 0
    if x < size // 2 and y < size // 2: # 1 quarter
        s[dx + size//2][dy + size//2] = s[dx + size//2][dy + size//2 - 1] = s[dx + size//2 - 1][dy + size//2] = maxk
        maxk += 1
        f(x, y, size//2, (0, 0), dx, dy) # 1 quarter
        f(size//2 - 1, 0, size//2, (0, size//2), dx, dy + size//2) # 2 quarter
        f(0, size//2 - 1, size//2, (size//2, 0), dx + size//2, dy) # 3 quarter
        f(0, 0, size//2, (size//2, size//2), dx + size//2, dy + size//2) # 4 quarter
    elif x < size // 2 and y >= size // 2: # 2 quarter
        s[dx + size//2][dy + size//2] = s[dx + size//2][dy + size//2 - 1] = s[dx + size//2 - 1][dy + size//2 - 1] = maxk
        maxk += 1
        f(x, y - size//2, size//2, (0, 0), dx, dy + size//2) # 2 quarter
        f(size//2 - 1, size//2 - 1, size//2, (0, 0), dx, dy) # 1 quarter
        f(0, size//2 - 1, size//2, (size//2, 0), dx + size//2, dy) # 3 quarter
        f(0, 0, size//2, (size//2, size//2), dx + size//2, dy + size//2) # 4 quarter
    elif x >= size // 2 and y < size // 2: # 3 quarter
        s[dx + size//2][dy + size//2] = s[dx + size//2 - 1][dy + size//2] = s[dx + size//2 - 1][dy + size//2 - 1] = maxk
        maxk += 1
        f(x - size//2, y, size//2, (0, 0), dx + size//2, dy) 
        f(size//2 - 1, size//2 - 1, size//2, (0, 0), dx, dy) # 1 quarter
        f(size//2 - 1, 0, size//2, (0, size//2), dx, dy + size//2) # 2 quarter
        f(0, 0, size//2, (size//2, size//2), dx + size//2, dy + size//2) # 4 quarter
    elif x >= size // 2 and y >= size // 2: # 4 quarter
        s[dx + size//2 - 1][dy + size//2] = s[dx + size//2][dy + size//2 - 1] = s[dx + size//2 - 1][dy + size//2 - 1] = maxk
        maxk += 1
        f(x - size//2, y - size//2, size//2, (0, 0), dx + size//2, dy + size//2) 
        f(size//2 - 1, size//2 - 1, size//2, (0, 0), dx, dy) # 1 quarter
        f(size//2 - 1, 0, size//2, (0, size//2), dx, dy + size//2) # 2 quarter
        f(0, size//2 - 1, size//2, (size//2, 0), dx + size//2, dy) # 3 quarter
        
        

n = 2 ** int(input())
s = [[-1] * n for i in range(n)]
x, y = map(int, input().split())
maxk = 1

s[x - 1][y - 1] = 0
f(x - 1, y - 1, n, (0, 0), 0, 0)
for el in s:
    print("\t".join([str(elem) for elem in el]))