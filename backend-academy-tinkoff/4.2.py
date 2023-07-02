for i in range(int(input())):
    a, b = map(int, input().split())
    if b-a > 5:
        print(9)
        continue
    answer = 1
    for j in range(a, b+1):
        answer *= (j%9)
    if answer % 9 == 0: print(9)
    else: print(answer % 9)