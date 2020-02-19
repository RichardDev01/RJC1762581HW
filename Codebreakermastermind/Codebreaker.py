# Feedback in de les
# Keep it simple stupid. Simpler is always better. Reduce complexity as much as possible.
# Always find root cause. Always look for the root cause of a problem.
# Use pronounceable names. Have no side effects. Prefer data structures.
# Similar functions should be close.
#
'''
Sources voor uitleg over itertools;
https://www.youtube.com/watch?v=Qu3dThVy6KQ
https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Itertools
https://docs.python.org/2/library/itertools.html
'''
import random
import itertools


def AICreateCode():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Dit is een random nummer gokker met geen logica     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      GameGokcode moet een list van 4 elementen zijn      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    gamemastercode = [ListKleurenNamen[random.randrange(AantalKleuren)],
                      ListKleurenNamen[random.randrange(AantalKleuren)],
                      ListKleurenNamen[random.randrange(AantalKleuren)],
                      ListKleurenNamen[random.randrange(AantalKleuren)]]
    print("De gamemastercode is", gamemastercode)
    return gamemastercode


def AIGokCode():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Dit is een random nummer gokker met geen logica     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      game_gokcode moet een list van 4 elementen zijn      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    game_gokcode = [ListKleurenNamen[random.randrange(AantalKleuren)],
                    ListKleurenNamen[random.randrange(AantalKleuren)],
                    ListKleurenNamen[random.randrange(AantalKleuren)],
                    ListKleurenNamen[random.randrange(AantalKleuren)]]
    return game_gokcode


def PlayerCreateCode():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Code voor het opvragen van de speler zijn oode    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    gamemastercode = []
    while len(gamemastercode) < AantalKleuren - 1:
        gamemastercode.append(
            ListKleurenNamen[int(input("Geef een nummer tussen de 0 en " + str(AantalKleuren) + " op: "))])
    return gamemastercode


def listmaken():
    # Het gebruik van itertools om een lijst te vullen met variabelen. zie bronnen bovenin
    result = itertools.product(ListKleurenNamen, repeat=4)
    mainlist = []
    for item in result:
        mainlist.append(list(item))
    return mainlist


def ControlleCode(gegokte_code, targetcode):
    # Gegokte code is de code die je toeleverd en de targetcode is de code waar je naar toe vergelijkt
    blackpin = 0
    whitepin = 0
    collourblindpin = 0

    # Het omzetten van list naar sets om de overeenkomsten te isoleren
    # set1 = set(GlobalGamemastercode)
    set1 = set(targetcode)
    set2 = set(gegokte_code)
    list3 = list(set1 & set2)
    for i in list3:
        # van alle overeenkosmten bepalen hoeveel witte pinnen er moeten zijn (ook zwarte pinnen zijn nog wit)
        if targetcode.count(i) <= gegokte_code.count(i):
            whitepin += targetcode.count(i)
            collourblindpin += targetcode.count(
                i)  # niet gebruikte variable, overgebleven van een eventuele optie voor anderen algoritme die alleen kijkt of er pinnen zijn
    for i in range(len(gegokte_code)):
        # het eventueel omzetten van witte pinnen naar zwarte pinnen
        if gegokte_code[i] == targetcode[i]:
            blackpin += 1
            whitepin -= 1
    if whitepin < 0:
        whitepin = 0
    feedbck = [blackpin, whitepin]
    # feedbck= [blackpin, whitepin,collourblindpin] #ongebruikte variable terug roepen om eventueel een extra algoritme te maken
    return feedbck


def aibraincode(mainlist, gokresultaat, controlecode):
    '''
    extra parameter voor code die gecheckt moeten worden
    De code hieronder controleerd elke uitkomst van de geheugen bank met de voorgaanden uitkomst om alles er uit tefilteren wat slechter is door dat element in de list te vervangen met een "".
    Aan het einde van de functie word leeg element verwijderd uit de lijst om alleen nog maar de meest correcte combinaties over tehouden.
    '''
    for i in range(len(mainlist)):
        ai_testuitkomst = ControlleCode(mainlist[i], controlecode)
        if (ai_testuitkomst != gokresultaat):
            # Alle elementen die niet de zelfde score hebben vervangen door lege strings
            mainlist[i] = ""
    while '' in mainlist:
        # het verwijderen van lege strings
        mainlist.remove('')
    return mainlist


def endgame(win, maxrondes):
    # functie om het spel af tesluiten
    # print(Totaleronde3dlist)
    if maxrondes == True:
        print("Er zijn geen beurten meer over :c")
        quit()
    if win == True:
        print("U heeft gewonnen/of de AI heeft gewonnen")
        for i in Totaleronde3dlist:
            print(i)
        quit()
    else:
        print("De AI heeft geen idee voor antwoord :c")
        quit()


def maingame():
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Setup     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    rondescount = 0
    aantal_rondes = 10  # normaal 10 maar kan minder

    # AI keuze Game mastercode
    ai_create_code_bool = True
    # ai_create_code_bool = False

    # keuze van algoritme, 0 = puur random, 1= interpertatie van broncode
    ai_keuze_alg = 1

    # AI keuze Game gokcode code
    ai_gok_code_bool = True
    # ai_gok_code_bool = False

    global_gokcode = []
    global_aws_pin = []
    # default_gok_code = [ListKleurenNamen[0], ListKleurenNamen[0], ListKleurenNamen[1], ListKleurenNamen[1]] #voor het gebruik van 2e algoritme wat er nog niet is

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Code voor het maken van een geheugen bank     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    mainlist = listmaken()
    # Het maken van de gamemastercode
    if ai_create_code_bool == True:
        global_gamemastercode = AICreateCode()
    else:
        global_gamemastercode = PlayerCreateCode()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print("Lengte lijst", len(mainlist))  # Debug print om te kijken of alle elementen toegevoegt zijn in de grote lijst
    # Start play loop
    for i in range(0, aantal_rondes):
        if ai_gok_code_bool:
            if ai_keuze_alg == 0:
                global_gokcode = AIGokCode()  # Random code ophalen
                global_aws_pin = ControlleCode(global_gokcode, 0)  # gok maken en feedback opvragen
            elif ai_keuze_alg == 1:
                # print(mainlist[0])
                if len(mainlist) == 0:
                    endgame(False, False)
                else:
                    controllecode = mainlist[0]
                gok_uitkomst = ControlleCode(mainlist[0], global_gamemastercode)
                global_aws_pin = gok_uitkomst
                mainlist = aibraincode(mainlist, gok_uitkomst, controllecode)
                game_gokcode = controllecode
                global_gokcode = game_gokcode
                print("Lengte lijst", len(mainlist))
            elif ai_keuze_alg == 3:
                print("Ai placeholder nmr3")
            else:
                print("Ai placeholder nmr4")
        else:
            # switch de comment om zelf code in te vullen met getallen, dit was voor de makelijkeheid
            global_gokcode = PlayerCreateCode()
            # global_gokcode = ['groen', 'blauw', 'zwart', 'wit']
        Totaleronde3dlist[rondescount].append([global_gokcode])
        Totaleronde3dlist[rondescount].append([global_aws_pin])

        # Als er 4 zwarte pinnen tussendoor zijn stopt de game
        if game_gokcode == global_gamemastercode:
            endgame(True, False)
        rondescount += 1
    return


# Global var
Totaleronde3dlist = [[], [], [], [], [], [], [], [], [], []]
AantalKleuren = 5  # maximaal 6 (of lengte listkleurennamen)
ListKleurenNamen = ["zwart", "wit", "groen", "blauw", "paars", "rood"]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      Mainloop     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
maingame()
endgame(False, True)
