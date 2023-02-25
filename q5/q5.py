string = 'desafio'
stringReversa = []
indice = len(string)

while indice > 0:
    stringReversa += (string[indice - 1])
    indice -= 1

resultado =''.join(stringReversa)
print(resultado)