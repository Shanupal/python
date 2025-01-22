class car:
    def __init__(self,brand,model):
        self.brand =brand
        self.model = model
    def full_name(self):
     return f"{self.brabd}{self.model}"
 
 
class electricar(car):
     def __init__(self, brand, model,battery_size):
         super().__init__(brand, model)
         self.battery_size = battery_size
     def fulltypr():
         return "electric charge"
             

my_tesla = electricar("Tesla", "Model S", "85kWh")
print(my_tesla.model)
print(my_tesla.fuel_type())
