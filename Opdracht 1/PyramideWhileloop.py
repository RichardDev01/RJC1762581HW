def makepiramidefirsthalf(hight,base):
    while base < hight:
        string = base * "*"
        print(string)
        #print('{:>20}'.format(string))
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
        print('{:>20}'.format(string))
        base += 1

    return 0

def makepiramidesecondhalfin(hight,base):
    while base < hight:
        string = hight * "*"

        print('{:>20}'.format(string))
        hight-=1
    return

def makepiramide(hight):
    makepiramidefirsthalf(hight,0)
    makepiramidesecondhalf(hight,0)
    makepiramidefirsthalfin(hight,0)
    makepiramidesecondhalfin(hight,0)

    return 0


Topofpiramide = int(input('Hight of the piramide: '))
base = 0
makepiramide(Topofpiramide)