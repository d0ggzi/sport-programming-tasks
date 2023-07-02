for i in range(int(input())):
    a, b = map(int, input().split())
    answer = 1
    for j in range(a, b+1):
        answer *= j
    while len(str(answer)) != 1:
        s = 0
        for el in list(str(answer)):
            s += int(el)
        answer = s
    print(answer)