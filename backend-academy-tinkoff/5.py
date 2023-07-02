import itertools

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

minugly, maxpower = 9999999, 0
for i in range(2, n+1):
    for el in list(itertools.combinations(spisok,i)):
        print(el)
        a, b, c = 0, 0, 0
        for elem in el:
            a += elem[0]; b += elem[1]; c += elem[2]
        minugly2 = max(a, b, c) - min(a, b, c)
        maxpower2 = a + b + c
        if minugly2 == minugly and maxpower2 > maxpower:
            maxpower = maxpower2
        elif minugly2 < minugly:
            minugly = minugly2
            maxpower = maxpower2
print(maxpower + answer)