class Job:
    def __init__(self, s, f):
        self.start = s
        self.finish = f

    def __repr__(self):
        return f"({self.start}, {self.finish})"

    def is_compatible(other):
        return self.start >= other.finish or self.finish <= other.start
