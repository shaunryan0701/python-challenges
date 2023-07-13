from calendar import Calendar

class MyCalendar(Calendar):
    def __init__(self, firstweekday: int = 0) -> None:
        super().__init__(firstweekday)


        