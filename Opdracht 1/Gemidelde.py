'''
Gemiddelde berekenen
Schrijf een functie die het gemiddelde van een lijst met cijfers berekend. Schrijf er ook een die als input een lijst van lijsten met cijfers berekend.
'''
def gemberekenen(lst):
    max=0
    lenlst = len(lst)
    for x in lst:
        max += x
    gem = max/lenlst
    return gem

lstinvoer = []

lst = [1,4,5,7,3,5,6,2,3]
print(gemberekenen(lst))

print("er moeten 5 getalen ingevult worden")
while len(lstinvoer) < 5:
    lstinvoer.append(int(input("Voeg een getal toe:")))
    print(lstinvoer)
print("het gemidelde van deze invoer is")
print(gemberekenen(lstinvoer))
