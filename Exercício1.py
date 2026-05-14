"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

numero_str = input("Insira um número inteiro: ")

try:
    numero_inteiro = int(numero_str)
    if numero_inteiro % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
except ValueError:
    print("Isso não é um número inteiro.")


hora_str = input("Insira a hora: ")

try:
    hora = int(hora_str)
    if 0 <= hora <= 11:
        print("Bom dia!")
    elif 12 <= hora <= 17:
        print("Boa tarde!")
    elif 18 <= hora <= 23:
        print("Boa noite!")
    else:
        print("Hora inválida!")
except ValueError:
    print("Por favor, digite um número inteiro válido")


primeiro_nome = input("Insira o seu primeiro nome: ")

nome = str(primeiro_nome)
if len(nome) <= 4:
    print("O seu nome é curto!")
elif 5 <= len(nome) <= 6:
    print("O seu nome é normal!")
else:
    print("O seu nome é muito grande!")
