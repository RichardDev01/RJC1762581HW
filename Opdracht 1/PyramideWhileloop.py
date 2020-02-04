def makepiramidefirsthalf(hight,base):
    while base < hight:
        print(base * "*")
        base += 1

    return 0

def makepiramidesecondhalf(hight,base):
    while base < hight:
        print(hight*"*")
        hight-=1
    return

def makepiramide(hight):
    makepiramidefirsthalf(hight,0)
    makepiramidesecondhalf(hight,0)
    return 0


Topofpiramide = int(input('Hight of the piramide: '))
base = 0
makepiramide(Topofpiramide)