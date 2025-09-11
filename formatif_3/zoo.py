from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Animal(ABC):
    #protected pour que les classes enfant y aillent acces
    __nom:str=''
    __age:int = 0
    __poids:float = 0

    def __init__(self, nom, age=0, poids=0):
        self.__nom = nom
        self.__age = age
        self.__poids = poids

    @property
    def nom(self):
        return self.__nom

    @property
    def age(self):
        return self.__age

    @property
    def poids(self):
        return self.__poids

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @age.setter
    def age(self, age):
        self.__age = age

    @poids.setter
    def poids(self, poids):
        self.__poids = poids

    @abstractmethod
    def parler(self):
        pass

    @abstractmethod
    def se_deplacer(self):
        pass

    def __str__(self):
        return f"{self.nom} à {self.age} ans et pèse {self.poids} grammes."


class Lion(Animal):
    #private because is the actual animal
    __nom:str
    __age:int
    __poids:float
    __dangereux:bool

    def __init__(self, nom, age=0, poids=0, dangereux=True):
        super().__init__(nom, age, poids)
        self.__dangereux = dangereux

    @property
    def dangereux(self):
        return self.__dangereux

    @dangereux.setter
    def dangereux(self, dangereux):
        self.__dangereux = dangereux

    def parler(self):
        if self.__dangereux:
            print(self.nom + ' rugit')
        else:
            print(self.nom + ' est muet')

    def se_deplacer(self):
        if self.__dangereux:
            print(self.nom + ' court vers vous.')
        else:
            print(self.nom + ' se promène')

    def __str__(self):
        if self.__dangereux:
            return f"{self.nom} à {self.age} ans et pèse {self.poids} grammes.\033[91m ATTENTION: DANGEREUX\033[00m"
        else:
            return f"{self.nom} à {self.age} ans et pèse {self.poids} grammes."

class Pingouin(Animal):
    #private because is the actual animal
    __nom:str
    __age:int
    __poids:float

    def __init__(self, nom, age=0, poids=0):
        super().__init__(nom, age, poids)

    def parler(self):
        print(self.nom + ' dit noot noot')

    def se_deplacer(self):
        print(self.nom + ' se promène maladroitement')

class Perroquet(Animal):
    #private because is the actual animal
    __nom:str
    __age:int
    __poids:float
    __dangereux:bool

    def __init__(self, nom, age=0, poids=0, dangereux=False):
        super().__init__(nom, age, poids)
        self.__dangereux = dangereux

    @property
    def dangereux(self):
        return self.__dangereux

    @dangereux.setter
    def dangereux(self, dangereux):
        self.__dangereux = dangereux

    def parler(self):
        if self.__dangereux:
            print(self.nom + ' rit')
        else:
            print(self.nom + ' est muet')

    def se_deplacer(self):
        if self.__dangereux:
            print(self.nom + ' vole vers vous.')
        else:
            print(self.nom + ' sautille')

    def __str__(self):
        if self.__dangereux:
            return f"{self.nom} à {self.age} ans et pèse {self.poids} grammes.\033[91m ATTENTION: DANGEREUX\033[00m"
        else:
            return f"{self.nom} à {self.age} ans et pèse {self.poids} grammes."



if __name__ == "__main__":
    lion = Lion('Nala', 5, 80000, False)

    pingouin = Pingouin('Pingu', 3, 2500)

    perroquet = Perroquet('Oscar', 3, 5, True)

    zoo = [lion, perroquet, pingouin]

    for animal in zoo:
        print(animal)
        animal.parler()
        animal.se_deplacer()
        print('------------------')

