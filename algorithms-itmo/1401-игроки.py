def f(x, y, id, table2, todo):
    table = [list(el) for el in table2]
    if todo != 0:
        if todo == 1:
            table[x][y] = table[x + 1][y] = table[x + 1][y + 1] = id
            y += 1
        elif todo == 2:
            table[x][y] = table[x + 1][y] = table[x + 1][y - 1] = id
            y -= 1
        elif todo == 3:
            table[x][y] = table[x + 1][y] = table[x][y + 1] = id
            x += 1
            y += 1
        elif todo == 4:
            table[x][y] = table[x + 1][y + 1] = table[x][y + 1] = id
            x += 1
    print(id, x, y)
    for el in table:
        print(*el)
    print("---------------------------")
    if x > len(table) - 1:
        return 0
    if table[x][y] != -1:
        for i in range(1, len(table) - 1):
            for j in range(1, len(table) - 1):
                if table[i][j] == -1:
                    f(i, j, id, table, 0)
    if table[x][y] == table[x + 1][y] == table[x + 1][y + 1] == -1:
        f(x, y, id + 1, table, 1)
    if table[x][y] == table[x + 1][y] == table[x + 1][y - 1] == -1:
        f(x, y, id + 1, table, 2)
    if table[x][y] == table[x + 1][y] == table[x][y + 1] == -1:
        f(x, y, id + 1, table, 3)
    if table[x][y] == table[x + 1][y + 1] == table[x][y + 1] == -1:
        f(x, y, id + 1, table, 4)

    ch = 0
    for el in table:
        if el.count(-1) == 0:
            ch += 1
    if ch == len(table):
        for el in table:
            print(*el)
        exit()

    return 0


n = 2 ** int(input())
s = [[-1] * (n + 2) for i in range(n + 2)]
for i in range(n + 2):
    for j in range(n + 2):
        if i == 0 or i == n + 1:
            s[i][j] = 0
        elif j == 0 or j == n + 1:
            s[i][j] = 0
x, y = map(int, input().split())

s[x][y] = 0
f(1, 1, 0, s, 0)
print(-1)