class Graph:
    def __init__(self, directed=False):
        self.graph = {}  # adjacency list
        self.directed = directed

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, u, v):
        self.add_node(u)
        self.add_node(v)
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def dfs_recursive(self, node, visited=None):
        if visited is None:
            visited = set()
        visited.add(node)
        print(node, end=' ')
        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def dfs_iterative(self, start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                stack.extend(reversed(self.graph.get(node, [])))

    def dfs_search(self, start, target, visited=None):
        if visited is None:
            visited = set()
        if start == target:
            print(f"Found target: {target}")
            return True
        visited.add(start)
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                if self.dfs_search(neighbor, target, visited):
                    return True
        return False

    def has_cycle(self):
        visited = set()
        if self.directed:
            rec_stack = set()
            def dfs(node):
                visited.add(node)
                rec_stack.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        if dfs(neighbor):
                            return True
                    elif neighbor in rec_stack:
                        return True
                rec_stack.remove(node)
                return False
        else:
            def dfs(node, parent):
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        if dfs(neighbor, node):
                            return True
                    elif neighbor != parent:
                        return True
                return False

        for node in self.graph:
            if node not in visited:
                if self.directed:
                    if dfs(node):
                        return True
                else:
                    if dfs(node, None):
                        return True
        return False
