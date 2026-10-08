class Vehicle:

    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def showVehicleInfo(self):
        print(f"Maker company : {self.make}")
        print(f"Model : {self.model}")
        print(f"Make year : {self.year}")

class FuelEfficiency(Vehicle):

    def __init__(self, make: str, model: str, year: int, distanceTraveled: int, fuelConsumed: int):
        super().__init__(make, model, year)
        self.distanceTraveled = distanceTraveled
        self.fuelConsumed = fuelConsumed

    def mileage(self):
        self.showVehicleInfo()
        return distanceTraveled/fuelConsumed

class MaintenanceCost(Vehicle):

    def __init__(self, make: str, model: str, year: int, services: int, costPerService: float):
        super().__init__(make, model, year)
        self.services = services
        self.costPerService = costPerService

    def totalMaintenanceCost(self):
        self.showVehicleInfo()
        return round(services * costPerService, 2)

make = input("Enter Vehicle maker : ")
model = input("Enter the vehicle model : ")
year = int(input("Enter the year : "))

distanceTraveled = int(input("Enter distance traveled by vehicle in KM : "))
fuelConsumed = int(input("Enter fuel consumed in liter: "))

services = int(input("Enter total services : "))
costPerService = int(input("Enter cost per service : "))

obj = FuelEfficiency(make, model, year, distanceTraveled, fuelConsumed)

print(f"Vehicle mileage is : {obj.mileage()}")

obj1 = MaintenanceCost(make, model, year, services, costPerService)

print(f"Total maintenance cost is : {obj1.totalMaintenanceCost()}")
