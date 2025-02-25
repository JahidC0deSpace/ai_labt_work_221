import random

class Node:
    def __init__(self, a, b, depth):
        self.x = a
        self.y = b
        self.depth = depth

class DFS:
    def __init__(self, N):
        self.N = N
        self.grid = [[random.choice(['.', '#']) for _ in range(N)] for _ in range(N)]
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.found = False
        self.path = []
        self.topological_order = []
        self.source = self.get_random_empty_cell()
        self.goal = self.get_random_empty_cell()
        while self.source == self.goal:
            self.goal = self.get_random_empty_cell()

    def get_random_empty_cell(self):
        while True:
            r, c = random.randint(0, self.N - 1), random.randint(0, self.N - 1)
            if self.grid[r][c] == '.':
                return (r, c)

    def dfs(self, x, y, visited):
        if (x, y) in visited:
            return
        visited.add((x, y))
        self.topological_order.append((x, y))
        if (x, y) == self.goal:
            self.found = True
            return
        
        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.N and 0 <= ny < self.N and self.grid[nx][ny] == '.' and (nx, ny) not in visited:
                self.dfs(nx, ny, visited)
                if self.found:
                    self.path.append((nx, ny))
                    return

    def find_path(self):
        visited = set()
        self.dfs(self.source[0], self.source[1], visited)
        if self.found:
            self.path.append(self.source)
            self.path.reverse()
        
    def print_grid(self):
        for r in range(self.N):
            for c in range(self.N):
                if (r, c) == self.source:
                    print('S', end=' ')
                elif (r, c) == self.goal:
                    print('G', end=' ')
                elif (r, c) in self.path:
                    print('*', end=' ')
                else:
                    print(self.grid[r][c], end=' ')
            print()

    def run(self):
        self.find_path()
        print("Generated Grid:")
        self.print_grid()
        print("\nSource:", self.source)
        print("Goal:", self.goal)
        print("DFS Path:", self.path)
        print("Topological Order of DFS Traversal:", self.topological_order)

if __name__ == "__main__":
    N = random.randint(4, 7)
    dfs_solver = DFS(N)
    dfs_solver.run()
