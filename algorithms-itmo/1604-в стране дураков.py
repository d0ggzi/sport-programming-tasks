k = int(input())
x = [[str(index + 1), int(element)] for index, element in enumerate(input().split())]
x = (sorted(x, key=lambda item: item[1], reverse=True))
while len(x) > 1:
    prev = 0
    i = 1
    while i < len(x):
        if x[i][1] >= prev:
            if x[0][1] >= x[i][1]:
                print(x[0][0] + " " + x[i][0] + " ", end="")
                x[i][1] -= 1
                x[0][1] -= 1
                prev = x[i][1]
                if x[i][1] == 0: x.pop(i)
                if x[0][1] == 0: x.pop(0)
            else:
                print(x[i][0] + " " + x[0][0] + " ", end="")
                x[i][1] -= 1
                x[0][1] -= 1
                prev = x[i][1]
                if x[i][1] == 0: x.pop(i)
                if x[0][1] == 0: x.pop(0)
            
        i += 1
if len(x) == 1:
    print((x[0][0] + " ") * x[0][1], end = "")