class SimpleCounter:
    def __init__(self, goal = 1):
        self.count = 0
        self.goal = goal
        self.done = False

    def reset(self):
        self.count = 0
        self.done = False

    def increase(self, amount):
        self.count += amount
        if(self.count >= self.goal):
            self.done = True