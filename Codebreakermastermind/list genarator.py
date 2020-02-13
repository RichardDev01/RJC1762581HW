import itertools
AantalKleuren = 3  #maximaal 6
ListKleurenNamen = ["zwart", "wit","groen","blauw","paars","rood"]
newlist = []
innerlist= []
print(itertools.product('ABCD', repeat=2))

'''
for i in range(2):
    for j in range(5):
        innerlist.append([i])
    newlist.append(innerlist)


for i in range(AantalKleuren + 1):
    for k in range(AantalKleuren + 1):
        for l in range(AantalKleuren + 1):
            newlist.append([])
        newlist[1] = ListKleurenNamen[1]
    newlist[0] = ListKleurenNamen[0]
'''

'''
for x in range(AantalKleuren+1):
    newlist.append(ListKleurenNamen[x])
    for i in range(AantalKleuren + 1):
        newlist.append(ListKleurenNamen[i])
        for o in range(AantalKleuren + 1):
            newlist.append(ListKleurenNamen[o])
            innerlist.append(newlist)
            for p in range(AantalKleuren + 1):
                newlist.append(ListKleurenNamen[p])
                innerlist.append(newlist)
    #print(ListKleurenNamen[x])

'''
print(newlist)