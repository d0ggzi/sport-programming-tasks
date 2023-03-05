s = [1, 100, 50]
s.sort()

to_found = 300

l, r = 0, len(s) - 1
while l <= r:
    index = l + (r-l) // 2
    x = s[index]
    if to_found < x:
        r = index - 1
    elif to_found > x:
        l = index + 1
    else:
        print("I've found")
        break
    print(l, r)