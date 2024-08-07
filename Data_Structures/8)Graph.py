"""
Graph Implementation

A graph is a collection of nodes (vertices) connected by edges. Graphs can be directed or undirected,
and edges can have weights representing the cost or distance between nodes.

Operations:
1. **Add Edge**: Adds an edge from vertex u to vertex v with a specified weight. If directed is False, the edge is undirected.
2. **Print Adjacency List**: Prints the adjacency list representation of the graph.
3. **Print Adjacency Matrix**: Prints the adjacency matrix representation of the graph.
4. **Prims Algorithm**: Finds the Minimum Spanning Tree (MST) of the graph using Prim's algorithm.
5. **Kruskals Algorithm**: Finds the Minimum Spanning Tree (MST) of the graph using Kruskal's algorithm.
6. **Djikstra Algorithm**: Finds the shortest path from a starting vertex to all other vertices using Djikstra's algorithm.
7. **Floyd Warshall Algorithm**: Finds the shortest paths between all pairs of vertices using the Floyd-Warshall algorithm.
8. **Bellman Ford Algorithm**: Finds the shortest paths from a starting vertex to all other vertices using the Bellman-Ford algorithm.

Time Complexity:
- **Adding Edge**: O(1) for adjacency list and O(1) for adjacency matrix.
- **Printing Adjacency List**: O(V + E), where V is the number of vertices and E is the number of edges.
- **Printing Adjacency Matrix**: O(V^2).
- **Prim's Algorithm**: O(E log V) with a priority queue.
- **Kruskal's Algorithm**: O(E log V) due to sorting edges.
- **Djikstra's Algorithm**: O(E log V) with a priority queue.
- **Floyd-Warshall Algorithm**: O(V^3).
- **Bellman-Ford Algorithm**: O(VE).

Applications:
- Graphs are used in network routing, social networks, scheduling problems, and various optimization problems.

"""

import heapq
from typing import List, Tuple, Union


