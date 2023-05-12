def print_tree(cur_tree, depth):
    if len(cur_tree) == 0:
        return
    for key in sorted(cur_tree.keys()):
        print(" " * depth + key)
        print_tree(cur_tree[key], depth + 1)
        

n = int(input())
tree = dict()
for i in range(n):
    x = input().split("\\")
    jopa = tree
    for i in range(len(x)):
        if x[i] in jopa:
            jopa = jopa.get(x[i])
        else:
            if len(x)-i == 1:
                jopa[x[i]] = dict()
                break
            branch = dict()
            branch[x[-1]] = dict()
            for j in range(len(x)-2, i, -1):
                new_branch = dict()
                new_branch[x[j]] = dict(branch)
                branch = dict(new_branch)
            jopa[x[i]] = branch
            break
print_tree(tree, 0)