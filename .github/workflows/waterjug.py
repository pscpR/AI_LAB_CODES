def solve(jug_sizes, target_volume, start_volumes):
    explored = set()
    start_state = tuple(start_volumes)
    path = dfs(start_state, jug_sizes, target_volume, explored)
    return path

def dfs(current_state, jug_sizes, target_volume, explored):
    jug1, jug2 = current_state
    if jug1 == target_volume or jug2 == target_volume:
        return [current_state]
    explored.add(current_state)
    successors = get_successors(current_state, jug_sizes)
    for successor in successors:
        if successor not in explored:
            path = dfs(successor, jug_sizes, target_volume, explored)
            if path is not None:
                return [current_state] + path
    return None

def get_successors(state, jug_sizes):
    jug1, jug2 = state
    jug1_cap, jug2_cap = jug_sizes
    successors = []
    successors.append((jug1_cap, jug2))
    successors.append((jug1, jug2_cap))
    successors.append((0, jug2))
    successors.append((jug1, 0))
    amount_to_pour = min(jug1, jug2_cap - jug2)
    successors.append((jug1 - amount_to_pour, jug2 + amount_to_pour))
    amount_to_pour = min(jug2, jug1_cap - jug1)
    successors.append((jug1 + amount_to_pour, jug2 - amount_to_pour))
    return [s for s in successors if is_valid_state(s, jug_sizes)]

def is_valid_state(state, jug_sizes):
    jug1_cap, jug2_cap = jug_sizes
    jug1, jug2 = state
    return 0 <= jug1 <= jug1_cap and 0 <= jug2 <= jug2_cap

jugs = (4, 3)
target = 2
start = (0, 0)
path = solve(jugs, target, start)
print("Path to reach target volume:", path)
