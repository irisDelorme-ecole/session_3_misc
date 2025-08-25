#Exercice 1 – Conversion de température
#Objectif : manipuler types, conditions et fonctions.
#Écrire une fonction convertir_temperature(valeur, unite) qui :
#• Accepte une température en degrés Celsius (“C”), Fahrenheit (“F”) ou Kelvin
#(“K”)
#• Retourne les deux autres valeurs converties
#Exemple d’appel :
#convertir_temperature(100, "C")  # renvoie (373.15, 212.0)

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


print(convertir_temperature(input("temp?"), input("unite?")))