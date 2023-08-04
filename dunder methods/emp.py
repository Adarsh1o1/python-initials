class emp:
    def __init__(self, name) -> None:
        self.name=name
    def __str__(self):
        return f"name is {self.name}"
    def __repr__(self):
        return f"the name {self.name}"
    def __call__(self):
        print(f"the instance is {self.name}")