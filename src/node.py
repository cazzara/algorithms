class Node:
    def __init__(self, n):
        self.name = n

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


class GraphNode(Node):
    def __init__(self, n):
        super(self, GraphNode).__init__(n)
        self.adjacencies = set()
        self.parent = None
        self.distance = 0

    def __repr__(self):
        return f"{self.name} - {self.adjacencies}"


class TreeNode(Node):
    def __init__(self, n):
        super(self, TreeNode).__init__(n)
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.name}"
