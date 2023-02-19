n = int(input())
s1, s2 = 0, 0
res = 0
for i in range(n):
    q = int(input())
    s1 += q
    if i!=0: s2 += q
    res = max(res, max(s1,s2))
    if s1 < 0: s1 = 0
    if s2 < 0: s2 = 0
print(res)