'''
Fibonaci
De rij van Fibonacci is genoemd naar Leonardo van Pisa, bijgenaamd Fibonacci, die de rij noemt in zijn boek Liber abaci uit 1202. De rij begint met 0 en 1 en vervolgens is elk
volgende element van de rij steeds de som van de twee voorgaande elementen. Bij de rij gebruiken we de notatie fn voor het aangeven van het n-de element van de rij. f9 is
bijvoorbeeld gelijk aan 34. De eerste elementen van de rij zijn dan als volgt:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584
Implementeer een functie die fn uitrekent gegeven integer n. De functie moet recursief zijn.

Meer oefenen met recursie: implementeer de eerdere sorteer-bereken-controleer opdrachten met recursieve functies.


nog maken
'''

def fibonaci(list, grote):
    if len(list) < grote:
        list.append(list[grond] + list[grond + 1])
        fibonaci(list, grond+1)
    else:
        print(list)
        return
    return

list = [0,1]
n = 15
grond = 0
#fibonaci(list, n)

for i in range(n):
    print(i)
    list.append(list[i]+list[i+1])
    print(list)