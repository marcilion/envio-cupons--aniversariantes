from calendar import isleap
from datetime import datetime
class Cliente():
    def __init__(self, nome_completo:str, data_nascimento: str, email, data_criacao: str) -> None:
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.email = email
        self.data_criacao = data_criacao

        def eh_ano_bissexto(selt):
            ano_atual = datetime.now().year
            return isleap(ano_atual) == False
        
        def faz_anivesario_ano_bissexto(self):
            dia, mes = self.data_nascimento.split("/")[:2]  
            return dia == "29" and mes == "02"
        
        def get_dia_mes_aniversario(self) -> dict["dia": str, "mes": str, "ano": str]:
            dia, mes = self.data_nascimento.split("/")[:2] 
            
            if self.eh_ano_bissexto() and self.faz_anivesario_ano_bissexto():
                dia = "28"

            data = {
                "dia": int(dia),
                "mes": int(mes)
                                
            }
            return data
        
        @staticmethod
        def mostrar_clientes(cliente: list) -> None:
            for cliente in cliente:
                print(f"NOME: {cliente.nome_completo}\nDATA NASCIMENTO: {cliente.data_nascimento}\nEMAIL: {cliente.email}\nDATA CRIACAO: {cliente.data_criacao}")      