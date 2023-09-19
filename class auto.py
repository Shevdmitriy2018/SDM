class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed -= amount

    def get_speed(self):
        return f"brand: {self.brand}, model: {self.model}, year: {self.year}, speed: {self.speed}"

car = Car("hyundai", "solaris", "2015")
car.accelerate(80)
car.brake(20)
print(car.get_speed())
1111111111111
