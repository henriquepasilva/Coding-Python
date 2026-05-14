a=1
b=1
print(a is b) #ambas as variáveis a e b, elas referenciam o mesmo objeto inteiro na memória, daí a is b é True

a=[1]
b=[1]
print(a is b) # retorna False porque a e b se referem a objetos diferentes na memória.

a=[1]
b=a
print(a is b) # a e b apontam para a mesma lista na memória, tornando a is b verdadeiro.

a=[1]
b=a+[]
print(a is b) # a, e essa nova lista não é o mesmo objeto que a. Portanto, a is b é False.