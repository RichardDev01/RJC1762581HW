'''
Tekstcheck
Schrijf een functie die de eerste index teruggeeft waarop twee strings een verschillende waarde hebben. Bedenk zelf een goede functienaam.
Het complete programma vraagt om twee strings aan de gebruiker en print de index waarop deze twee strings verschillen. Zorg je dat de functie goed test. Let op: een string mag spaties bevatten! Voorbeeld output:
'''
def stringcom(Stringinput1,Stringinput2):
    #in deze functie maak ik steeds de string van links naar rechts kleiner om te kijken waar het eerste verschil is
    counter = 0
    while len(Stringinput1) >= 0:
        if Stringinput1[0] == Stringinput2[0]:
            counter += 1
        else:
            print("het eerste verschil is na",counter)
        if len(Stringinput1) >1:
            Stringinput1 = Stringinput1[1:]
            Stringinput2 = Stringinput2[1:]
        else:
            return print("string 1 heeft geen verschil")
    return


Stringinput1 = str(input('Eerste string: '))
Stringinput2 = str(input('Tweede string: '))

stringcom(Stringinput1,Stringinput2)