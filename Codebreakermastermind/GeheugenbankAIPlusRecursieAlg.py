'''
https://www.youtube.com/watch?v=Qu3dThVy6KQ
https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Itertools
https://docs.python.org/2/library/itertools.html
'''

import  itertools
import random
def ControlleCode(gegokte_code):
    '''De witte pin correctie werkt niet 100% maar dar maakt in deze keuze niet uit behalve effiecnietie'''
    Blackpin = 0
    Whitepin =0
    Collourblindpin=0

    set1 = set(GlobalGamemastercode)
    set2 = set(gegokte_code)
    list3 = list(set1 & set2)
    #print(list3)
    for i in list3:
        #print(GlobalGamemastercode.count(i))
        #print(gegokte_code.count(i))
        if GlobalGamemastercode.count(i) <=gegokte_code.count(i):
            Whitepin += GlobalGamemastercode.count(i)
            Collourblindpin +=GlobalGamemastercode.count(i)
    for i in range(len(gegokte_code)):
        #print("globalmaster =", GlobalGamemastercode.count(gegokte_code[i]))
        #print("gegoktecode",gegokte_code.count(gegokte_code[i]))
        if gegokte_code[i]==GlobalGamemastercode[i]:
            Blackpin +=1
            Whitepin -=1

    '''
    
    for i in range(len(gegokte_code)):
        #print("globalmaster =", GlobalGamemastercode.count(gegokte_code[i]))
        #print("gegoktecode",gegokte_code.count(gegokte_code[i]))
        if gegokte_code[i]==GlobalGamemastercode[i]:
            Blackpin +=1
            #Whitepin -=1
        compare = GlobalGamemastercode.count(gegokte_code[i])
        comparegok = gegokte_code.count(gegokte_code[i])
        #if gegokte_code[i] in GlobalGamemastercode and (GlobalGamemastercode.count(gegokte_code[i]) <= gegokte_code.count(gegokte_code[i])):
        if gegokte_code[i] in GlobalGamemastercode and (compare + Whitepin <=comparegok):
            Whitepin +=1
    '''

    '''
    for i in range (len(gegokte_code)):
        if gegokte_code[i]==GlobalGamemastercode[i]:
            Blackpin+=1
            continue
    #for i in range(len(gegokte_code)):
        if gegokte_code[i] in GlobalGamemastercode and (GlobalGamemastercode.count(gegokte_code[i]) > Whitepin):
            Whitepin += 1
           '''


    '''
    for i in range(len(gegokte_code)):
        if gegokte_code[i] in GlobalGamemastercode and gegokte_code[i] !=GlobalGamemastercode[i] and GlobalGamemastercode.count(gegokte_code[i]) >= gegokte_code.count(gegokte_code[i]):
            Whitepin += 1
            #if GlobalGamemastercode.count(gegokte_code[i])>Blackpin and Whitepin < GlobalGamemastercode.count(gegokte_code[i]) and gegokte_code.count(gegokte_code[i])>Blackpin and gegokte_code[i]!=GlobalGamemastercode[i]:
            #if Whitepin < GlobalGamemastercode.count(gegokte_code[i]) and gegokte_code[i] !=GlobalGamemastercode[i]:

                #hier moet ik nog aanpassen nu is het verkeerd
               # Whitepin += 1


            #else:
             #   continue
            #continue
      '''
    if Whitepin <0:
        Whitepin = 0
    return [Blackpin,Whitepin,Collourblindpin]

