class PautaULP:
    def __init__(self):
        self.notas = []
        self.estado = None

    def _tem_permissao(self, ator, permissao):
        return permissao in ator.getPermissoes()

    def criar(self, ator):
        if not self._tem_permissao(ator, "CRIAR"):
            return

        if self.estado is None:
            self.estado = "CRIADA"

    def lancar(self, ator, notas):
        if not self._tem_permissao(ator, "LANCAR"):
            return

        if self.estado in [None, "ASSINADA", "PUBLICADA"]:
            return

        self.notas = notas
        self.estado = "LANCADA"

    def consultar(self, ator):
        if not self._tem_permissao(ator, "CONSULTAR"):
            return None

        return self.notas

    def assinar(self, ator):
        if not self._tem_permissao(ator, "ASSINAR"):
            return

        if self.estado == "LANCADA":
            self.estado = "ASSINADA"

    def publicar(self, ator):
        if not self._tem_permissao(ator, "PUBLICAR"):
            return

        if self.estado == "ASSINADA":
            self.estado = "PUBLICADA"
