'''
https://www.youtube.com/watch?v=Qu3dThVy6KQ
https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Itertools
https://docs.python.org/2/library/itertools.html
'''

import  itertools

def ControlleCode(gegokte_code):
    Blackpin = 0
    Whitepin =0
    for i in range (len(gegokte_code)):
        if gegokte_code[i]==GlobalGamemastercode[i]:
            Blackpin+=1
            continue
    for i in range(len(gegokte_code)):
        if gegokte_code[i] in GlobalGamemastercode:
            if GlobalGamemastercode.count(gegokte_code[i])>  Blackpin:
                Whitepin += 1
            else:
                continue
            continue
    return [Blackpin,Whitepin]


GlobalGamemastercode= ['groen', 'zwart', 'paars', 'paars']
GlobalGokcode = []
GlobalAwsPin = []

ListKleurenNamen = ["zwart", "wit","groen","blauw","paars","rood"]
DefaultGokCode = [ListKleurenNamen[4], ListKleurenNamen[0], ListKleurenNamen[0], ListKleurenNamen[4]]
result = itertools.product(ListKleurenNamen, repeat=4)

mainlist = []
for item in result:
    #print(item[0:4])
    mainlist.append(list(item))
print("Kraak",GlobalGamemastercode)
print("Gok  ",DefaultGokCode)
print(ControlleCode(DefaultGokCode))


