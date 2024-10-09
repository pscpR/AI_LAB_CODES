def dfs(component,visited, graph, node):
    component.append(node)
    visited[node] = True

    for i in graph[node]:
        if not visited[i]:
            dfs(component, visited, graph, i)


graph =  {0:[1], 1:[2,3], 2:[0,1,4], 3:[], 4:[]}
node = 0
component  = []
visited = [False] * len(graph)
dfs(component, visited , graph , node)
print(component)