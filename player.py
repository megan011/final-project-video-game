class Player:
    def __init__(self): 
        self.speed = 0 
        self.score = 0 
        self.health = 100
        self.progress = []
    
    def increase_speed(self): 
        self.speed += 7
    
    def decrease_speed(self): 
        self.speed -= 7  

    def current_speed(self): 
        return self.speed 
    
    def progress(self): 
        self.progress.append({"speed": self.speed, "health": self.health}) 