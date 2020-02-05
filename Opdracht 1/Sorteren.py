'''
Opdracht 5 - Sorteren
Bedenk en schrijf zelf een functie die een lijst met getallen op volgorde sorteert.
'''

def sortfucntie(lst):
    lenlst = len(lst)
    for x in range(lenlst):
        for i in range(1,lenlst-x):
            #< of > om de volg orde te veranderen
            if lst[i-1] > lst[i]:
                (lst[i],lst[i-1])=(lst[i-1],lst[i])
    return lst
sortedlist = []
list = [14,1,23,5,33,35,12,11,25]

print(sortfucntie(list))