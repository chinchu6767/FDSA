class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_edge(self, u,v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append(v)

    def dfs(self, start_vertex):  
        visited = set()

        def dfs_recursive(vertex):
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                for neighbor in self.adjacency_list.get(vertex, []):
                    dfs_recursive(neighbor)

            dfs_recursive(start_vertex)  

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(2, 6)

    print("dfs Traversal starting from vertex 0:")
    graph.dfs(0)                 



    

    




