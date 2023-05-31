def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:        
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

n = int(input())
neighbors = dict()
for i in range(n):
    x = input().split()[:-1]
    for el in x:
        neighbors[i+1] = neighbors.get(i+1, []).append(int(el))

visited = []
queue = []

bfs(visited, neighbors, 1)