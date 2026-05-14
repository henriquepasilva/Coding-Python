from abc import ABC, abstractmethod

class PessoaULP(ABC):
    def __init__(self, nome: str, identificacao: str):
        self.nome = nome
        self.identificacao = identificacao

    def getPermissoes(self):
        pass

    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Identificação: {self.identificacao}\n"
            f"Permissões: {self.getPermissoes()}"
        )

class Aluno(PessoaULP):
    def getPermissoes(self):
        return["CONSULTAR"]

class Docente(PessoaULP):
    def getPermissoes(self):
        return["CONSULTAR", "LANCAR", "ASSINAR"]

class Secretaria(PessoaULP):
    def getPermissoes(self):
        return["CRIAR", "CONSULTAR", "LANCAR", "PUBLICAR"]

aluno = Aluno("Henrique Silva", "A1234")
docente = Docente("António Camacho", "D2334")
secretaria = Secretaria("Glória Santos", "S5677")

print(aluno)
print()
print(docente)
print()
print(secretaria)