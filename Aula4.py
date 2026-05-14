"""
Introdução ao try/expect
try -> tentar executar o código
expect -> ocurreu algum erro a tentar executar
"""

numero_str = input("Vou dobrar o número que tu digitares: ")

try:
    print('STR: ', numero_str )
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.0f}')
except:
    print("Isso não é um número!")

#if numero_str.isdigit():
#    numero_float = float(numero_str)
#    print(f'O dobro de {numero_str} é {numero_float * 2:.0f}')
#else:
#    print("Isso não é um número!")