class Vehicle:#Superclass
    def __init__(self):
        self.type = input("Enter your Vehicle type such as Car or Truck: ")
class Automobile(Vehicle):#Subclass
    def year(self):
        return input("Enter the year of your vehicle: ")
    def make(self):
        return input("Enter the make of your vehicle: ")
    def model(self):
        return input("Enter the model of your vehicle: ")
    def doors(self):
        door_input = int(input("Does your vehicle have 2 or 4 doors? "))
        if door_input == 2:
            return "2 doors"
        elif door_input == 4:
            return "4 doors"
        else:
            return "please enter a valid input for number of doors"
    def roof(self):
        roof_input = input("Does your vehicle have a solid or sun roof?").lower() #added the lower method to make it more user friendly 
        if roof_input == "solid": 
            return "solid"
        elif roof_input == "sun":
            return "sun"
        else:
            return "please enter either sun or solid for roof type"
    def get_vehicle_info(self): #calls the class functions for user input
        vehicle_data = {
            "Type ":self.type,
            "Year ": self.year(),
            "Make ": self.make(),
            "Model ": self.model(),
            "Doors ": self.doors(),
            "Roof Type ": self.roof()

        }
        return vehicle_data
if __name__ == "__main__":
    auto = Automobile()
    vehicle_info = auto.get_vehicle_info()
    print("Vehicle Info:")
    for attribute, answer in vehicle_info.items():
        print(f"{attribute}: {answer}")
        



    