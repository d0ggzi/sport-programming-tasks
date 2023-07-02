import itertools
from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

@timeit
def f1(spisok):
    minugly, maxpower = 9999999, 0
    for i in range(2, n+1):
        for el in list(itertools.combinations(spisok,i)):
            a, b, c = 0, 0, 0
            for elem in el:
                a += elem[0]; b += elem[1]; c += elem[2]
            minugly2 = max(a, b, c) - min(a, b, c)
            maxpower2 = a + b + c
            if minugly2 == minugly and maxpower2 > maxpower:
                maxpower = maxpower2
            elif minugly2 < minugly:
                minugly = minugly2
                maxpower = maxpower2
    return maxpower, minugly

@timeit
def func(a, b, c, visited, minugly, maxpower, index):
    if len(visited) == index: 
        return maxpower, minugly
    for i in range(index, len(visited)):
        el = visited[i]
        a1 = a; b1 = b; c1 = c
        a += el[0]; b += el[1]; c += el[2]
        minugly2 = max(a, b, c) - min(a, b, c)
        if minugly2 <= minugly:
            maxpower2 = a + b + c
            minugly = minugly2
            if maxpower2 > maxpower:
                maxpower = maxpower2
        maxpower, minugly = func(a1, b1, c1, visited, minugly, maxpower, i+1)
    return maxpower, minugly

n = int(input())
answer = 0
spisok = []
for i in range(n):
    s = input()
    a, b, c = 0, 0, 0
    for el in s:
        if el == 'a': a+=1
        elif el == 'b': b+=1
        else: c+=1
    if a == b == c:
        answer += len(s)
        n-=1
    else:
        spisok.append((a,b,c))
ans1, ans11 = f1(spisok)
ans2, ans21 = func(0,0,0,spisok,99999, 0, 0)
if ans1 == ans2:
    print("correct", ans11, ans21)
else:
    print("incorrect", ans1, ans2, ans11, ans21) 