from calendar import isleap
from datetime import datetime
import utils.tabela as tabela
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
        def mostrar_clientes(clientes: list) -> None:
            largura = 30
            cabecalho = tabela.montar_linha(
                ["nome completo", "data nascimento", "email", "cliente desde"], eh_cabecalho=True,
                largura_coluna=largura)
            
            print(cabecalho)
            contador = 0
            for cliente in cliente:
                linha = tabela.montar_linha(
                    ["cliente.nome_completo","cliente.data_nascimento", "cliente.email", "cliente.data_criacao"], 
                largura_coluna=largura)

                print(linha)
                contador +=1
                if contador == len(clientes):
                    print("-" * len(linha))     