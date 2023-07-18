from calendar import isleap
from datetime import datetime
class Cliente():
    def __init__(self, nome_completo:str, data_nascimento: str, email, data_criacao: str) -> None:
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.email = email
        self.data_criacao = data_criacao
        def get__data_nascimento(self) -> dict["dia": str, "mes": str, "ano": str]:
            lista_data = self.data_nascimento.split("/")

            ano_atual = datetime.now().year
            #if isleap()
            data = {
                "dia": lista_data[0],
                "mes": lista_data[1],
                "ano": lista_data[2]
            }
            return data
        
        @staticmethod
        def mostrar_clientes(cliente: list) -> None:
            for cliente in cliente:
                print(f"NOME: {cliente.nome_completo}\nDATA NASCIMENTO: {cliente.data_nascimento}\nEMAIL: {cliente.email}\nDATA CRIACAO: {cliente.data_criacao}")      