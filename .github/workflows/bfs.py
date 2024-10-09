def bfs(queue, visited, graph, node):
    queue.append(node)
    visited.add(node)

    while queue:
        m = queue.pop(0)
        print(m, end = " ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
            
graph =  {0:[1], 1:[2,3], 2:[0,1,4], 3:[], 4:[]}
node = 0
queue = []
visited = set()
bfs(queue, visited, graph, node)