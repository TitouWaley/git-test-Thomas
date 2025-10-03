class Voiture:
    
    def __init__(self, v_max : int):
        self.vmax = v_max
        self.current_speed = 0
    
    def demarrer (self):
        print("Voiture a une vittes max de :",self.vmax)
    