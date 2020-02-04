'''
a. Schrijf een functie count() die berekent hoe vaak een geheel getal x in een lijst voorkomt.

b. Schrijf een functie die in een gegeven lijst het grootste verschil tussen twee op een volgende getallen bepaalt.

c. Schrijf een functie, die bepaalt of een gegeven lijst met alleen 1’en en 0’en aan de volgende eisen voldoet:
  - Het aantal enen is groter dan aan het aantal nullen
  - Er mogen niet meer dan 12 nullen zijn.
Bedenk zelf wat het return type van deze functie moet zijn. Gebruik in je programma de functie count() die je hebt geschreven bij de vorige opgave.
'''


def count(zoekgetal):
    counter = 0
    while len(lijst) > 0:
        if lijst[0] == zoekgetal:
            counter +=1
        lijst.pop(0)
    print(counter)
    return

def compare(lijst):
    counter = 0
    print(len(lijst))
    while len(lijst) > 1:
        verschil = lijst[0] - lijst[1]
        print(verschil)
        if verschil > counter:
            counter == verschil
        lijst.pop(0)
    print(counter)
    return


lijst = [1,2,2,3,4,5,2,2,5,4]
zoekgetal = int(input('Welk getal zoek je: '))

count(zoekgetal)
compare(lijst)