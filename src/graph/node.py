class Node:
    def __init__(self, n):
        self.name = n
        self.adjacencies = set()
        self.parent = None
        self.distance = 0

    def __repr__(self):
        return f"{self.name} - {self.adjacencies}"

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)
