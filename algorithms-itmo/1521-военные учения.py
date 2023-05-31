def remove(v, l, r, pos):
    while l != r:
        tree[v][0] -= 1
        if pos <= tree[v * 2][0]:
            r = (l + r) // 2
            v = v * 2
        else:
            pos -= tree[v * 2][0]
            l = (l + r) // 2 + 1
            v = v * 2 + 1
    tree[v][0] -= 1
    return tree[v][1]


def build(v, l, r):
    if l == r:
        tree[v] = [1, l + 1]
    else:
        mid = (l + r) // 2
        build(v * 2, l, mid)
        build(v * 2 + 1, mid + 1, r)
        tree[v][0] = tree[v * 2][0] + tree[v * 2 + 1][0]


n, k = map(int, input().split())
tree = [[0] * 2 for i in range(4 * n)]
build(1, 0, n - 1)
curr = k
for i in range(n):
    print(remove(1, 1, n, curr), end=" ")
    curr = (curr - 1 + k) % (n - 1 - i)
    if curr == 0: curr = n - 1 - i
