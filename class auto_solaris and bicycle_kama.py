class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed


class Car(Vehicle):
    def __init__(self, name, max_speed, number_doors, model):
        super().__init__(name, max_speed)
        self.number_doors = number_doors
        self.model = model


    def engine_start(self):
        self.run = True

    def engine_stop(self):
        self.run = False


    def sound(self):
        return f"В автомобиле имеется сигнал  бип-бип"

    def info(self):
        return  (f"Автомобиль {self.name}"
         f" его максимальная скорость по трассе {self.max_speed}, \nмодель "
         f"{self.model}, а также количество дверей в данном"
         f" сидане {self.number_doors}.{self.sound()}.")

class Bicycle(Vehicle):
    def __init__(self, name, max_speed, frame_type, numbers_pedals):
        super().__init__(name, max_speed)
        self.frame_type = frame_type
        self.numbers_pedals = numbers_pedals


    def pedal(self):
        return f"Велосипед {self.name}, совершает движения с помощью педалей вперед-назад"


    def info(self):
        return (f"{self.pedal()}, максимальная скорость: {self.max_speed} км, тип: {self.frame_type}, " \
               f"количество педалей: {self.numbers_pedals}.")



car = Car("hyundai", 180, 4, "solaris")
car.engine_start()
if car.run == True:
    print(f"Ваш автомобиль заведен. {car.info()}")
else:
    print(f"Ваш автомобиль не заведен. {car.info()}")

bicycle = Bicycle("kama", 30, "lite", 2)
print(bicycle.info())