class Graph:
    """
    A class representing a graph.

    Attributes:
        vertices (int): The number of vertices in the graph.
        adj_list (List[List[Tuple[int, int]]]): Adjacency list representation of the graph.
        adj_matrix (List[List[float]]): Adjacency matrix representation of the graph.
    """

    def __init__(self, vertices: int):
        """
        Initialize the graph with a given number of vertices.

        Args:
            vertices (int): The number of vertices in the graph.
        """
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]
        self.adj_matrix = [[float('inf')] * vertices for _ in range(vertices)]
        for i in range(self.vertices):
            self.adj_matrix[i][i] = 0

    def add_edge(self, u: int, v: int, weight: int, directed: bool = False) -> None:
        """
        Add an edge to the graph.

        Args:
            u (int): The starting vertex of the edge.
            v (int): The ending vertex of the edge.
            weight (int): The weight of the edge.
            directed (bool): If True, the edge is directed from u to v. If False, the edge is undirected.
        
        Returns:
            None
        """
        # For adjacency list
        if not directed:
            self.adj_list[v].append((u, weight))  # Undirected graph
        self.adj_list[u].append((v, weight))

        # For adjacency matrix
        if not directed:
            self.adj_matrix[v][u] = weight
        self.adj_matrix[u][v] = weight

    def print_adj_list(self) -> None:
        """
        Print the adjacency list representation of the graph.

        Returns:
            None
        """
        for u in range(self.vertices):
            print(f'Vertex {u}', end='\t')
            for v, weight in self.adj_list[u]:
                print(f'Node{v}[ End:{weight} Dist:{weight}]', end="\t")
            print()

    def print_adj_matrix(self) -> None:
        """
        Print the adjacency matrix representation of the graph.

        Returns:
            None
        """
        for row in self.adj_matrix:
            print(row)

    def prims_algorithm(self) -> Tuple[int, List[Tuple[int, int, int]]]:
        """
        Find the Minimum Spanning Tree (MST) using Prim's algorithm.

        Returns:
            Tuple[int, List[Tuple[int, int, int]]]: The total weight of the MST and the edges in the MST.
        """

        """
        Prim's Algorithm

        Logic:
            Prim's algorithm is used to find the Minimum Spanning Tree (MST) of a connected, undirected graph. It starts from an arbitrary vertex and grows the MST by adding the smallest edge that connects a vertex in the MST to a vertex outside of it. This process is repeated until all vertices are included in the MST.

        Data Structure Used:
            - Priority Queue (Min-Heap): To efficiently select the edge with the smallest weight.

        Algorithm Used:
            - Greedy Algorithm: Always selects the minimum weight edge to build the MST.

        Use Case:
            - Prim's algorithm is useful for network design problems, such as designing the least-cost network to connect a set of nodes.
        """

        min_heap = [(0, 0)]  # (weight, vertex)
        visited = [False] * self.vertices
        min_cost = 0
        edges = []
        prev = [None] * self.vertices

        while min_heap:
            weight, u = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True
            min_cost += weight
            if prev[u] is not None:
                edges.append((prev[u], u, weight))

            for v, weight in self.adj_list[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (weight, v))
                    prev[v] = u  # Previous vertex to track the edge

        return min_cost, edges

    def kruskals_algorithm(self) -> Tuple[int, List[Tuple[int, int, int]]]:
        """
        Find the Minimum Spanning Tree (MST) using Kruskal's algorithm.

        Returns:
            Tuple[int, List[Tuple[int, int, int]]]: The total weight of the MST and the edges in the MST.
        """

        """
        Kruskal's Algorithm

        Logic:
            Kruskal's algorithm finds the Minimum Spanning Tree (MST) for a connected, undirected graph by sorting all edges by weight and adding the smallest edge to the MST, provided it does not form a cycle. The Union-Find data structure is used to detect and avoid cycles.

        Data Structure Used:
            - Union-Find (Disjoint Set): To manage and merge disjoint sets and detect cycles.

        Algorithm Used:
            - Greedy Algorithm: Chooses the smallest edge available that does not create a cycle.

        Use Case:
            - Kruskal's algorithm is suitable for sparse graphs where edge list representations are used, and it's beneficial in network design and optimization problems.
        """
        
        parent = list(range(self.vertices))
        rank = [0] * self.vertices

        def find(x: int) -> int:
            """
            Find the root of the set containing x.

            Args:
                x (int): The element to find.

            Returns:
                int: The root of the set containing x.
            """
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> None:
            """
            Union the sets containing x and y.

            Args:
                x (int): An element of the first set.
                y (int): An element of the second set.

            Returns:
                None
            """
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        edge_list = []
        for u in range(self.vertices):
            for v, weight in self.adj_list[u]:
                if u < v:  # Avoid duplicate edges
                    edge_list.append((weight, u, v))

        edge_list.sort()
        min_cost = 0
        mst_edges = []

        for weight, u, v in edge_list:
            if find(u) != find(v):
                union(u, v)
                min_cost += weight
                mst_edges.append((u, v, weight))

        return min_cost, mst_edges

    def djikstra_algorithm(self, start: int) -> List[float]:
        """
        Find the shortest path from a starting vertex to all other vertices using Djikstra's algorithm.

        Args:
            start (int): The starting vertex for the shortest path calculations.

        Returns:
            List[float]: The shortest distances from the starting vertex to all other vertices.
        """

        """
        Djikstra's Algorithm

        Logic:
            Djikstra's algorithm finds the shortest path from a single source vertex to all other vertices in a weighted graph with non-negative weights. It uses a priority queue to repeatedly select the vertex with the smallest distance and update the shortest path to its neighboring vertices.

        Data Structure Used:
            - Priority Queue (Min-Heap): To efficiently retrieve the vertex with the smallest distance.

        Algorithm Used:
            - Greedy Algorithm: Expands the shortest path incrementally.

        Use Case:
            - Djikstra's algorithm is commonly used in routing and navigation systems where shortest paths need to be computed in weighted graphs with non-negative weights.
        """

        dist = [float('inf')] * self.vertices
        dist[start] = 0
        min_heap = [(0, start)]  # (distance, vertex)
        visited = [False] * self.vertices

        while min_heap:
            d, u = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True
            for v, weight in self.adj_list[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(min_heap, (dist[v], v))

        return dist
    
    def floyd_warshall_algorithm(self) -> List[List[float]]:
        """
        Find the shortest paths between all pairs of vertices using the Floyd-Warshall algorithm.

        Returns:
            List[List[float]]: The shortest path distances between all pairs of vertices.
        """

        """
        Floyd-Warshall Algorithm

        Logic:
            The Floyd-Warshall algorithm finds the shortest paths between all pairs of vertices in a graph. It uses dynamic programming to iteratively improve the shortest paths by considering each vertex as an intermediate point.

        Data Structure Used:
            - 2D Matrix (Distance Matrix): To store shortest path estimates between all pairs of vertices.

        Algorithm Used:
            - Dynamic Programming: Updates shortest paths by considering intermediate vertices.

        Use Case:
            - Floyd-Warshall is applicable in scenarios where all-pairs shortest paths are required, such as in network analysis and routing problems where path information is needed for every vertex pair.
        """
        
        dist = [row[:] for row in self.adj_matrix]

        for k in range(self.vertices):
            for i in range(self.vertices):
                for j in range(self.vertices):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist

    def bellman_ford_algorithm(self, start: int) -> Union[List[float], None]:
        """
        Find the shortest paths from a starting vertex to all other vertices using the Bellman-Ford algorithm.

        Args:
            start (int): The starting vertex for the shortest path calculations.

        Returns:
            Union[List[float], None]: The shortest distances from the starting vertex to all other vertices if there are no negative-weight cycles; otherwise, None.
        """

        """
        Bellman-Ford Algorithm

        Logic:
            The Bellman-Ford algorithm finds the shortest path from a single source vertex to all other vertices in a weighted graph, handling graphs with negative weights. It iteratively relaxes all edges up to V-1 times and checks for negative-weight cycles in a final pass.

        Data Structure Used:
            - Array: To store the shortest path estimates.

        Algorithm Used:
            - Dynamic Programming: Updates shortest path estimates through edge relaxation.

        Use Case:
            - Bellman-Ford is useful in scenarios where the graph may contain negative weight edges and is commonly applied in financial systems and network routing to detect negative cycles that may be present.
        """

        distances = [float('inf')] * self.vertices
        distances[start] = 0

        # Relax edges up to V-1 times
        for _ in range(self.vertices - 1):
            for u in range(self.vertices):
                for v, weight in self.adj_list[u]:
                    if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight

        # Check for negative-weight cycles
        for u in range(self.vertices):
            for v, weight in self.adj_list[u]:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    print("Negative-weight cycle detected")
                    return None  # Or handle accordingly

        return distances

if __name__ == "__main__":
    # Create a graph with 5 vertices
    g = Graph(5)

    # Add edges
    g.add_edge(0, 1, 10)
    g.add_edge(0, 4, 3)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 4, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)

    # Print adjacency list
    print("Adjacency List:")
    g.print_adj_list()

    # Print adjacency matrix
    print("\nAdjacency Matrix:")
    g.print_adj_matrix()

    # Prim's Algorithm
    min_cost, edges = g.prims_algorithm()
    print(f"\nPrim's Algorithm:\nMinimum Cost: {min_cost}\nEdges in MST: {edges}")

    # Kruskal's Algorithm
    min_cost, mst_edges = g.kruskals_algorithm()
    print(f"\nKruskal's Algorithm:\nMinimum Cost: {min_cost}\nEdges in MST: {mst_edges}")

    # Djikstra's Algorithm from vertex 0
    distances = g.djikstra_algorithm(0)
    print(f"\nDjikstra's Algorithm (starting from vertex 0):\nDistances: {distances}")

    # Bellman-Ford Algorithm from vertex 0
    distances = g.bellman_ford_algorithm(0)
    print(f"\nBellman-Ford Algorithm (starting from vertex 0):\nDistances: {distances}")

    # Floyd-Warshall Algorithm
    dist_matrix = g.floyd_warshall_algorithm()
    print("\nFloyd-Warshall Algorithm:\nDistance Matrix:")
    for row in dist_matrix:
        print(row)