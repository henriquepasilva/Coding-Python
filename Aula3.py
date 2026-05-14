"""
Fatiamento de strings
0123456789
Olá mundo
-9876543210
Fatiamento [i:f:p] [::]
i - ínicio do fatiamento
f - fim do fatiamento
p - passo do fatiamento (de quantos em quantos caractéres imprime)
Obs: a função len retorna a quantidade
de caractéres da str
"""

variavel = "Olá mundo"
print(variavel[3:]) #faz o tal "fatiamento" ou seja, desde
                    #o caractére 3 até ao fim (neste caso)
print(len(variavel)) #conta os caractéres
print((variavel[0:9:2]))
