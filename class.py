class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"

class SUV(Car):
    def __init__(self, brand, model, year, awd):
        super().__init__(brand, model, year)
        self.awd = awd  # All-wheel drive feature
    
    def get_info(self):
        return f"{super().get_info()} - AWD: {'Yes' if self.awd else 'No'}"

# Example usage
car1 = Car("Toyota", "Corolla", 2022)
suv1 = SUV("Subaru", "Outback", 2023, True)

print(car1.get_info())
print(suv1.get_info())
