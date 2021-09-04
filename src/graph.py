import random
from math import inf
from src.edge import Edge
from src.node import GraphNode
import heapq

# random.seed(20)


class Graph:
    def __init__(self, nodes=None):
        self.nodes = nodes or {}

    def __repr__(self):
        return "\n".join([repr(self.nodes[n]) for n in self.nodes])

    def initialize_single_soruce(self, src):
        """
        Set all node's distance value to infinity
        Then sets source node src distance to 0 
        used in single source shortest path problem
        """
        for node in self.nodes.values():
            node.distance = inf
        self.nodes[src].distance = 0

    @classmethod
    def init_random_graph(cls, n=10, max_weight=50, undirected=True):
        """
        Generate a graph with random edges/weights
        Either directed or undirected
        """
        g = {i: GraphNode(i) for i in range(1, n + 1)}

        for i in range(n):
            src = random.randint(1, n)
            dest = random.randint(1, n)
            while src == dest:
                dest = random.randint(1, n)
            weight = random.randint(1, max_weight)
            g[src].adjacencies.add(Edge(src, dest, weight))
            if undirected:
                g[dest].adjacencies.add(Edge(dest, src, weight))

        return Graph(g)

    def dijkstra(self, src, dest):
        """
        src: source node - int
        dest: source node - int
        """

        def relax(src, dest, weight):
            if dest.distance > src.distance + weight:
                dest.distance = src.distance + weight
                dest.parent = src

        if src not in self.nodes:
            raise ValueError(f"src {src} not in nodes")
        if dest not in self.nodes:
            raise ValueError(f"dest {dest} not in nodes")
        self.initialize_single_soruce(src)
        min_heap = [
            (self.nodes[n].distance, idx, self.nodes[n])
            for idx, n in enumerate(self.nodes)
        ]
        heapq.heapify(min_heap)
        while min_heap:
            u = heapq.heappop(min_heap)[2]
            for edge in u.adjacencies:
                relax(self.nodes[edge.src], self.nodes[edge.dest], edge.weight)
        if self.nodes[dest].distance == inf:
            print(f"Node {dest} is unreachable from Node {src}")
            return

        print(f"Shortest Path Cost from {src} to {dest}")
        print(f"Cost: {self.nodes[dest].distance}")
        path = [dest]
        p = self.nodes[dest].parent
        while p:
            path.append(p.value)
            p = p.parent
        print("Shortest Path:")
        print(" ".join([str(n) for n in path]))
        return path
