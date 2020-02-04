def makepiramide(hight):
    if hight ==0:
        return 0

    for x in range(hight):
        print("*", end="")
    print("")
    return makepiramide(hight-1)


Topofpiramide = int(input('Hight of the piramide: '))

makepiramide(Topofpiramide)
print(Topofpiramide)