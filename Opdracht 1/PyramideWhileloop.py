def makepiramidefirsthalf(hight,base):

    while base < hight:
        print(base*"*")
        base+=1
        makepiramidefirsthalf(hight, base+1)
    return 0

def makepiramidesecondhalf(hight,base):
    if hight ==0:
        return 0
    base=0
    while base < hight:
        print(base*"*")
        base+=1
    return makepiramidesecondhalf(hight-1)

def makepiramide(hight):
    makepiramidefirsthalf(hight,0)
    makepiramidesecondhalf(hight,0)
    return 0


Topofpiramide = int(input('Hight of the piramide: '))
base = 0
makepiramide(Topofpiramide)