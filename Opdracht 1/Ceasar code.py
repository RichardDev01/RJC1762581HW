'''
Caesarcijfer
Schrijf een programma voor Caesarcijfers. Voorbeeld van de interactie met het programma:

nog maken
'''

alfabet= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
mystring = "hallo"

#ik heb een eigen alfabet gemaakt en dan verander ik de plaats van het index nummer om zo een caesar cypher te maken
n=3 #nummer van verplaatsen van index
for i in mystring:
    print(alfabet[alfabet.index(i)+n%26], end="")
