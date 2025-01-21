class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def full_name(self):
     return f"{self.brabd}{self.model}"
        
my_car = car("toyota","innova")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = car("tata", "safari")
print(my_new_car)