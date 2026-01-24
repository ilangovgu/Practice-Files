# Class and objects
# Software representation of a the physical system(Digital twin concept)

class ElectricVehicle:
    def __init__(self,name,battery_kwh,range_km):
        self.name=name
        self.battery_kwh=battery_kwh
        self.range_km=range_km
    def drive(self):
        print(self.name,"-Driving the car")
    def charge(self):
        print(self.name,"-Charge the battery")

Tesla=ElectricVehicle("Tesla model 3",82,600)
Mahindra=ElectricVehicle("Mahindra EV",79,683)
Toyota=ElectricVehicle("Toyota Camry",75,585)

Tesla.drive()
