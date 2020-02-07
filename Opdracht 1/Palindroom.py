'''
Opdracht 4 - Palindroom
Schrijf een functie die checkt of een woord een palindroom is.
Schrijf een versie die gebruikt maakt van een bibliotheekfunctie die een string voor je omdraait.
Maak ook een versie waarbij jij zelf het omdraaien verzorgt. Probeer zo min mogelijk code te gebruiken.
'''

def palidroom(woord):
    if len(woord)<1:
        print("het woord is palidroom")
        return
    if woord[0] == woord[-1]:
        palidroom(woord[1:-1])
    else:
        print("het woord was geen palidroom")
    return

woord = str(input("geef het woord op: "))

print("het opgeven woord is", woord)
palidroom(woord)
# dit ondster stukje code gebruik ik om de string om te draaien volgens de opdracht
print("dit is het woord gespiegel met een librabry", woord[::-1])
print("nu wordt de functie gespiegeld uitgevoord")
palidroom(woord[::-1])

