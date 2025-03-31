class IDDFSMazeSolver:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.maze = []
        self.visited = []
        self.path = []
        self.max_depth = 0
        self.goal_found = False
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.maze[x][y] == 0

    def dls(self, x, y, target_x, target_y, depth):
        if x == target_x and y == target_y:
            self.path.append((x, y))
            self.goal_found = True
            return True
        
        if depth <= 0:
            return False

        self.visited[x][y] = True
        self.path.append((x, y))

        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            if self.is_valid(nx, ny) and not self.visited[nx][ny]:
                if self.dls(nx, ny, target_x, target_y, depth - 1):
                    return True

        self.path.pop()  # Backtrack if no path found from this cell
        self.visited[x][y] = False
        return False

    def iddfs(self, start_x, start_y, target_x, target_y):
        depth_limit = 0
        max_possible_depth = self.rows * self.cols  # Upper bound for search
        
        while depth_limit <= max_possible_depth and not self.goal_found:
            self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
            self.path = []
            if self.dls(start_x, start_y, target_x, target_y, depth_limit):
                return True
            depth_limit += 1
        
        return False

    def solve_maze(self):
        print("Enter the number of rows and columns (space separated):")
        self.rows, self.cols = map(int, input().split())
        
        print("Enter the maze (0 for empty, 1 for wall):")
        self.maze = []
        for _ in range(self.rows):
            row = list(map(int, input().split()))
            self.maze.append(row)
        
        print("Enter start coordinates (space separated):")
        start_x, start_y = map(int, input().split())
        
        print("Enter target coordinates (space separated):")
        target_x, target_y = map(int, input().split())

        if not self.is_valid(start_x, start_y) or not self.is_valid(target_x, target_y):
            print("Invalid start or target position (either wall or out of bounds)")
            return

        if self.iddfs(start_x, start_y, target_x, target_y):
            print(f"Path found at depth {len(self.path)-1} using IDDFS")
            print(f"Traversal Order: {self.path}")
        else:
            print(f"Path not found at max depth {self.rows*self.cols} using IDDFS")

if __name__ == "__main__":
    solver = IDDFSMazeSolver()
    solver.solve_maze()