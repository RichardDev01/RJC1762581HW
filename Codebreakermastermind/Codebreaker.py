'''
Sources voor uitleg over itertools;
https://www.youtube.com/watch?v=Qu3dThVy6KQ
https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Itertools
https://docs.python.org/2/library/itertools.html
'''
import random
import  itertools

def AICreateCode():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Dit is een random nummer gokker met geen logica     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      GameGokcode moet een list van 4 elementen zijn      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    Gamemastercode = [ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)]]
    print("De Gamemastercode is", Gamemastercode)
    return Gamemastercode

def AIGokCode():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Dit is een random nummer gokker met geen logica     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      GameGokcode moet een list van 4 elementen zijn      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    GameGokcode = [ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)]]
    return GameGokcode

def PlayerCreateCode():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Code voor het opvragen van de speler zijn oode    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    Gamemastercode = []
    while len(Gamemastercode) < AantalKleuren-1:
        Gamemastercode.append(ListKleurenNamen[int(input("Geef een nummer tussen de 0 en "+ str(AantalKleuren)+ " op: "))])
    return Gamemastercode

def ControlleCode(gegokte_code):
    Blackpin = 0
    Whitepin = 0
    Collourblindpin = 0

    #Het omzetten van list naar sets om de overeenkomsten te isoleren
    set1 = set(GlobalGamemastercode)
    set2 = set(gegokte_code)
    list3 = list(set1 & set2)
    for i in list3:
        # van alle overeenkosmten bepalen hoeveel witte pinnen er moeten zijn (ook zwarte pinnen zijn nog wit)
        if GlobalGamemastercode.count(i) <= gegokte_code.count(i):
            Whitepin += GlobalGamemastercode.count(i)
            Collourblindpin += GlobalGamemastercode.count(i)    #niet gebruikte variable, overgebleven van een eventuele optie voor anderen algoritme die alleen kijkt of er pinnen zijn
    for i in range(len(gegokte_code)):
        #het eventueel omzetten van witte pinnen naar zwarte pinnen
        if gegokte_code[i] == GlobalGamemastercode[i]:
            Blackpin += 1
            Whitepin -= 1
    if Whitepin < 0:
        Whitepin = 0
    feedbck= [Blackpin, Whitepin]
    #feedbck= [Blackpin, Whitepin,Collourblindpin] #ongebruikte variable terug roepen om eventueel een extra algoritme te maken
    return feedbck

def aibraincode(mainlist):
    '''
    De code hieronder controleerd elke uitkomst van de geheugen bank met de voorgaanden uitkomst om alles er uit tefilteren wat slechter is door dat element in de list te vervangen met een "".
    Aan het einde van de functie word leeg element verwijderd uit de lijst om alleen nog maar de meest correcte combinaties over tehouden.
    '''
    for i in range(len(mainlist)):
        AITestuitkomst = ControlleCode(mainlist[i])
        if (AITestuitkomst != GokUitkomst):
            #Alle elementen die niet de zelfde score hebben vervangen door lege strings
            mainlist[i] = ""
    while '' in mainlist:
        #het verwijderen van lege strings
        mainlist.remove('')
    return mainlist

def endgame():
    print(Totaleronde3dlist[Rondescount])
    print("U heeft gewonnen")
    quit()

def debugprint():
    print("De GlobalGamemastercode =", GlobalGamemastercode)
    print("De GlobalGokcode =", GlobalGokcode)
    print("Het aantal zwarte pinnen zijn",GlobalAwsPin[0], 'Het aantal witte pinnen zijn',GlobalAwsPin[1])
    return

def listmaken():
    result = itertools.product(ListKleurenNamen, repeat=4)
    mainlist = []
    for item in result:
        mainlist.append(list(item))
    return mainlist

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Setup     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Global var
AantalKleuren = 5  #maximaal 6
ListKleurenNamen = ["zwart", "wit","groen","blauw","paars","rood"]
Rondescount = 0
AantalRondes = 10   #normaal 10 maar kan minder
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

#keuze van algoritme, 0 = puur random, 1= interpertatie van broncode
AIKeuzeAlg = 1

#AI keuze Game gokcode code
AIGokCodeBool = True
#AIGokCodeBool = False

GlobalGamemastercode= []
GlobalGokcode = []
GlobalAwsPin = []
DefaultGokCode = [ListKleurenNamen[0], ListKleurenNamen[0], ListKleurenNamen[1], ListKleurenNamen[1]]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Code voor het maken van een geheugen bank     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
mainlist = listmaken()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Mainloop     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Het maken van de gamemastercode
if AICreateCodeBool == True:
    GlobalGamemastercode = AICreateCode()
else:
    GlobalGamemastercode = PlayerCreateCode()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(len(mainlist))    #Debug print om te kijken of alle elementen toegevoegt zijn in de grote lijst
#Start play loop
#while Rondescount < AantalRondes:
for i in range (0,AantalRondes):
    if AIGokCodeBool == True:
        if AIKeuzeAlg == 0:
            GlobalGokcode = AIGokCode()
            GlobalAwsPin = ControlleCode(GlobalGokcode)
        elif AIKeuzeAlg== 1:
            print(mainlist[1])
            GokUitkomst = ControlleCode(mainlist[1])
            mainlist = aibraincode(mainlist)
            print(len(mainlist)) #Debug print om de lengte van de lijst bij tehouden
            GameGokcode = mainlist[1]
            '''
            mainlist = aibraincode(mainlist)
            GameGokcode = mainlist[random.randrange(len(mainlist))]
            GokUitkomst = ControlleCode(GameGokcode)
            '''

            print(GokUitkomst)
            print(len(mainlist))
            GlobalAwsPin = GokUitkomst
            GlobalGokcode = GameGokcode
        elif AIKeuzeAlg == 3:
            print("Ai placeholder nmr3")
        else:
            print("Ai placeholder nmr4")
    else:
        #switch de comment om zelf code in te vullen met getallen, dit was voor de makelijkeheid
        #GlobalGokcode = PlayerCreateCode()
        GlobalGokcode = ['groen', 'blauw', 'zwart', 'wit']
    Totaleronde3dlist[Rondescount].append([GlobalGokcode])
    Totaleronde3dlist[Rondescount].append([GlobalAwsPin])

    #Als er 4 zwarte pinnen tussendoor zijn stopt de game
    if GameGokcode == GlobalGamemastercode:
        endgame()
    Rondescount += 1

#print(Totaleronde3dlist)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Debug     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#debugprint()

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
