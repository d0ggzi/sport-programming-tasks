cube = [int(j) for j in input().split()]
neighbours = {
    0: [1, 3, 4],
    1: [0, 2, 5],
    2: [1, 3, 6],
    3: [0, 2, 7],
    4: [0, 5, 7],
    5: [1, 4, 6],
    6: [2, 5, 7],
    7: [3, 4, 6]
}
letters = 'ABCDEFGH'
to_be_printed = []

# Удаление смежных
for i in range(8):
    if cube[i] > 0:
        for j in range(3):
            neighbour = neighbours[i][j]
            minimum = min(cube[neighbour], cube[i])
            if minimum:
                cube[i] -= minimum
                cube[neighbour] -= minimum
                for _ in range(minimum): to_be_printed.append(letters[i] + letters[neighbour] + '-')

# Удаление по главной диагонали
diagonal = {0: 6, 1: 7, 2: 4, 3: 5, 4: 2, 5: 3, 6: 0, 7: 1}
for i in range(8):
    minimum = min(cube[diagonal[i]], cube[i])
    cube[i] -= minimum
    cube[diagonal[i]] -= minimum
    first_neighbour = neighbours[i][0]
    for el in neighbours[first_neighbour]:
        if el != i: 
            second_neighbour = el
            break
    for j in range(minimum):
        to_be_printed.append(letters[first_neighbour] + letters[second_neighbour] + '+')
        to_be_printed.append(letters[i] + letters[first_neighbour] + '-')
        to_be_printed.append(letters[diagonal[i]] + letters[second_neighbour] + '-')

if sum(cube) != 0:
    print("IMPOSSIBLE")
else:
    for el in to_be_printed:
        print(el)