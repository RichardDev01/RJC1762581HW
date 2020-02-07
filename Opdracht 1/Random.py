'''
Random
Schrijf een programma dat een willekeurig getal kiest en de gebruiker net zo lang laat gokken tot dat ze het goed hebben.
'''
import random
number = random.randrange(10)
while True:
    gues = int(input("kies een getoal tussen 0 en 10:  "))
    if gues == number:
        print("goodjob")
        break       #het programma stopt pas zodra het juiste nummer is geraden