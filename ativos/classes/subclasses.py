from .ativo import Ativo, TipoAtivo

class Servidor(Ativo):

    def __init__(self, id, hostname, responsavel, setor):
        super().__init__(id, hostname, responsavel, setor, TipoAtivo.SERVIDOR.name)

    def __str__(self):
        return f"[SERVIDOR] {self.hostname} - Responsável: {self.responsavel}"
    
class Notebook(Ativo):

    def __init__(self, id, hostname, responsavel, setor):
        super().__init__(id, hostname, responsavel, setor, TipoAtivo.NOTEBOOK.name)

    def __str__(self):
        return f"[NOTEBOOK] {self.hostname} - Responsável: {self.responsavel}"
    

class Roteador(Ativo):

    def __init__(self, id, hostname, responsavel, setor):
        super().__init__(id, hostname, responsavel, setor, TipoAtivo.ROTEADOR.name)

    def __str__(self):
        return f"[ROTEADOR] {self.hostname} - Responsável: {self.responsavel}"
    

class AplicacaoWeb(Ativo):

    def __init__(self, id, hostname, responsavel, setor):
        super().__init__(id, hostname, responsavel, setor, TipoAtivo.APLICACAO_WEB.name)

    def __str__(self):
        return f"[APLICACAO_WEB] {self.hostname} - Responsável: {self.responsavel}"
    

def criar_ativo(id, hostname, responsavel, setor, tipo):

    tipos = {
        TipoAtivo.SERVIDOR.name: Servidor,
        TipoAtivo.NOTEBOOK.name: Notebook,
        TipoAtivo.ROTEADOR.name: Roteador,
        TipoAtivo.APLICACAO_WEB.name: AplicacaoWeb,
    }

    classe = tipos.get(tipo.upper())
    if classe is None:
        raise ValueError(f"Tipo de ativo inválido: {tipo}")
    return classe(id, hostname, responsavel, setor)
    
    
