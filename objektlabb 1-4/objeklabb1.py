<<<<<<< HEAD
class Car():
    def __init__(self,name :str, model :str, engine: str):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
     return f'This is{self.name} {self.model} with engine {self.engine}'


car = Car('volvo',"240", "1.6L")
print(car.get_info())
=======
class Car():
    def __init__(self,name :str, model :str, engine: str):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
     return f'This is{self.name} {self.model} with engine {self.engine}'


car = Car('volvo',"240", "1.6L")
print(car.get_info())
>>>>>>> 83187f189bd2a7b08390ef3c66e7a80b0cc5b1f1
