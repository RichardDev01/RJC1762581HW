def stringcom(Stringinput1,Stringinput2):
    counter = 0
    while len(Stringinput1) >= 0:
        if Stringinput1[0] == Stringinput2[0]:
            counter += 1
        else:
            print("het eerste verschil is na",counter)
        if len(Stringinput1) >1:
            Stringinput1 = Stringinput1[1:]
            Stringinput2 = Stringinput2[1:]
        else:
            return print("string 1 heeft geen verschil")
    return


Stringinput1 = str(input('Eerste string: '))
Stringinput2 = str(input('Tweede string: '))

stringcom(Stringinput1,Stringinput2)