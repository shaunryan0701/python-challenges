'''
Create a class representing a time interval;
the class should implement its own method for addition, subtraction on time interval class objects;
the class should implement its own method for multiplication of time interval class objects 
by an integer-type value;
the __init__ method should be based on keywords to allow accurate and convenient object initialization, 
but limit it to hours, minutes, and seconds parameters;
the __str__ method should return an HH:MM:SS string, where 
HH represents hours, 
MM represents minutes and 
SS represents the seconds 
attributes of the time interval object;
check the argument type, and in case of a mismatch, raise a TypeError exception.
'''

class TimeInterval:
    def __init__(self, **components) -> None:
        self.hour = 0
        self.minute = 0
        self.second = 0

        for time_component, time_value in components.items():
            if time_component == "hours":
                self.hour = time_value
            elif time_component == "minutes":
                self.minute = time_value
            elif time_component == "seconds":
                self.second = time_value
    
    def __str__(self) -> str:
        return f'{self.hour}:{self.minute}:{self.second}'
    
    def __add__(self, other):
        self_seconds = self.hour * 60 * 60
        self_minutes = self.minute * 60
        self_total = self_seconds + self_minutes + self.second

        other_seconds = other.hour * 60 * 60
        other_minutes = other.minute * 60
        other_total = other_seconds + other_minutes + other.second

        total_secoonds = self_total + other_total

        hour_component = total_secoonds // 3600
        seconds_component = total_secoonds % 60

        return f'{hour_component}:{10}:{seconds_component}'
    

time_1 = TimeInterval(hours=1, minutes=58, seconds=17)
time_2 = TimeInterval(hours=2, minutes=8, seconds=34)

print(time_1)
print(time_2)

print(time_1 + time_2)