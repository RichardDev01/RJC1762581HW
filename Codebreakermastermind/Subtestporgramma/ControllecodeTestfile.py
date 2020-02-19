def ControlleCode(gegokte_code, targetcode):
    #Gegokte code is de code die je toeleverd en de targetcode is de code waar je naar toe vergelijkt
    Blackpin = 0
    Whitepin = 0
    Collourblindpin = 0

    #Het omzetten van list naar sets om de overeenkomsten te isoleren
    #set1 = set(GlobalGamemastercode)
    set1 = set(targetcode)
    set2 = set(gegokte_code)
    list3 = list(set1 & set2)
    for i in list3:
        # van alle overeenkosmten bepalen hoeveel witte pinnen er moeten zijn (ook zwarte pinnen zijn nog wit)
        if targetcode.count(i) <= gegokte_code.count(i):
            Whitepin += targetcode.count(i)
            Collourblindpin += targetcode.count(i)    #niet gebruikte variable, overgebleven van een eventuele optie voor anderen algoritme die alleen kijkt of er pinnen zijn
    for i in range(len(gegokte_code)):
        #het eventueel omzetten van witte pinnen naar zwarte pinnen
        if gegokte_code[i] == targetcode[i]:
            Blackpin += 1
            Whitepin -= 1
    if Whitepin < 0:
        Whitepin = 0
    feedbck= [Blackpin, Whitepin]
    #feedbck= [Blackpin, Whitepin,Collourblindpin] #ongebruikte variable terug roepen om eventueel een extra algoritme te maken
    return feedbck

print(ControlleCode(['rood', 'zwart', 'paars', 'rood'], ['blauw', 'zwart', 'paars', 'blauw']))