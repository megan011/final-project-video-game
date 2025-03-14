class Health:
    def __init__(self, initial_health=100):
        self.health = initial_health

    def decrease_health (self,amount):
        self.health -= amount 
        if self.health <= 0: 
            self.health = 0 
        return self.health 

    def increase_health (self, amount): 
        self.health += amount
        if self.health > 100:
             self.health = 100 
        return self.health 