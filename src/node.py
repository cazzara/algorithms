class Node:
    def __init__(self, v):
        self.value = v
        self.parent = None


class GraphNode(Node):
    def __init__(self, n):
        super().__init__(n)
        self.adjacencies = set()
        self.distance = 0

    def __repr__(self):
        return f"{self.value} - {self.adjacencies}"

    def __eq__(self, other):
        return self.value == other.value



class TreeNode(Node):
    def __init__(self, n):
        super().__init__(n)
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.value}"

    def __eq__(self, other):
        return self.value == other.value and \
               self.left == other.left and \
               self.right == other.right and \
               self.parent == other.parent
