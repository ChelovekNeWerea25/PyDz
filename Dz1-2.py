from time import sleep
import random


class Cat:
    def __init__(self):
        self.name=input("Введіть ім'я свого котика:")
        self.radist=1
        self.life=True
        self.pregress=1
        self.food = 15
    def study(self):
        print("🦞ЧАС ДЛЯ ТОЧІННЯ КІГТІВ🦞")
        self.radist-=0.5
        self.pregress+=1
        self.food -= 1
    def chill(self):
        print("🎮ЧАС ДЛЯ ГРИ🎮")
        self.radist+=1
        self.pregress-=0.5
        self.food -= 1
    def sleep(self):
        print("☁ЧАС ДЛЯ СНУ☁")
        self.radist+=1
        self.food -= 2

    def rest(self):
        print("💤ЧАС ДЛЯ ВІДПОЧИНКУ💤")
        self.radist += 1
        self.food -= 1
    def eat(self):
        print("🥞ЧАС ДЛЯ ЇДИ🥞")
        self.radist+=1
        self.food += 6
    def OKNO(self):
        print("🧳ЧАС ДЛЯ СТРИБКА у ФОРТОЧКУ🧳")
        self.radist=0
        self.pregress=0
        self.food =0
        self.life=False
        sleep(2)
        print(f"{self.name} помер від шоку")

    def check(self):
        if self.radist <=0:
            print(f'{self.name} помер від депресії')
            self.life = False
        elif self.pregress<=0:
            print(f"{self.name} помер, бо кігті вже не можна наточити !")
            self.life=False
        elif self.food<=0:
            print(f"{self.name} помер, бо його не кормили! Поганий женя, поганий!")
            self.life=False
    def dayoff(self):
        print(f"У {self.name} радість = {self.radist},наточиність кігтів {self.pregress}, голод {self.food}")
    def simmulate(self):
        rnd=random.randint(1,100)
        if(rnd<=90):
            rndd=random.randint(1,5)
            if rndd==1:
                self.study()
            if rndd==2:
                self.chill()
            if rndd == 3:
                self.sleep()
            if rndd == 4:
                self.rest()
            if rndd==5:
                self.eat()
        else:
            self.OKNO()

        if self.life==True:
            self.dayoff()
            self.check()
catt=Cat()
for i in range(50):
    catt.simmulate()
    if catt.life==False:
        break