from collections import deque

def get_moves(x, y):
    return [(x, y), (y, -x), (-y, x), (-x, -y)]

def is_valid(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0

def bfs(grid, source, destination, x, y):
    M, N = len(grid), len(grid[0])
    queue = deque([(source[0], source[1], 0)])
    visited = set()
    visited.add((source[0], source[1]))
    moves = get_moves(x, y)
    
    while queue:
        row, col, steps = queue.popleft()
        if (row, col) == (destination[0], destination[1]):
            return steps
        
        for dx, dy in moves:
            new_row, new_col = row + dx, col + dy
            if is_valid(grid, new_row, new_col) and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, steps + 1))
    
    return -1

# Input grid dimensions
M, N = map(int, input().split())

# Input the grid
grid = [list(map(int, input().split())) for _ in range(M)]

# Input source and destination
source = tuple(map(int, input().split()))
destination = tuple(map(int, input().split()))

# Input move constraints
x, y = map(int, input().split())

# Output the result
print(bfs(grid, source, destination, x, y), end='')
