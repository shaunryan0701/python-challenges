'''
Imagine that you are an automotive fan, and you are able to build a car from a limited set of components.

Your task is to :

define classes representing:
tires (as a bundle needed by a car to operate); 
methods available: get_pressure(), 
pump(); 
attribute available: size 
engine; 
methods available: start(), 
stop(), 
get_state(); 
attribute available: fuel type
vehicle; method available: __init__(VIN, engine, tires); attribute available: VIN
based on the classes defined above, create the following objects:
two sets of tires: city tires (size: 15), off-road tires (size: 18)
two engines: electric engine, petrol engine
instantiate two objects representing cars:
the first one is a city car, built of an electric engine and city tires
the second one is an all-terrain car build of a petrol engine and off-road tires
play with the cars by calling methods responsible for interaction with components.
'''

class Vehicle:
    def __init__(self, VIN, engine, tyres):
        self.VIN = VIN
        self.engine= engine
        self.tyres = tyres

class Tyres:
    def __init__(self, size) -> None:
        self.size = size
    
    def get_pressure(self):
        pass
    
    def pump(self):
        pass
    
class CityTyres(Tyres):
    def __init__(self) -> None:
        super().__init__('city')

class OffroadTyres(Tyres):
    def __init__(self) -> None:
        super().__init__('off_road')        

class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
    
    def start(self):
        print(f'Starting {self.__class__.__name__}')
    
    def stop(self):
        print(f'Stopping {self.__class__.__name__}')
     
class ElectricEngine(Engine):
    def __init__(self, fuel_type) -> None:
        super().__init__(fuel_type)


class DieselEngine(Engine):
    def __init__(self, fuel_type) -> None:
        super().__init__(fuel_type)

my_vehicle = Vehicle('1234asdf', ElectricEngine('Electric'), CityTyres())
my_vehicle.engine.start()