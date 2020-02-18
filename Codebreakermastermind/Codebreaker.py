'''
Sources voor uitleg over itertools;
https://www.youtube.com/watch?v=Qu3dThVy6KQ
https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Itertools
https://docs.python.org/2/library/itertools.html
'''
import random
import  itertools

def AICreateCode():
    Gamemastercode = [ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)]]
    print("De Gamemastercode is", Gamemastercode)
    return Gamemastercode

def AIGokCode():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Dit is een random nummer gokker met geen logica     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      GameGokcode moet een list van 4 elementen zijn      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    GameGokcode = [ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)]]
    return GameGokcode

def PlayerCreateCode():
    Gamemastercode = []
    while len(Gamemastercode) < AantalKleuren-1:
        Gamemastercode.append(ListKleurenNamen[int(input("Geef een nummer tussen de 0 en "+ str(AantalKleuren)+ " op: "))])
    return Gamemastercode

def feedback(y, x):
    blackpin = 0
    whitepin = 0
    gok = y.copy()
    code = x.copy()

    for i in range(len(x)):
        if gok[i] == code[i]:
            blackpin += 1
            code[i] = 0
            gok[i] = 1

    for i2 in range(len(x)):
        if gok[i2] != code[i2] and gok[i2] in code:
            whitepin += 1
            z = code.index(gok[i2])
            code[z] = 0
            gok[i2] = 1

    pinnetjes = [blackpin, whitepin]
    return pinnetjes


def ControlleCode(gegokte_code):

    Blackpin = 0
    Whitepin = 0
    Collourblindpin = 0
    set1 = set(GlobalGamemastercode)
    set2 = set(gegokte_code)
    list3 = list(set1 & set2)
    for i in list3:
        if GlobalGamemastercode.count(i) <= gegokte_code.count(i):
            Whitepin += GlobalGamemastercode.count(i)
            Collourblindpin += GlobalGamemastercode.count(i)
    for i in range(len(gegokte_code)):
        if gegokte_code[i] == GlobalGamemastercode[i]:
            Blackpin += 1
            Whitepin -= 1
    if Whitepin < 0:
        Whitepin = 0
    feedbck= [Blackpin, Whitepin]
    return feedbck
    #return [Blackpin, Whitepin, Collourblindpin]

def ControlleCodeAIBrain(gegokte_code):
    Blackpin = 0
    Whitepin = 0
    Collourblindpin = 0
    set1 = set(AIGokCodeComparator)
    set2 = set(gegokte_code)
    list3 = list(set1 & set2)
    for i in list3:
        if AIGokCodeComparator.count(i) <= gegokte_code.count(i):
            Whitepin += AIGokCodeComparator.count(i)
            Collourblindpin += AIGokCodeComparator.count(i)
    for i in range(len(gegokte_code)):
        if gegokte_code[i] == AIGokCodeComparator[i]:
            Blackpin += 1
            Whitepin -= 1
    feedbck = [Blackpin, Whitepin]
    return feedbck
    #return [Blackpin, Whitepin, Collourblindpin]

def aibraincode(mainlist):
    '''
    De code hieronder controleerd elke uitkomst van de geheugen bank met de voorgaanden uitkomst om alles er uit tefilteren wat slechter is door dat element in de list te vervangen met een "".
    Aan het einde van de functie word leeg element verwijderd uit de lijst om alleen nog maar de meest correcte combinaties over tehouden.
    '''
    ailist = mainlist
    for i in range(len(ailist)):
        # print(mainlist[i],end= " ")
        #AITestuitkomst = ControlleCodeAIBrain(ailist[i])
        AITestuitkomst = ControlleCode(ailist[i])
        #print(AITestuitkomst)
        # print(ControlleCodeAIBrain(mainlist[i]))
        #if (AITestuitkomst[2] < GokUitkomst[2]):
        #if (AITestuitkomst[0] < GokUitkomst[0] or GokUitkomst[1] >= AITestuitkomst[1]):
        #if (AITestuitkomst[0] < GokUitkomst[0] or GokUitkomst[1] > AITestuitkomst[1]):
        #if (AITestuitkomst[0] < GokUitkomst[0] or  GokUitkomst[1] < AITestuitkomst[1]):
        #if (AITestuitkomst != GokUitkomst):
        if (AITestuitkomst != GokUitkomst):
        #if (AITestuitkomst[0] < GokUitkomst[0]) or (AITestuitkomst[1] < GokUitkomst[1]):
            # AIChoiceslist.append(mainlist[i])
            mainlist[i] = ""

    while '' in mainlist:
        mainlist.remove('')
    return ailist


def endgame():
    print(Totaleronde3dlist[Rondescount])
    print("U heeft gewonnen")
    quit()

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

AIGokCodeComparator= DefaultGokCode
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Code voor het maken van een geheugen bank     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
result = itertools.product(ListKleurenNamen, repeat=4)
mainlist = []
for item in result:
    mainlist.append(list(item))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Mainloop     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Het maken van de gamemastercode
if AICreateCodeBool == True:
    GlobalGamemastercode = AICreateCode()
else:
    GlobalGamemastercode = PlayerCreateCode()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~
GokUitkomst = ControlleCode(DefaultGokCode)
print(GokUitkomst)
print(len(mainlist))
ronde = 1

mainlist = aibraincode(mainlist)

GokUitkomst = ControlleCode(mainlist[1])
#mainlist = aibraincode(mainlist)

#Start play loop
while Rondescount < AantalRondes:
    if AIGokCodeBool == True:
        if AIKeuzeAlg == 0:
            GlobalGokcode = AIGokCode()
            GlobalAwsPin = ControlleCode(GlobalGokcode)
        elif AIKeuzeAlg== 1:

            mainlist = aibraincode(mainlist)

            GokUitkomst = ControlleCode(mainlist[1])
            GameGokcode = mainlist[random.randrange(len(mainlist))]
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
    #if GlobalAwsPin[0] == 4:
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
