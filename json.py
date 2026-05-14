def criar_fh(nome):
    with open(nome, 'w') as f_obj:
        f_obj.write("1\n2\n3\n4\n5\n\n66\n77\n88\n99\ncem")


def ler_fh(nome):
    with open(nome, 'r') as f_obj:
        texto = f_obj.read()
    return texto


def linhas_impares(nome):
    try:
        with open (nome) as f_obg:
            conteudo = f_obg.readlines()
            for a in conteudo[1::2]:
                    print(a)
    except FileNotFoundError as erro: 
                                    print(erro)
        

#criar_fh('teste.txt')

#print(ler_fh('teste.txt'))

print(linhas_impares('teste.txt'))