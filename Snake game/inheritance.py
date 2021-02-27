class Animal:
    def __init__(self):
        self.num_eyes=2

    def breathe(self):
        print("Inhale,Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()  # Here animal is the super class. and this line and the above line inherits the all attributes and methods from super class i.e. Animal.
    
    def breathe(self):
        super().breathe()  #This means we are going to do everything that breathe() func in super class does but afterward we are going to do something extra.
        print("Doing this underwater.")              

    def swim(self):
        print("Moving in water.")

jane=Fish()
jane.swim()
jane.breathe() 
print(jane.num_eyes)