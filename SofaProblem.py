from collections import deque

class State:
    def __init__(self, x1, y1, x2, y2, steps):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.steps = steps

    def __eq__(self, other):
        return (self.x1, self.y1, self.x2, self.y2) == (other.x1, other.y1, other.x2, other.y2)

    def __hash__(self):
        return hash((self.x1, self.y1, self.x2, self.y2))

def is_valid(x1, y1, x2, y2, grid, m, n):
    return (0 <= x1 < m and 0 <= y1 < n and
            0 <= x2 < m and 0 <= y2 < n and
            grid[x1][y1] != 'H' and
            grid[x2][y2] != 'H' and
            not (x1 == x2 and y1 == y2))  # Prevent overlapping cells

def can_rotate(current, grid, m, n):
    x1, y1, x2, y2 = current.x1, current.y1, current.x2, current.y2
    if x1 == x2:  # Horizontal
        return (y1 + 1 < n and
                grid[x1][y1] != 'H' and
                grid[x1][y1 + 1] != 'H' and
                grid[x1 + 1][y1] != 'H' and
                grid[x1 + 1][y1 + 1] != 'H')
    else:  # Vertical
        return (x1 + 1 < m and
                grid[x1][y1] != 'H' and
                grid[x1 + 1][y1] != 'H' and
                grid[x1][y1 + 1] != 'H' and
                grid[x1 + 1][y1 + 1] != 'H')

def rotate(current):
    x1, y1 = current.x1, current.y1
    return State(x1, y1, x1, y1 + 1, current.steps + 1)  # Rotate to vertical position

def min_steps(grid, m, n):
    start = None
    target = None

    # Locate the starting and target positions
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 's':
                start = State(i, j, i, j + 1, 0)
            if grid[i][j] == 'S':
                target = State(i, j, i, j + 1, 0)

    if start is None or target is None:
        return -1

    # BFS for shortest path
    queue = deque([start])
    visited = set([start])

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        current = queue.popleft()

        # Check if we've reached the target
        if ((current.x1 == target.x1 and current.y1 == target.y1 and
             current.x2 == target.x2 and current.y2 == target.y2) or
            (current.x1 == target.x2 and current.y1 == target.y2 and
             current.x2 == target.x1 and current.y2 == target.y1)):
            return current.steps

        # Try moving in all 4 directions
        for dx, dy in directions:
            nx1, ny1 = current.x1 + dx, current.y1 + dy
            nx2, ny2 = current.x2 + dx, current.y2 + dy

            if is_valid(nx1, ny1, nx2, ny2, grid, m, n):
                next_state = State(nx1, ny1, nx2, ny2, current.steps + 1)
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)

        # Try rotating the sofa if in a 2x2 area
        if can_rotate(current, grid, m, n):
            rotated = rotate(current)
            if rotated not in visited:
                visited.add(rotated)
                queue.append(rotated)

    return -1  # Impossible to move the sofa

def main():
    m, n = map(int, input().split())
    grid = [input().split() for _ in range(m)]

    result = min_steps(grid, m, n)
    print("Impossible" if result == -1 else result)

if __name__ == "__main__":
    main()