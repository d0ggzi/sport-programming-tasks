n = int(input())
s = []
for i in range(n):
    q = input()
    if q[0] == '1':
        el = q.split()[1]
        if len(s) != 0 and s[-1][1] == el:
            s[-1][0] += 1
        else:
            s.append([1,el])
    elif q[0] == '3':
        s[0][0] -= 1
        print(s[0][1])
        if s[0][0] == 0:
            s.pop(0)
    elif q[0] == '2':
        for i in range(len(s)):
            s[i][0] *= 2