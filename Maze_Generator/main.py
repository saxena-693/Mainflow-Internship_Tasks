import random
import sys
sys.setrecursionlimit(10000)

# Maze characters
WALL = '#'
PATH = ' '
START = 'S'
END = 'E'
VISITED = '.'

def create_empty_maze(rows, cols):
    """Initializes a maze filled with walls."""
    maze = [[WALL for _ in range(cols)] for _ in range(rows)]
    return maze

def generate_maze(maze, x, y):
    """Recursive backtracking maze generation."""
    directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 1 <= nx < len(maze) - 1 and 1 <= ny < len(maze[0]) - 1:
            if maze[nx][ny] == WALL:
                maze[nx][ny] = PATH
                maze[x + dx // 2][y + dy // 2] = PATH
                generate_maze(maze, nx, ny)

def print_maze(maze):
    """Display the maze in terminal."""
    for row in maze:
        print(''.join(row))

def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == START:
                return i, j
    return None

def dfs_solve_maze(maze, x, y, end_x, end_y, visited):
    if not (0 <= x < len(maze) and 0 <= y < len(maze[0])):
        return False
    if maze[x][y] == WALL or visited[x][y]:
        return False
    if (x, y) == (end_x, end_y):
        return True

    visited[x][y] = True
    maze[x][y] = VISITED

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if dfs_solve_maze(maze, x + dx, y + dy, end_x, end_y, visited):
            return True

    # Optional: comment below to see full trace path
    maze[x][y] = PATH
    return False

def build_and_run_maze(rows=21, cols=21):
    # Ensure odd dimensions for path carving
    rows = rows if rows % 2 == 1 else rows + 1
    cols = cols if cols % 2 == 1 else cols + 1

    maze = create_empty_maze(rows, cols)

    # Start generation at (1, 1)
    maze[1][1] = PATH
    generate_maze(maze, 1, 1)

    # Set Start and End
    maze[1][1] = START
    maze[rows - 2][cols - 2] = END

    print("Generated Maze:")
    print_maze(maze)

    # Solve the maze
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    print("\nSolving Maze...\n")
    dfs_solve_maze(maze, 1, 1, rows - 2, cols - 2, visited)

    print("Solved Maze:")
    print_maze(maze)

# Run the maze program
if __name__ == "__main__":
    build_and_run_maze(rows=21, cols=41)  # You can change the size here
