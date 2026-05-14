from functools import reduce

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return self.nome

class Aluno(Pessoa):
    pass

class Docente(Pessoa):
    pass

class Secretaria(Pessoa):
    pass

pessoas = [
    Aluno("João"),
    Docente("Mário"),
    Secretaria("Cândida"),
    Aluno("Gonçalo"),
    Docente("Henrique"),
    Secretaria("Maria")
]

pessoas_ordenadas = sorted(pessoas, key=lambda p: p.nome)

print("Lista ordenada:")
for p in pessoas_ordenadas:
    print(p.nome)

maior_nome = reduce(
    lambda p1, p2: p1 if p1.nome > p2.nome else p2,
    pessoas
)

print("\nNome alfabéticamente maior:")
print(maior_nome.nome)