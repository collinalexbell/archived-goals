

class Goal:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline

    def __str__(self):
        return f"{self.name} with deadline: {self.deadline}"
