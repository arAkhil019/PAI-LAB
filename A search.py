import heapq

def actions(state):
    x, y = state
    pos_actions = []
    if x < 4:
        pos_actions.append("fill 4l jug")
    if y < 3:
        pos_actions.append("fill 3l jug")
    if x > 0:
        pos_actions.append("empty 4l jug")
    if y > 0:
        pos_actions.append("empty 3l jug")
    if x > 0 and y < 3:
        pos_actions.append("pour 4l to 3l jug")
    if y > 0 and x < 4:
        pos_actions.append("pour 3l to 4l jug")
    return pos_actions

def transition(state, action):
    x, y = state
    if action == "fill 4l jug":
        return (4, y)
    elif action == "fill 3l jug":
        return (x, 3)
    elif action == "empty 4l jug":
        return (0, y)
    elif action == "empty 3l jug":
        return (x, 0)
    elif action == "pour 4l to 3l jug":
        amount_to_pour = min(x, 3 - y)
        return (x - amount_to_pour, y + amount_to_pour)
    elif action == "pour 3l to 4l jug":
        amount_to_pour = min(y, 4 - x)
        return (x + amount_to_pour, y - amount_to_pour)

def astar_search(start_state):
    frontier = []
    heapq.heappush(frontier, (0, start_state, []))
    explored = set()
    while frontier:
        _, state, path = heapq.heappop(frontier)
        if state in explored:
            continue
        if state == (2, 0):
            return path
        explored.add(state)
        for action in actions(state):
            next_state = transition(state, action)
            if next_state not in explored:
                new_cost = len(path) + 1
                heapq.heappush(frontier, (new_cost, next_state, path + [action]))
    return None

start_state = (0, 0)
solution = astar_search(start_state)
if solution:
    print("Solution found in", len(solution), "steps:")
    for i, action in enumerate(solution, 1):
        print("Step", i, ":", action)
else:
    print("No solution found")