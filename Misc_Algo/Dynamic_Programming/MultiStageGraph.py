class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]
        self.adj_matrix = [[float('inf')] * vertices for _ in range(vertices)]
        for i in range(vertices):
            self.adj_matrix[i][i] = 0

    def add_edge(self, u, v, weight, directed=True):
        self.adj_list[u].append((v, weight))
        self.adj_matrix[u][v] = weight
        if not directed:
            self.adj_list[v].append((u, weight))
            self.adj_matrix[v][u] = weight

    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(row)

    def print_adj_list(self):
        for idx, adj in enumerate(self.adj_list):
            print(f'{idx}: {adj}')

    def find_least_costly_path(self):
        # Initialize cost and path arrays
        cost = [float('inf')] * self.vertices
        cost[-1] = 0  # Cost to reach the last node from itself is 0
        d = [-1] * self.vertices  # To store the next node in the path
        path = []

        # Calculate the minimum cost path using dynamic programming
        for i in range(self.vertices - 2, -1, -1):
            min_cost = float('inf')
            for j in range(i + 1, self.vertices):
                if self.adj_matrix[i][j] != float('inf'):
                    if self.adj_matrix[i][j] + cost[j] < min_cost:
                        min_cost = self.adj_matrix[i][j] + cost[j]
                        d[i] = j
            cost[i] = min_cost

        # Construct the path
        current_node = 0
        while current_node != -1:
            path.append(current_node)
            current_node = d[current_node]

        # Output results
        print("Adjacency Matrix:")
        self.print_adj_matrix()
        print("\nAdjacency List:")
        self.print_adj_list()
        print("\nMinimum cost:", cost[0])
        print("Path:", path)


# # Test Case
# # Define the number of stages and nodes in each stage
# stages = [1, 2, 3, 2, 1]  # Number of nodes in each stage

# # Create a graph instance with total nodes being the sum of nodes in all stages
# num_nodes = sum(stages)
# graph = Graph(num_nodes)

# # Add predefined edges and weights manually
# # Stage 0 to Stage 1
# graph.add_edge(0, 1, 3)  # A → B1
# graph.add_edge(0, 2, 2)  # A → B2

# # Stage 1 to Stage 2
# graph.add_edge(1, 3, 5)  # B1 → C1
# graph.add_edge(1, 4, 6)  # B1 → C2
# graph.add_edge(2, 3, 4)  # B2 → C1
# graph.add_edge(2, 4, 3)  # B2 → C2
# graph.add_edge(2, 5, 7)  # B2 → C3

# # Stage 2 to Stage 3
# graph.add_edge(3, 6, 2)  # C1 → D1
# graph.add_edge(3, 7, 1)  # C1 → D2
# graph.add_edge(4, 6, 6)  # C2 → D1
# graph.add_edge(4, 7, 5)  # C2 → D2
# graph.add_edge(5, 6, 8)  # C3 → D1
# graph.add_edge(5, 7, 7)  # C3 → D2

# # Stage 3 to Stage 4
# graph.add_edge(6, 8, 3)  # D1 → E
# graph.add_edge(7, 8, 4)  # D2 → E

# # Call the method to find and print the least costly path
# graph.find_least_costly_path()
