def makepiramidefirsthalf(hight,base):
    while base < hight:
        string = base * "*"
        print(string)
        base += 1
    return 0

def makepiramidesecondhalf(hight,base):
    while base < hight:
        string = hight * "*"
        print(string)
        hight-=1
    return

def makepiramidefirsthalfin(hight,base):
    while base < hight:
        string = base * "*"
        print('{:>20}'.format(string))  #formating string, kan beter
        base += 1

    return 0

def makepiramidesecondhalfin(hight,base):
    while base < hight:
        string = hight * "*"

        print('{:>20}'.format(string))  #formating string, kan beter
        hight-=1
    return

def makepiramide(hight):
    makepiramidefirsthalf(hight,base)
    makepiramidesecondhalf(hight,base)
    makepiramidefirsthalfin(hight,base)
    makepiramidesecondhalfin(hight,base)

    return 0


Topofpiramide = int(input('Hight of the piramide: '))
base = 0 #Base is niet nodig maar als ik later de pyramide anders wil maken, dan kan dat
makepiramide(Topofpiramide)