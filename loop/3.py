class car:
    def __init__(self,brand,model):
        self.brand =brand
        self.model = model
    def full_name(self):
     return f"{self.brabd}{self.model}"
 
 
Class electricar(car):
     def __init__(self, brand, model,battery_size):
         super().__init__(brand, model)
         self.battery_size = battery_size
         
my_tesla = electricar("Tesla", "Model S", "85kWh")
print(my_tesla)