#Exercice 1 – Conversion de température
#Objectif : manipuler types, conditions et fonctions.
#Écrire une fonction convertir_temperature(valeur, unite) qui :
#• Accepte une température en degrés Celsius (“C”), Fahrenheit (“F”) ou Kelvin
#(“K”)
#• Retourne les deux autres valeurs converties
#Exemple d’appel :
#convertir_temperature(100, "C")  # renvoie (373.15, 212.0)
from physique import acceleration, pression

CELSIUS = "C"
KELVIN = "K"
FAHRENHEIT = "F"

def convertir_temperature(valeur, unite):
    if unite == "C":
        return float(valeur) + 273.15, ((float(valeur) * (9/5)) + 32)
    elif unite == "K":
        return float(valeur) - 273.15, (((float(valeur) - 273.15) * (5/9)) + 32)
    else:
        celsius = (float(valeur)-32)*(5/9)
        return celsius, celsius + 273.15


#print(convertir_temperature(input("temp?"), input("unite?")))
"""
Exercice 2 – Vitesse de chute libre 
Objectif : utiliser une boucle et une liste. 
Créer une fonction vitesses_chute_libre(duree, pas) qui renvoie une liste des 
vitesses toutes les pas secondes pendant duree secondes. On utilise : 
(v = g t avec = 9.81) 
Exemple : vitesses_chute_libre(5, 1) → [0, 9.81, 19.62, 29.43, 39.24]
"""

def vitesse_chute_libre(duree, pas):
    compteur = 0
    resultat = list()
    g = 9.81
    while(compteur < duree):
        resultat.append(compteur*g)
        compteur += pas
    return resultat

#print(vitesse_chute_libre(5, 1))


"""Exercice 3 – Energie cinétique 
Objectif : créer une fonction avec vérification de types. 
Écrire une fonction energie_cinetique(masse, vitesse) qui retourne : 
(𝐸 = (1/2)𝑚 𝑣2) 
Ajouter une vérification : masse et vitesse doivent être > 0 (Utiliser raise qui lève une 
Exception)"""

def energie_cinetique(masse, vitesse):
    if (vitesse > 0 and masse > 0):
        return masse * vitesse * vitesse * 0.5
    else :
        raise

#print(energie_cinetique(100, 100))
#print(energie_cinetique(100, -100))


"""
Exercice 4 – Statistiques sur des mesures 
Objectif : parcourir des listes et utiliser des fonctions. 
Écrire une fonction qui, à partir d’une liste de températures, retourne : 
• la moyenne 
• la température minimale 
• la température maximale
"""

def statistiques(liste):
    moyenne = 0
    min = liste[0]
    max = liste[0]
    for _ in liste:
        moyenne += _
        if _ < min:
            min = _
        elif _ > max:
            max = _

    return (moyenne/len(liste)), min, max

liste = [10, 2, 4, 5, 1, 9, 18]
#print(statistiques(liste))

"""
Exercice 5 – Masse molaire d’un composé 
Objectif : manipuler des dictionnaires. 
Utiliser un dictionnaire avec les masses molaires de quelques éléments : """
masses = {"H": 1.008, "O": 15.999, "C": 12.011}
""" Écrire une fonction masse_totale(liste_elements) qui calcule la masse molaire 
d’un composé sous forme de """
liste = ('H', 'H', 'O')

def masse_totale(formule):

    liste_elements = formule_a_liste(formule)
    masse_totale = 0
    for element in liste_elements:
        masse_totale += masses.get(element)
    return masse_totale

#print(masse_totale(liste) == (1.008 + 1.008 + 15.999))


"""
Exercice 6 – Décomposition d’une formule chimique simple 
Objectif : compréhensions de listes. 
Écrire une fonction qui transforme une formule comme "H2O" en liste : 
["H", "H", "O"] 
Combiner ensuite les exercices 5 et 6 
"""

def formule_a_liste(formule):
    liste_elements = list()

    for element in formule:
        if element.isdigit():
            nombre_de_repeat = int(element)
            while nombre_de_repeat > 1:
               liste_elements.append(liste_elements[len(liste_elements)-1])
               nombre_de_repeat -= 1
        else:
            liste_elements.append(str.upper(element))

    return liste_elements


#print(formule_a_liste("H2O"))
#print(masse_totale("H2O") == (1.008 + 1.008 + 15.999))-->gives true(yay)

"""
Exercice 7 – Création d’un module physique 
Objectif : comprendre les modules. 
1. Créer un fichier physique.py contenant : 
o acceleration(force, masse) 
o pression(force, surface) 
2. Dans un autre fichier, importer physique et tester les fonctions. 
"""

import physique

#print(acceleration(9.81, 1))
#print(pression(50, 10)) cool

"""
Exercice 8 – Simulation de chute avec frottements 
Objectif : écrire un programme plus complet avec boucles, conditions et calculs. 
Simuler la chute d’un objet soumis à une accélération de la gravité 𝑔 = 9.81 et à 
une force de frottement proportionnelle à sa vitesse 𝑓 = −𝑘𝑣, avec 𝑘 = 0.1. 
L’objet commence avec une vitesse nulle. À chaque pas de temps 𝑡 = 0.1 s, 
mettez à jour : 
• L’accélération instantanée 𝑎 = 𝑔 − 𝑘𝑣 
• La vitesse 𝑣 = 𝑣 + 𝑎 𝑡 
• La position 𝑥 = 𝑥 + 𝑣 𝑡 
Le programme s’arrête après 10 secondes. 
Retournez une liste des positions à chaque instant.



jai utilisé une équation différentielle pour obtenir la vitesse en fonction du temps,
parce que je ne faisais pas confiance en mon raisonnement sinon(tout me semblait comme des approximations,
au lieu de des calculs.)

en bref, je suis partie de a = dv/dt, et a = g-kv
ce qui fait 

dv/dt = g-kv

qui m'a donné 

-98,1*e^(t/-10) + 98,1 = V

(résolution explicite avec le point (0, 0)
"""


import math

def sim():
    liste = list()
    t = 0
    x = 0
    v = 0
    while t < 10 and v < 98.1:
        v = (-98.1 * (math.pow(math.e, (t/(-10))))) + 98.1
        x += v * t
        liste.append(x)
        t += 0.1

    return liste

print(sim())



