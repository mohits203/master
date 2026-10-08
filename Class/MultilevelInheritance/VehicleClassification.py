class Vehicle:

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def vehicleInfo(self):
        print(f"Vehicle maker is : {self.make}")
        print(f"Vehicle model is : {self.model}")

class Car(Vehicle):

    def __init__(self, make: str, model: str, seatingCapacity: int):
        super().__init__(make, model)
        self.seatingCapacity = seatingCapacity

    def displayCarInfo(self):
        self.vehicleInfo()
        print(f"Vehicle seating capacity is :{self.seatingCapacity}")

class ElectricCar(Car):

    def __init__(self, make: str, model: str, seatingCapacity: int, batteryCapacity: float):
        super().__init__(make, model, seatingCapacity)
        self.batteryCapacity = batteryCapacity

    def displayElectricCarInfo(self):
        self.displayCarInfo()
        print(f"Battery Capacity : {self.batteryCapacity}")

make = input("Enter car maker : ")
model = input("Enter car Model : ")
seatingCapacity = int(input("Enter car seating capacity : "))
batteryCapacity = float(input("Enter car battery capacity"))

obj = ElectricCar(make, model, seatingCapacity, batteryCapacity)
obj.displayElectricCarInfo()
