n, m, s, v = map(float, input().split())
n, m, s = int(n), int(m), int(s)
rebra = []
for i in range(m):
    a,b,rab,cab,rba,cba = map(float, input().split())
    a, b = int(a) - 1, int(b) - 1
    rebra.append([a,b,rab,cab])
    rebra.append([a,b,rba,cba])
money = [0]*n
money[s-1] = v

for i in range(n-1):
    for rebro in rebra:
        if (money[rebro[0]] - rebro[3]) * rebro[2] > money[rebro[1]]:
            money[rebro[1]] = money[rebro[0]] - rebro[3] * rebro[2]

for rebro in rebra:
    if (money[rebro[0]] - rebro[3]) * rebro[2] > money[rebro[1]]:
        print("YES")
        exit()
print("NO")