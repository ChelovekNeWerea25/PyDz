class Animal:
    name = "Амогус"

    def __init__(self, species):
        self.species = species
        self.printsgt()

    def printsgt(self):
        print(f"Зараз в світі {self.species} мільйонів видів різних тварин.")


class Insects(Animal):
    def __init__(self, age, species):
        self.age = age
        self.species = species
        self.print_insects()

    def print_insects(self):
        print(f"Середня протяжність життя комах {self.age} днів для {self.species} мільйонів видів.")


class Butterfly(Insects):
    def __init__(self, age, subspecies):
        self.age = age
        self.subspecies = subspecies
        self.printing()

    def printing(self):
        print(f"Цьому метелику якого звати {self.name} всього {self.age} днів подвид якого це {self.subspecies}")


'''
class Zenya(Human):
    def __init__(self, group, mark):
        self.group = group
        self.mark = mark

    def prntzenya(self):
        print(f"Вчитель веде групу {self.group} і поставив середню оцінку {self.mark}")
'''

h1 = Animal(8.7)
h2 = Insects(56, 1.5)
h3 = Butterfly(8, "Грета Ото")
