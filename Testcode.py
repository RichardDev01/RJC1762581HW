import random

combinaties = ['A', 'B', 'C', 'D', 'E', 'F']
lijst = []
teller = 1296
while True:
    a = (random.choice(combinaties) + random.choice(combinaties) +
         random.choice(combinaties) + random.choice(combinaties))
    if a not in lijst:
        lijst.append(a)
        teller -= 1
    if teller == 0:
        break
lijst.sort()

#

def functie():
    antwoord =  'ABCA'
    pogingen = 8
    juiste_plek = 0
    niet_juiste_plek = 0
    lijst1 = []
    while True:
        ingave = random.choice(lijst)
        if antwoord == ingave or pogingen == 0:
            return False
        pogingen -= 1
        for x in range(0, 4):
            if ingave[x] == antwoord[x]:
                for item in lijst:
                    if item[x] != ingave[x]:
                        lijst.pop(lijst.index(item))
                juiste_plek += 1
            elif ingave[x] in antwoord:
                for item in lijst:
                    if ingave[x] not in item:
                        lijst.pop(lijst.index(item))
                niet_juiste_plek += 1
        print(juiste_plek, niet_juiste_plek)
        juiste_plek = 0
        niet_juiste_plek = 0

functie()