import heapq


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]
        self.adj_matrix = [[float('inf')] * vertices for _ in range(vertices)]
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i == j:
                    self.adj_matrix[i][j] = 0

    def add_edge(self, u, v, weight, directed=False):
        # For adjacency list
        if not directed:
            self.adj_list[v].append((u, weight))  # Undirected graph
        self.adj_list[u].append((v, weight))

        # For adjacency matrix
        if not directed:
            self.adj_matrix[v][u] = weight
        self.adj_matrix[u][v] = weight

    def print_adj_list(self):
        for u in range(self.vertices):
            print(f'Vertex {u}', end='\t')
            for v in range(len(self.adj_list[u])):
                print(
                    f'Node{v}[ End:{self.adj_list[u][0]} Dist:{self.adj_list[u][1]}]', end="\t")
            print()

    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(row)

    def prims_algorithm(self):
        min_heap = [(0, 0)]  # (weight, vertex)
        visited = [False] * self.vertices
        min_cost = 0
        edges = []

        while min_heap:
            weight, u = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True
            min_cost += weight
            if weight != 0:
                edges.append((prev, u, weight))

            for v, weight in self.adj_list[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (weight, v))
                    prev = u  # Previous vertex to track the edge

        return min_cost, edges

    def kruskals_algorithm(self):
        parent = list(range(self.vertices))
        rank = [0] * self.vertices

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
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

    def dijkstra_algorithm(self, start):
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
    
    def floyd_warshall_algorithm(self):
        dist = [row[:] for row in self.adj_matrix]

        for k in range(self.vertices):
            for i in range(self.vertices):
                for j in range(self.vertices):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist
    def bellman_ford_algorithm(self, start):
        # Initialize distances
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