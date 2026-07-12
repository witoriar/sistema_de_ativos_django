from enum  import Enum 

class TipoAtivo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    APLICACAO_WEB = 4

class Severidade(Enum):

    BAIXA = 1
    MEDIA = 2
    ALTA = 3
    CRITICA = 4

class StatusVulnerabilidades(Enum):

    ABERTA = 1
    EM_TRATAMENTO = 2
    CORRIGIDA = 3 
    ACEITA = 4


class Ativo:

    def __init__(self, id, hostname, responsavel, setor, tipo):
        self.id = id
        self.hostname = hostname
        self.responsavel = responsavel
        self.setor = setor
        self.tipo = tipo
        self.vulnerabilidades = []

    
    def adicionar_vulnerabilidade(self, descricao, severidade, status):
        vulnerabilidades = {
            "descricao": descricao,
            "severidade": severidade,
            "status": status
        }
        self.vulnerabilidades.append(vulnerabilidades)


    def to_dict(self):

        return {
            "id": self.id,
            "hostname": self.hostname,
            "responsavel": self.responsavel,
            "setor": self.setor,
            "tipo": self.tipo,
            "vulnerabilidades": self.vulnerabilidades
        }
    
    def __str__(self):
        return f"[{self.tipo}] {self.hostname} - Responsável: {self.responsavel}"
