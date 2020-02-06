'''
Compressie
Schrijf een compress-programma, dat uit een gegeven bestand een nieuwe bestand maakt, waarbij van iedere regel alle spaties en tabs aan het begin van de regel zijn verwijderd.
Verder zijn alle lege regels verwijderd (een lege regel bevat ’\n’ , eventueel voorafgegaan door spaties en tabs(‘\t’)).

nog maken
'''
filename = "compressie.txt"
filenametarget = "compressietarget.txt"
try:
    infile = open(filename, "r")
    inhoud = infile.readlines()
    infile.close()
    outfile = open(filenametarget, "w")

    for x in inhoud:
        print(x)
        if "\n" in x:
            outfile.write(x[:-1])
            print("empty")
        else:
            outfile.write(x)
    outfile.close()
except FileNotFoundError:
    print("Bestand bestaat niet")


