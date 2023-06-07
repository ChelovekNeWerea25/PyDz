class car:
    def sound(self):
        print("Бр-р-р-р-р!")


class Human:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f'{self.name} імітує звук машини. Бррррррррр')


a1 = car()
h = Human("Женя")
a1.sound()
h.sound()