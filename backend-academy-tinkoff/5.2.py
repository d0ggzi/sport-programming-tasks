def func(a, b, c, visited, minugly, maxpower, index):
    if len(visited) == index: 
        return maxpower
    for i in range(index, len(visited)):
        el = visited[i]
        a1 = a; b1 = b; c1 = c
        a += el[0]; b += el[1]; c += el[2]
        minugly2 = max(a, b, c) - min(a, b, c)
        if minugly2 <= minugly:
            maxpower2 = a + b + c
            minugly = minugly2
            if maxpower2 > maxpower:
                maxpower = maxpower2
        maxpower = func(a1, b1, c1, visited, minugly, maxpower, i+1)
    return maxpower

n = int(input())
answer = 0
spisok = []
for i in range(n):
    s = input()
    a, b, c = 0, 0, 0
    for el in s:
        if el == 'a': a+=1
        elif el == 'b': b+=1
        else: c+=1
    if a == b == c:
        answer += len(s)
        n-=1
    else:
        spisok.append((a,b,c))
print(func(0,0,0,spisok,99999, 0, 0) + answer)