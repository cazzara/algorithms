class Edge:
    def __init__(self, s, d, w):
        self.src = s
        self.dest = d
        self.weight = w

    def __repr__(self):
        return f"({self.src}) --- {self.weight} ---> ({self.dest})"

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return (self.weight == other.weight and
               self.src == other.src and 
               self.dest == other.dest)

    def __hash__(self):
        return hash(self.src) + hash(self.dest) + hash(self.weight)