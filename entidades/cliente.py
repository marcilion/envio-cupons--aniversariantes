class Cliente():
    def __init__(self, nome_completo:str, data_nascimento: str, email, data_criacao: str) -> None:
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.email = email
        self.data_criacao = data_criacao
        