from queue import PriorityQueue

class Puzzle:
    def __init__(self, board, parent=None, depth=0):
        self.b = board
        self.p = parent
        self.d = depth

    def __eq__(self, other):
        return self.b == other.b

    def __hash__(self):
        return hash(str(self.b))

    def __lt__(self, other):
        return False

    def manhattan_distance(self):
        dist = 0
        for i in range(3):
            for j in range(3):
                if self.b[i][j]!= 0:
                    x, y = divmod(self.b[i][j] - 1, 3)
                    dist += abs(x - i) + abs(y - j)
        return dist

    def is_goal(self):
        return self.manhattan_distance() == 0

    def successors(self):
        succ = []
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        x, y = next((i, j) for i in range(3) for j in range(3) if self.b[i][j] == 0)
        for dx, dy in moves:
            if 0 <= x + dx < 3 and 0 <= y + dy < 3:
                new_board = [row[:] for row in self.b]
                new_board[x][y], new_board[x + dx][y + dy] = new_board[x + dx][y + dy], new_board[x][y]
                succ.append(Puzzle(new_board, self, self.d + 1))
        return succ

def a_star_search(initial_state):
    frontier = PriorityQueue()
    frontier.put((initial_state.manhattan_distance() + initial_state.d, initial_state))
    visited = set()

    while not frontier.empty():
        _, current = frontier.get()
        if current.is_goal():
            path = []
            while current:
                path.append(current.b)
                current = current.p
            return path[::-1]
        visited.add(current)
        for successor in current.successors():
            if successor not in visited:
                frontier.put((successor.manhattan_distance() + successor.d, successor))

if __name__ == "__main__":
    initial_state = Puzzle([[1, 2, 3], [4, 0, 5], [6, 7, 8]])
    solution = a_star_search(initial_state)
    if solution:
        print("Solution path:")
        for step, board in enumerate(solution):
            print(f"Step {step + 1}:")
            for row in board:
                print(row)
            print()
    else:
        print("No solution found.")