def ControlleCodeAIBrain(gegokte_code):
    '''De witte pin correctie werkt niet 100% maar dar maakt in deze keuze niet uit behalve effiecnietie'''

    Blackpin = 0
    Whitepin =0
    Collourblindpin=0
    set1 = set(AIGokCodeComparator)
    set2 = set(gegokte_code)
    list3 = list(set1 & set2)
    #print(list3)
    for i in list3:
        #print(GlobalGamemastercode.count(i))
        #print(gegokte_code.count(i))
        if AIGokCodeComparator.count(i) <=gegokte_code.count(i):
            Whitepin += AIGokCodeComparator.count(i)
            Collourblindpin += AIGokCodeComparator.count(i)
    for i in range(len(gegokte_code)):
        #print("globalmaster =", GlobalGamemastercode.count(gegokte_code[i]))
        #print("gegoktecode",gegokte_code.count(gegokte_code[i]))
        if gegokte_code[i]==AIGokCodeComparator[i]:
            Blackpin +=1
            Whitepin -=1
        '''
    
    Blackpin = 0
    Whitepin =0
    for i in range (len(gegokte_code)):
        if gegokte_code[i]==AIGokCodeComparator[i]:
            Blackpin+=1
            continue
    #for i in range(len(gegokte_code)):
        if gegokte_code[i] in AIGokCodeComparator and (AIGokCodeComparator.count(gegokte_code[i]) > Whitepin):
        #if gegokte_code[i] in AIGokCodeComparator and (AIGokCodeComparator.count(gegokte_code[i])- gegokte_code.count(gegokte_code[i])) >= Whitepin:
            Whitepin += 1
    
    '''

    '''       
    for i in range(len(gegokte_code)):
        if gegokte_code[i] in AIGokCodeComparator and gegokte_code[i] !=AIGokCodeComparator[i] and AIGokCodeComparator.count(gegokte_code[i]) <=gegokte_code.count(gegokte_code[i]):
            #if Whitepin < AIGokCodeComparator.count(gegokte_code[i]) and gegokte_code[i] !=AIGokCodeComparator[i]:
                # hier moet ik nog aanpassen nu is het verkeerd
            Whitepin += 1
        else:
            continue
        continue
    '''
    return [Blackpin,Whitepin,Collourblindpin]

def aibraincode(mainlist):
    ailist = mainlist
    for i in range(len(ailist)):
        # print(mainlist[i],end= " ")
        AITestuitkomst = ControlleCodeAIBrain(ailist[i])
        #print(AITestuitkomst)
        # print(ControlleCodeAIBrain(mainlist[i]))
        if (AITestuitkomst[2] < GokUitkomst[2]):
        #if (AITestuitkomst[0] < GokUitkomst[0] or GokUitkomst[1] >= AITestuitkomst[1]):
            # if (AITestuitkomst[0] < GokUitkomst[0] or GokUitkomst[1] > AITestuitkomst[1]):
            # if (AITestuitkomst[0] < GokUitkomst[0] or  GokUitkomst[1] < AITestuitkomst[1]):
            # if (AITestuitkomst[0] < GokUitkomst[0]) or (AITestuitkomst[1] < GokUitkomst[1]):
            # AIChoiceslist.append(mainlist[i])
            mainlist[i] = ""

    while '' in mainlist:
        ailist.remove('')
    return ailist


GlobalGamemastercode= ['paars', 'blauw', 'paars', 'wit'] #['blauw', 'paars', 'groen', 'paars']   ['wit', 'groen', 'groen', 'zwart']
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
print(len(mainlist))
ronde = 1


while ronde < 1:
    mainlist = aibraincode(mainlist)
    GokUitkomst = ControlleCode(mainlist[random.randrange(len(mainlist))])
    print(GokUitkomst)
    print(len(mainlist))
    ronde +=1
print(mainlist)

#print(aibraincode(mainlist))

'''
for i in range(len(mainlist)):
    #print(mainlist[i],end= " ")
    AITestuitkomst = ControlleCodeAIBrain(mainlist[i])
    #print(ControlleCodeAIBrain(mainlist[i]))
    if (AITestuitkomst[0] < GokUitkomst[0] or GokUitkomst[1]-1 > AITestuitkomst[1]):
    #if (AITestuitkomst[0] < GokUitkomst[0] or GokUitkomst[1] > AITestuitkomst[1]):
    #if (AITestuitkomst[0] < GokUitkomst[0] or  GokUitkomst[1] < AITestuitkomst[1]):
    #if (AITestuitkomst[0] < GokUitkomst[0]) or (AITestuitkomst[1] < GokUitkomst[1]):
        #AIChoiceslist.append(mainlist[i])
        mainlist[i] = ""

while '' in  mainlist:
    mainlist.remove('')

'''

'''
print(len(mainlist))
print(mainlist)
print("Kraak",GlobalGamemastercode)
print("Gok  ",DefaultGokCode)
print(GokUitkomst)
print(len(mainlist))
'''
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