class Vulnerability:
    def __init__(self, name, description, rank):
        self.name = name
        self.description = description
        self.rank = rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def increase_rank(self):
        self.rank += 1

    def decrease_rank(self):
        if self.rank > 0:
            self.rank -= 1