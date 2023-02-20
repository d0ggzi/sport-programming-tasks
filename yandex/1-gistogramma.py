string = ""
d = {}
fin = open("input-gistogramma.txt", "r")
for line in fin:
    string += "".join(line.split())
for s in string:
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1
sorted_d = {}
for k in sorted(d.keys()):
    sorted_d[k] = d[k]
m = max(sorted_d.values())
while m != 0:
    res = ""
    for s in sorted_d.keys():
        if sorted_d[s] == m:
            res += "#"
            sorted_d[s] -= 1
        else:
            res += " "
    m = max(sorted_d.values())
    print(res)
print("".join(sorted_d.keys()))