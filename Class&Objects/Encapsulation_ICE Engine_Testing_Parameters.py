# BMW Testing vehicle engine parameters
# BMW ECU Simulation mode

class BMW_ECU:
    def __init__(self,rpm,coolant_temp,oil_pressure,fuel_level):
        self.__rpm=int(rpm)                                     # RPM in numbers
        self.__coolant_temp=int(coolant_temp)                   # Coolant temp in degree celcius 
        self.__oil_pressure=int(oil_pressure)                   # Oil pressure in psi(pounds per square inch)
        self.__fuel_level=int(fuel_level)                       # Fuel level in %

    def get_values(self):
        return self.__rpm,self.__coolant_temp,self.__oil_pressure,self.__fuel_level

    def validate_rpm(self,updated_rpm):
        if updated_rpm>=600 and updated_rpm<=7000:
            return "RPM OKAY"
        return "RPM ERROR"
    def validate_coolant_temp(self,updated_coolant_temp):
        if updated_coolant_temp>=-20 and updated_coolant_temp<=120:
            return "COOLANT TEMP OKAY"
        return "COOLANT TEMP ERROR"
    def validate_oil_pressure(self,updated_oil_pressure):
        if updated_oil_pressure>=20 and updated_oil_pressure<=80:
            return "OIL PRESSURE OKAY"
        return "OIL PRESSURE ERROR"
    def validate_fuel_level(self,updated_fuel_level):
        if updated_fuel_level>=0 and updated_fuel_level<=100:
            return "FUEL LEVEL OKAY"
        return "FUEL LEVEL ERROR"
    

    def set_values(self,updated_rpm,updated_coolant_temp,updated_oil_pressure,updated_fuel_level):
        updated_rpm=int(updated_rpm)
        updated_coolant_temp=int(updated_coolant_temp)
        updated_oil_pressure=int(updated_oil_pressure)
        updated_fuel_level=int(updated_fuel_level)

# Validation Check
        rpm_status=self.validate_rpm(updated_rpm)
        coolant_temp_status=self.validate_coolant_temp(updated_coolant_temp)
        oil_pressure_status=self.validate_oil_pressure(updated_oil_pressure)
        fuel_level_status=self.validate_fuel_level(updated_fuel_level)

    

# Block update if any parameter is unsafe
        if rpm_status !="RPM OKAY":
            return rpm_status
        if coolant_temp_status !="COOLANT TEMP OKAY":
            return coolant_temp_status
        if oil_pressure_status !="OIL PRESSURE OKAY":
            return oil_pressure_status
        if fuel_level_status !="FUEL LEVEL OKAY":
            return fuel_level_status

# Pass the parameters if all validation pass
        self.__rpm=int(updated_rpm)
        self.__coolant_temp=int(updated_coolant_temp)
        self.__oil_pressure=int(updated_oil_pressure)
        self.__fuel_level=int(updated_fuel_level)

        return "UPDATED SUCESSFULLY"
    

bmw_testing=BMW_ECU(2000,50,40,80)
# print(bmw_testing.get_values())

result=bmw_testing.set_values(5500,75,450,90)
print(result)
print(bmw_testing.get_values())
        