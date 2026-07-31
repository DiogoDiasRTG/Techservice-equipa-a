class Tecnico:
    def __init__(
        self,
        nome,
        especialidade="",
        telefone="",
        email="",
        id_tecnico=None,
        status=1
    ):
        self.id_tecnico = id_tecnico
        self.nome = nome
        self.especialidade = especialidade
        self.telefone = telefone
        self.email = email
        self.status = status