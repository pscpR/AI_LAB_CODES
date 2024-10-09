from queue import PriorityQueue

def UCS(start_node,goal_node,graph):
    q = PriorityQueue()
    q.put((0, start_node))
    explored  = set()
    while not q.empty(): 
        curr_cost, curr_node = q.get()
        explored.add(curr_node)
        if curr_node == goal_node:
            return curr_cost
        for neighbours,cost in graph[curr_node].items():
            if neighbours not in explored:
                new_cost = curr_cost + cost
                q.put((new_cost,neighbours))
    return -1




graph = {
'A': {'B': 5, 'C': 3},
'B': {'D': 2},
'C': {'D': 4}, 
'D': {}
}
start_node = 'A' 
goal_node = 'D'   

print(UCS(start_node,goal_node,graph))