import json
#1 --------------------------------------------
'''def escrever_em_arquivo(nome):

    f = open(nome, 'w')
    lista = ["1","2","3","4","5"," ","66","77","88","99","cem"]
    lista_str = "\n".join(lista)
    f.write(lista_str)
    f.close()

escrever_em_arquivo("newfile.txt")'''

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#2
'''print("\n")
def read_fichiero(nome):
        f = open(nome, "r")
        # f = open(nome)
        #data  = f.read().split("\n")
        #print(data)
        lines = f.readlines()
        print(lines)
        novalistta = [ l.strip() for l in lines ]
       # nova_lista = []
        #for l in lines:
         #   nova_lista.append(l.strip())
        print(novalistta)
       # f.close() ->  with já inclui o close

read_fichiero("newfile.txt")'''

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
#3 e #4
'''print("\n")
def read_write_file_impar(nome):
    with open(nome, "r") as f:
            linhas = f.readlines()
            for i, linha in enumerate(linhas):
                if (i + 1) % 2 != 0:
                    print(linha.strip())

arquivo = "newfile.txt"
read_write_file_impar(arquivo)'''

#*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#5
'''print("\n\n")

def escrever_arq(nome_arq):
    try:
        with open(nome_arq, "w") as f:
            lista_ = ["1", "2", "3", "4", "5", " ", "66", "77", "88", "99", "cem"]
            lista_str_ = "\n".join(lista_)
            f.write(lista_str_)
            print(f"Arquivo {nome_arq} criado com sucesso.")
    except FileNotFoundError:
            print("Arquivo não encontrado.")

escrever_arq("")'''
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*--*---*--*-*---*-*-*-*-*-*-*--
#6
'''def read_write_file_dobro(nome):
    try:
        with open(nome, "r") as f:
                linhas = f.readlines()
                for linha in linhas:
                    linha = linha.strip()
                    if linha.isnumeric():
                        valor = int(linha)
                        print(valor *2)
                    else:
                        print(0)
    except FileNotFoundError:
        print("Ficheiro nao encontrado")

arquivo = "newfile.txt"
read_write_file_dobro(arquivo)'''
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#7
'''def read_write_file_dobro(nome):
    try:
        with open(nome, "r") as f:
                linhas = f.readlines()
                for linha in linhas:
                    linha = linha.strip()
                    if linha.isnumeric():
                        valor = int(linha)
                        print(valor *2)
                    else:
                        print(0)
    except FileNotFoundError:
        raise FileNotFoundError(f"Ficheiro '{nome}' nao encontrado")
    except Exception as exp:
        raise Exception(f"Erro ao processar o ficheiro '{nome}': {str(exp)}")

try:
    arquivo = "newfile.txt"
except FileNotFoundError as fnotfound:
    print(fnotfound)
except Exception as error:
    print(error)
    
read_write_file_dobro(arquivo)'''
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*
#8
'''dados = {"João": 13, "Francisco": 24, "Maria": 30, "Ana": 22}

nomes_json= "dados.json"

with open(nomes_json, "w") as arquivo:
    json.dump(dados, arquivo)

print(f'O dicionário foi salvo em {nomes_json}')

with open(nomes_json, "r") as arquivo:
    dados_carregados = json.load(arquivo)

print("Dicionário carregado:")
print(dados_carregados)'''

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-----------------------------
#9 

import json

dicionarios = [
    {"João": 13},
    {"Francisco": 24},
    {"Maria": 30},
    {"Ana": 22}
]

arquivo_json = "dados_lista.json"

with open(arquivo_json, "w") as f:
    json.dump(dicionarios, f)

print(f'A lista de dicionários foi salva em {arquivo_json}')

with open(arquivo_json, "r") as f:
    lista_carregada = json.load(f)

print("Lista de dicionários carregada:")
print(lista_carregada)

#-*-*-*-*-*-*-*************************************************************************







