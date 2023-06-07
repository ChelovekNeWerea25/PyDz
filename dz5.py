class car:
    def __init__(self, marka, litr, age):
        self.__litr = None
        self.__age = None
        self.marka = marka
        self.set_age(age)
        self.set_litr(litr)
        self.printing()

    def printing(self):
        print(f"Марка машини {self.marka} в неї {self.__litr}л в баці, та {self.__age} років машині після покупки")

    def get_litr(self):
        return self.__litr

    def set_litr(self, lit):
        if lit >= 0:
            self.__litr = lit
        else:
            self.__litr = lit / -1

    def get_age(self):
        return self.__age

    def set_age(self, ag):
        if ag >= 0:
            self.__age = ag
        else:
            self.__age = int(ag / -1)


h = car("BMW", 20, -2)
