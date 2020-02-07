'''
Caesarcijfer
Schrijf een programma voor Caesarcijfers. Voorbeeld van de interactie met het programma:

nog maken
'''

alphabet= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
mystring = "hallo"

#print(alphabet[29%26])
n=3
for i in mystring:
    print(alphabet[alphabet.index(i)+n%26], end="")
