class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
my_car = car("toyota","innova")
print(my_car.brand)
print(my_car.model)

my_new_car = car("tata", "safari")
print(my_new_car)