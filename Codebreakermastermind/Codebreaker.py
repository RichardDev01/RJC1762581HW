'''
computer 10 poginging

import random

kleuren random(0,6) (5 kleuren)

1 List met de code [1,2,3,4]

    De poging   De feedback(1/2)    2 == zwarte pin
10x [[1,2,3,4][1,2,3,4]]


**Use 2-2 patterns to detect the colors**

Functie AI

    Eerst 5x stategie 1, 2 x vaste kleur bij blue, en dan roleren door de kleuren

    dan de waardens ophalen en dan een dictonary aanmaken om te kijken welke kleuren de meeste kans hebben
    dan brute force met de laaste 5 pogingen

funcatie Tekenbord
    print(scope)

Functie gokcode
    list[0-4] == random(0,6)

Functie Controle code:
for i in gegokte_code:
    If gegokte_kleur && positie == code_kleur && code_positie
        Zwarte pin
    elif gegokte_kleur in list code_kleur:
       Witte pin

'''
import random

def AICreateCode():
    Gamemastercode = [ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)]]
    #print("De gekozen code is", Gamemastercode)
    return Gamemastercode

def AIGokCode():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Dit is een random nummer gokker met geen logica     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      GameGokcode moet een list van 4 elementen zijn      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    GameGokcode = [ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)]]
    #print("De gekozen code is", Gamemastercode)
    return GameGokcode

def PlayerCreateCode():
    Gamemastercode = []
    while len(Gamemastercode) < AantalKleuren-1:
        Gamemastercode.append(ListKleurenNamen[int(input("Geef een nummer tussen de 0 en "+ str(AantalKleuren)+ " op: "))])
    #print("De gekozen code is", Gamemastercode)
    return Gamemastercode

def ControlleCode(gegokte_code):
    Blackpin = 0
    Whitepin =0
    for i in range (len(gegokte_code)):
        if gegokte_code[i]==GlobalGamemastercode[i]:
            Blackpin+=1
            continue
        elif gegokte_code[i] in GlobalGamemastercode:
            Whitepin+=1
            continue
    if Blackpin == 4:
        Totaleronde3dlist[Rondescount].append([GlobalGokcode])
        Totaleronde3dlist[Rondescount].append([GlobalAwsPin])
        print(Totaleronde3dlist[Rondescount])
        print("U heeft gewonnen")
        quit()
    return [Blackpin,Whitepin]

def debugprint():
    print("De GlobalGamemastercode =", GlobalGamemastercode)
    print("De GlobalGokcode =", GlobalGokcode)
    print("Het aantal zwarte pinnen zijn",GlobalAwsPin[0], 'Het aantal witte pinnen zijn',GlobalAwsPin[1])


    return
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Setup     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Global var
AantalKleuren = 5  #maximaal 6
ListKleurenNamen = ["zwart", "wit","groen","blauw","paars","rood"]
Rondescount = 0
AantalRondes = 10   #normaal 10 maar kan minder
#Totaleronde3dlist = [ [[1],[]] , [[2],[]] , [[3],[]] , [[4],[]] , [[5],[]] , [[6],[]] , [[7],[]] , [[8],[]] , [[9],[]] , [[10],[]] ]
#Totaleronde3dlist = [ [[],[]] , [[],[]] , [[],[]] , [[],[]] , [[],[]] , [[],[]] , [[],[]] , [[],[]] , [[],[]] , [[],[]] ]
Totaleronde3dlist = [[] ,[] ,[],[],[],[],[],[],[],[]]
Rondelist1 = Totaleronde3dlist[0]
Rondelist2 = Totaleronde3dlist[1]
Rondelist3 = Totaleronde3dlist[2]
Rondelist4 = Totaleronde3dlist[3]
Rondelist5 = Totaleronde3dlist[4]
Rondelist6 = Totaleronde3dlist[5]
Rondelist7 = Totaleronde3dlist[6]
Rondelist8 = Totaleronde3dlist[7]
Rondelist9 = Totaleronde3dlist[8]
Rondelist10= Totaleronde3dlist[9]

#AI keuze Game mastercode
AICreateCodeBool = True
#AICreateCodeBool = False

#AI keuze Game gokcode code
AIGokCodeBool = True
#AIGokCodeBool = False

GlobalGamemastercode= []
GlobalGokcode = []
GlobalAwsPin = []

if AICreateCodeBool == True:
    GlobalGamemastercode = AICreateCode()
else:
    GlobalGamemastercode = PlayerCreateCode()

print(GlobalGamemastercode)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Mainloop     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

while Rondescount < AantalRondes:
    if AIGokCodeBool == True:
        GlobalGokcode = AIGokCode()
    else:
        #GlobalGokcode = PlayerCreateCode()
        GlobalGokcode = ['groen', 'blauw', 'zwart', 'wit']
    GlobalAwsPin = ControlleCode(GlobalGokcode)
    Totaleronde3dlist[Rondescount].append([GlobalGokcode])
    Totaleronde3dlist[Rondescount].append([GlobalAwsPin])
    #Totaleronde3dlist[Rondescount] = Totaleronde3dlist[[GlobalGokcode][GlobalAwsPin]]
    print(Totaleronde3dlist[Rondescount])
    Rondescount += 1
#print(Totaleronde3dlist)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Debug     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
debugprint()

print("Deze ronde heeft de volgende list",Rondelist1)
print("Deze ronde heeft de volgende list",Rondelist2)
print("Deze ronde heeft de volgende list",Rondelist3)
print("Deze ronde heeft de volgende list",Rondelist4)
print("Deze ronde heeft de volgende list",Rondelist5)
print("Deze ronde heeft de volgende list",Rondelist6)
print("Deze ronde heeft de volgende list",Rondelist7)
print("Deze ronde heeft de volgende list",Rondelist8)
print("Deze ronde heeft de volgende list",Rondelist9)
print("Deze ronde heeft de volgende list",Rondelist10)
