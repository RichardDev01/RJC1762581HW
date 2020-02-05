'''
a. Schrijf een functie count() die berekent hoe vaak een geheel getal x in een lijst voorkomt.

b. Schrijf een functie die in een gegeven lijst het grootste verschil tussen twee op een volgende getallen bepaalt.

c. Schrijf een functie, die bepaalt of een gegeven lijst met alleen 1’en en 0’en aan de volgende eisen voldoet:
  - Het aantal enen is groter dan aan het aantal nullen
  - Er mogen niet meer dan 12 nullen zijn.
Bedenk zelf wat het return type van deze functie moet zijn. Gebruik in je programma de functie count() die je hebt geschreven bij de vorige opgave.
'''
def count(zoekgetal,lijstzoek):
    counter = 0
    lijstedit = lijstzoek
    while len(lijstedit) > 0:
        if lijstedit[0] == zoekgetal:
            counter +=1
        lijstedit.pop(0)
    print("het getal",zoekgetal ,"komt", counter, "voor")
    return counter

def compare(lijstcompare):
    counter = 0
    #print(len(lijst))
    while len(lijstcompare) > 1:
        verschil = lijstcompare[0] - lijstcompare[1]
        #print(verschil)
        if verschil > counter:
            counter = verschil
        lijstcompare.pop(0)
    print("Het grootste verschill tussen de 1 op volgenden getallen =",counter)
    return

def count1en0(lijsteenofnull,lijsteenofnull2):

    aantal0= count(0,lijsteenofnull)

    aantal1=count(1, lijsteenofnull2)
    if aantal1 > aantal0:
        print("er zijn meer enen dan nullen")
    else:
        print("er zijn meer nullen dan enen")
    if aantal0 > 12:
        print("Er zijn teveel nullen")
    return


lijstcount = [1,2,2,9,4,5,2,2,5,4]
lijstcompare = [1,2,2,9,4,5,2,2,5,4]
lijsteenofnull = [1,1,1,0,0,1,1,0,1,0,1]
lijsteenofnull2 = [1,1,1,0,0,1,1,0,1,0,1]
zoekgetal = int(input('Welk getal zoek je: '))
count(zoekgetal,lijstcount)
compare(lijstcompare)
count1en0(lijsteenofnull,lijsteenofnull2)