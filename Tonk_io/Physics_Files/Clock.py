class Clock:

    time = 0
    
    def tick(self):
        time
        time += 1
        
    def transition(self, frame_duration):
        if time % frame_duration == 0:
            return True
