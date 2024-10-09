import heapq

def astar(graph,start,goal,heuristic):
    frontier = [(heuristic[start], start)]
    explored = set()
    cost = {start:0}
    path = {start:None}

    while frontier:
        _ , current = heapq.heappop(frontier)

        if current == goal:
            path_list = [current]
            while path[current]!= None:
                path_list.append(path[current])
                current = path[current]
            path_list.reverse()
            return path_list

        explored.add(current)

        for neighbours in graph[current]:
            new_cost = cost[current] + graph[current][neighbours]
            if neighbours not in cost or new_cost < cost[neighbours]:
                cost[neighbours] = new_cost
                priority = new_cost + heuristic[neighbours]
                heapq.heappush(frontier,(priority,neighbours))
                path[neighbours] = current
    return None


graph = {
'A' : {'B':5, 'C':10},
'B' : {'D':15},
'C' : {'D':20},'D':{}
}
heuristic = {'A':15,'B':10,'C':5, 'D':0}
start = 'A'
goal = 'D'
path = astar(graph, start, goal, heuristic)
print(path)