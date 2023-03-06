n = int(input())
stack = []
was = 0
for i in range(n):
    x = int(input())
    if stack == []: 
        for i in range(was + 1, x):
            stack.append(i)
    else:
        if stack[-1] == x:
            stack.pop(-1)
        elif stack[-1] < x:
            for i in range(was + 1, x):
                stack.append(i)
        else:
            print("Cheater")
            exit()
    was = max(was, x)
if stack == []: print("Not a proof")