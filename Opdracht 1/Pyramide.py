def makepiramidefirsthalf(hight,base):
    if base < hight:
        for x in range(base):
            print("*", end="")
        print("")
        makepiramidefirsthalf(hight, base+1)
    return 0

def makepiramidesecondhalf(hight):
    if hight ==0:
        return 0
    for x in range(hight):
        print("*", end="")
    print("")
    return makepiramidesecondhalf(hight-1)

def makepiramide(hight):
    makepiramidefirsthalf(hight,0)
    makepiramidesecondhalf(hight)
    return 0


Topofpiramide = int(input('Hight of the piramide: '))
base = 0    #Base is niet nodig maar als ik later de pyramide anders wil maken, dan kan dat
makepiramide(Topofpiramide)