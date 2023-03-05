n = int(input())
diego = list(map(int, input().split()))
diego.sort()
k = int(input())
guests = list(map(int, input().split()))

for i in range(k):
    l, r = 0, n - 1
    flag = True
    while l <= r:
        index = l + (r-l) // 2
        x = diego[index]
        if guests[i] < x:
            r = index - 1
        elif guests[i] > x:
            l = index + 1
        else:
            flag = False
            while diego[index] == guests[i] and index >= 0:
                index -= 1
            print(index + 1)
            break
    if flag: print(l)