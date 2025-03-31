class GraphColoring:
    def __init__(self, num_vertices, edges, num_colors):
        """
        Initialize the GraphColoring problem
        :param num_vertices: number of vertices in the graph
        :param edges: list of edges as tuples (u, v)
        :param num_colors: number of colors available
        """
        self.V = num_vertices
        self.num_colors = num_colors
        self.color = [0] * self.V
        self.edges = edges
        self.graph = self._build_adjacency_matrix()
        self.solution = None

    def _build_adjacency_matrix(self):
        """Convert edge list to adjacency matrix"""
        graph = [[0] * self.V for _ in range(self.V)]
        for u, v in self.edges:
            graph[u][v] = 1
            graph[v][u] = 1  # Undirected graph
        return graph

    def solve(self):
        """Main function to solve the graph coloring problem"""
        if not self._solve_util(0):
            print("Coloring Not Possible with", self.num_colors, "Colors")
            return False
        
        print("Coloring Possible with", self.num_colors, "Colors")
        print("Color Assignment:", self.solution)
        return True

    def _solve_util(self, vertex):
        """
        Recursive utility function to solve the problem
        :param vertex: current vertex being colored
        """
        if vertex == self.V:
            self.solution = self.color.copy()
            return True

        for color in range(1, self.num_colors + 1):
            if self._is_safe(vertex, color):
                self.color[vertex] = color
                if self._solve_util(vertex + 1):
                    return True
                self.color[vertex] = 0

        return False

    def _is_safe(self, vertex, color):
        """
        Check if current color assignment is safe
        :param vertex: vertex being colored
        :param color: proposed color
        """
        for neighbor in range(self.V):
            if self.graph[vertex][neighbor] == 1 and self.color[neighbor] == color:
                return False
        return True


def read_input(filename):
    """Read input from file and return graph data"""
    with open(filename, 'r') as file:
        lines = file.readlines()
        N, M, K = map(int, lines[0].strip().split())
        edges = []
        for line in lines[1:M+1]:
            u, v = map(int, line.strip().split())
            edges.append((u, v))
    return N, edges, K


def main():
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python graph_coloring.py <input_file>")
        return
    
    input_file = sys.argv[1]
    
    try:
        N, edges, K = read_input(input_file)
        gc = GraphColoring(N, edges, K)
        gc.solve()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error processing input: {str(e)}")


if __name__ == "__main__":
    main()