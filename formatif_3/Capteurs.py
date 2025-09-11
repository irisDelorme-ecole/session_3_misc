from abc import ABC, abstractmethod
from dataclasses import dataclass
import datetime
import random
import pprint

@dataclass
class Capteur(ABC):
    #attribut classe
    gen_id_capteur = 0

    #attributs instance
    __unite:str
    __id_capteur:str

    def __init__(self, unite='undefined'):
        self.__unite = unite
        Capteur.gen_id_capteur += 1
        self.__id_capteur= 'ID' + str(Capteur.gen_id_capteur)


    @property
    def id_capteur(self):
        return self.__id_capteur

    @property
    def unite(self):
        return self.__unite


    @abstractmethod
    def mesurer(self):
        pass

    def __str__(self):
        return f'Capteur {self.id_capteur} qui mesure en {self.unite}'

    @id_capteur.setter
    def id_capteur(self, value):
            self.__id_capteur = value


class Thermometre(Capteur):

    def __init__(self):
        super().__init__('C')
        print('instance created')


    def mesurer(self):
        current_time = datetime.datetime.now()

        if current_time.month < 3 or current_time.month > 10:
            return f"Mesure de Thermometre ({self.id_capteur}) :" + str(round(random.uniform(-20, 2),2)) + "C ."
        #case (current_time.month < 4 or current_time.month > 10):
        elif current_time.month < 6 or current_time.month > 8:
            return f"Mesure de Thermometre ({self.id_capteur}) :" + str(round(random.uniform(-2, 15), 2)) + "C ."
        else:
            return f"Mesure de Thermometre ({self.id_capteur}) : " + str(round(random.uniform(13, 30), 2)) + " C ."

class Barometre(Capteur):

    def __init__(self):
        super().__init__('hPa')
        print('instance created')

    def mesurer(self):
        return f"Mesure de Barometre ({self.id_capteur}) : " + str(round(random.uniform(950, 1050), 3)) + " hPa ."

class Luxmetre(Capteur):

    def __init__(self):
        super().__init__('lux')
        print('instance created')

    def mesurer(self):
        current_time = datetime.datetime.now()

        if current_time.hour < 6 or current_time.hour > 22:
            return f"Mesure de Luxmetre ({self.id_capteur}) : " + str(round(random.uniform(0, 1), 4)) + " lux ."
        # case (current_time.month < 4 or current_time.month > 10):
        else:
            return f"Mesure de Luxmetre ({self.id_capteur}) : " + str(round(random.uniform(2, 1000000), 4)) + " lux ."

class StationMesure():

    #attributs d'instance
    __nom_station:str
    __capteurs:list

    def __init__(self, nom_station):
        self.__nom_station = nom_station
        self.__capteurs = []

    def ajouter_capteur(self, capteur):
        self.__capteurs.append(capteur)

    def effectuer_mesures(self):
        capteurs_dict = {'capt' : 'Mesures des capteurs'}

        for capteur in self.__capteurs:
            capteurs_dict.update({capteur.id_capteur:capteur.mesurer()})

        return capteurs_dict

if __name__ == '__main__':
    c1 = Thermometre()
    c2 = Thermometre()
    c3 = Barometre()
    c4 = Luxmetre()
    c5 = Luxmetre()
    list_capteurs = [ c1, c2, c3, c4, c5]



    station_mesures = StationMesure('Station de Iris')
    for capteur in list_capteurs:
        station_mesures.ajouter_capteur(capteur)

    pprint.pprint(station_mesures.effectuer_mesures())