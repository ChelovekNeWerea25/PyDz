class Human:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, brand, color, number):
        self.brand = brand
        self.color = color
        self.number = number
        self.passengers = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers(self):
        if self.passengers:
            print(f"\nВ автобусі марки {self.brand} з гос номером '{self.number}' та кольором '{self.color}' є "
                  f"наступні пасажири:")
            for passenger in self.passengers:
                print(passenger.name, end=" ")
        else:
            print(f"\nВ автобусі марки {self.brand} з гос номером '{self.number}' та кольором '{self.color}' немає "
                  f"пасажирів")


bus1 = Bus("Абобус", "Жовтий", "BI3587AG")
bus2 = Bus("Мерседес", "Синій", "BI4576YY")
bus3 = Bus("Ікарус", "Білий", "BI7587CH")

bus1_passenger_count = int(input("Введіть кількість пасажирів для автобуса 1: "))
for i in range(bus1_passenger_count):
    passenger_name = input(f"Введіть ім'я пасажира {i + 1}: ")
    bus1.add_passenger(Human(passenger_name))

bus2_passenger_count = int(input("Введіть кількість пасажирів для автобуса 2: "))
for i in range(bus2_passenger_count):
    passenger_name = input(f"Введіть ім'я пасажира {i + 1}: ")
    bus2.add_passenger(Human(passenger_name))

bus3_passenger_count = int(input("Введіть кількість пасажирів для автобуса 3: "))
for i in range(bus3_passenger_count):
    passenger_name = input(f"Введіть ім'я пасажира {i + 1}: ")
    bus3.add_passenger(Human(passenger_name))

bus1.print_passengers()
bus2.print_passengers()
bus3.print_passengers()
