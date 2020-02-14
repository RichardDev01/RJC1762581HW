'''
https://www.youtube.com/watch?v=Qu3dThVy6KQ
https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Itertools
https://docs.python.org/2/library/itertools.html
'''

import  itertools
import random
def ControlleCode(gegokte_code):
    Blackpin = 0
    Whitepin =0
    for i in range (len(gegokte_code)):
        if gegokte_code[i]==GlobalGamemastercode[i]:
            Blackpin+=1
            continue
    for i in range(len(gegokte_code)):
        if gegokte_code[i] in GlobalGamemastercode:
            if GlobalGamemastercode.count(gegokte_code[i])>Blackpin and Whitepin < GlobalGamemastercode.count(gegokte_code[i]) and gegokte_code.count(gegokte_code[i])>Blackpin:
                #hier moet ik nog aanpassen nu is het verkeerd
                Whitepin += 1


            else:
                continue
            continue
    return [Blackpin,Whitepin]

def ControlleCodeAIBrain(gegokte_code):
    Blackpin = 0
    Whitepin =0
    for i in range (len(gegokte_code)):
        if gegokte_code[i]==AIGokCodeComparator[i]:
            Blackpin+=1
            continue
    for i in range(len(gegokte_code)):
        if gegokte_code[i] in AIGokCodeComparator:
            if AIGokCodeComparator.count(gegokte_code[i])>  Blackpin and Whitepin < AIGokCodeComparator.count(gegokte_code[i]) and gegokte_code.count(gegokte_code[i])>Blackpin:
                # hier moet ik nog aanpassen nu is het verkeerd
                Whitepin += 1
            else:
                continue
            continue
    return [Blackpin,Whitepin]


GlobalGamemastercode= ['groen', 'zwart', 'zwart', 'zwart']
GlobalGokcode = []
GlobalAwsPin = []
AantalKleuren = 5  #maximaal 6
ListKleurenNamen = ["zwart", "wit","groen","blauw","paars","rood"]
DefaultGokCode = [ListKleurenNamen[0], ListKleurenNamen[0], ListKleurenNamen[1], ListKleurenNamen[1]]

AIGokCodeComparator= DefaultGokCode
result = itertools.product(ListKleurenNamen, repeat=4)

#GlobalGamemastercode = [ListKleurenNamen[random.randrange(AantalKleuren)], ListKleurenNamen[random.randrange(AantalKleuren)],ListKleurenNamen[random.randrange(AantalKleuren)], ListKleurenNamen[random.randrange(AantalKleuren)]]

mainlist = []
AIChoiceslist= []
AIChoiceslist2= []
for item in result:
    #print(item[0:4])
    mainlist.append(list(item))

##Ronde 1
print("Kraak",GlobalGamemastercode)
print("Gok  ",DefaultGokCode)
GokUitkomst = ControlleCode(DefaultGokCode)
print(GokUitkomst)

for i in range(len(mainlist)):
    #print(mainlist[i],end= " ")
    AITestuitkomst = ControlleCodeAIBrain(mainlist[i])
    #print(ControlleCodeAIBrain(mainlist[i]))
    if (AITestuitkomst[0] < GokUitkomst[0]) or (AITestuitkomst[1] < GokUitkomst[1]):
        #AIChoiceslist.append(mainlist[i])
        mainlist[i] = ""

while '' in  mainlist:
    mainlist.remove('')

print(len(mainlist))
#print(mainlist)
#ronde 2
'''
AIGokCodeComparator = AIChoiceslist[random.randrange(len(AIChoiceslist))]
print("Kraak",GlobalGamemastercode)
print("Gok  ",AIGokCodeComparator)
GokUitkomst = ControlleCode(AIGokCodeComparator)
print(GokUitkomst)

for i in range(len(AIChoiceslist)):
    #print(mainlist[i],end= " ")
    AITestuitkomst = ControlleCodeAIBrain(AIChoiceslist[i])
    #print(ControlleCodeAIBrain(mainlist[i]))
    if AITestuitkomst[0] >= GokUitkomst[0]:
        AIChoiceslist2.append(AIChoiceslist[i])

for j in range(len(AIChoiceslist2)):
    print(AIChoiceslist2[j])
#print(AIChoiceslist2)

#for j in range(len(AIChoiceslist)):
#    print(AIChoiceslist[j])
#print(AIChoiceslist)

'''