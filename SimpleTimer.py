class SimpleTimer:
    def __init__(self, timer_duration = 1):
        self.duration = timer_duration
        self.time_passed = 0
        self.done = False

    def update(self, delta_time):
        self.time_passed += delta_time
        if(self.time_passed >= self.duration):
            self.done = True

    def reset(self):
        self.time_passed = 0
        self.done = False
        
        