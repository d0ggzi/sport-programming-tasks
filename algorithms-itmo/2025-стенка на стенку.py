t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    fights = k * (k-1) // 2
    sostav = n // k
    ostatok = n % k
    result = sostav * sostav * fights   # количество боев не учитывая остаток
    result += ostatok * sostav * (k-1) + ostatok * (ostatok - 1) // 2
    print(result)