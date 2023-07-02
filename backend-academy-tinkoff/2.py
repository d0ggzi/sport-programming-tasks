n = int(input())
s = []
for i in range(n):
    q = input()
    if q[0] == '1':
        s.append(q.split()[1])
    elif q[0] == '3':
        # print("answer is ", end = "")
        print(s.pop(0))
    elif q[0] == '2':
        s = [s[i//2] for i in range(len(s)*2)]