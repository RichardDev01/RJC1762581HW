'''
https://www.youtube.com/watch?v=Qu3dThVy6KQ
https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Itertools
https://docs.python.org/2/library/itertools.html
'''

import  itertools
ListKleurenNamen = ["zwart", "wit","groen","blauw","paars","rood"]
result = itertools.product(ListKleurenNamen, repeat=4)

print(result)
mainlist = []

for item in result:
    #print(item[0:4])
    mainlist.append(list(item))
print(mainlist[256][1])

