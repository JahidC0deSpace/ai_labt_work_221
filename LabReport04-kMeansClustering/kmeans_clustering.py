import random

NUM_POINTS = 100
NUM_CLUSTERS = 10
GRID_SIZE = 20  

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None

class KMeans:
    def __init__(self, num_points, num_clusters, grid_size):
        self.num_points = num_points
        self.num_clusters = num_clusters
        self.grid_size = grid_size
        self.points = [Point(random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)) for _ in range(num_points)]
        self.centers = [Point(random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)) for _ in range(num_clusters)]
        self.run()

    def manhattan_distance(self, a, b):
        return abs(a.x - b.x) + abs(a.y - b.y)

    def assign_clusters(self):
        for point in self.points:
            min_dist = float('inf')
            for idx, center in enumerate(self.centers):
                dist = self.manhattan_distance(point, center)
                if dist < min_dist:
                    min_dist = dist
                    point.cluster = idx

    def update_centers(self):
        new_centers = [Point(0, 0) for _ in range(self.num_clusters)]
        counts = [0] * self.num_clusters

        for point in self.points:
            idx = point.cluster
            new_centers[idx].x += point.x
            new_centers[idx].y += point.y
            counts[idx] += 1

        for i in range(self.num_clusters):
            if counts[i] > 0:
                self.centers[i].x = new_centers[i].x // counts[i]
                self.centers[i].y = new_centers[i].y // counts[i]

    def has_converged(self, prev_centers):
        for i in range(self.num_clusters):
            if self.centers[i].x != prev_centers[i].x or self.centers[i].y != prev_centers[i].y:
                return False
        return True

    def run(self):
        while True:
            self.assign_clusters()
            prev_centers = [Point(c.x, c.y) for c in self.centers]
            self.update_centers()
            if self.has_converged(prev_centers):
                break
        self.visualize()

    def visualize(self):
        grid = [['.' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        for p in self.points:
            grid[p.y][p.x] = 'P'

        for c in self.centers:
            grid[c.y][c.x] = 'C'

        print("\nData visualization(P=Point,C=Center):")
        for y in range(self.grid_size - 1, -1, -1):
            for x in range(self.grid_size):
                print(grid[y][x], end=' ')
            print()

if __name__ == "__main__":
    KMeans(NUM_POINTS, NUM_CLUSTERS, GRID_SIZE)
