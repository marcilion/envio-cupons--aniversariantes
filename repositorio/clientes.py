from entidades.cliente import Cliente
import os
#import dotenv
from datetime import datetime

#dotenv.load_dotenv()
CAMINHO_ARQUIVO_DADOS = os.getenv("CAMINHO_DADOS_ARQUIVO")

def get_todos_clientes() -> list:
    clientes = []
    with open(CAMINHO_ARQUIVO_DADOS, 'r', encoding="utf8") as arquivo:
       linha_atual = 0 
       for linha in arquivo:
            if linha_atual == 0:
               linha_atual += 1
            else:
               lista_valores = linha.split(",")
               Cliente = Cliente(
                  nome_completo=lista_valores[0],
                  data_nascimento=lista_valores[1],
                  email=lista_valores[2],
                  data_criacao=lista_valores[3].replace("\n", "")
               )
               clientes.append(Cliente)

    return clientes

def get_clientes_aniversariantes(mes:int, dia: int) -> list[Cliente]:
    clientes = get_todos_clientes()
    
    hoje = datetime.today()
    dia_atual = hoje.day
    mes_atual = hoje.month

    dia = datetime.today().day
    mes = datetime.today().month

    aniversariantes = []
    for cliente in clientes:
        data_nascimento = cliente.get_data_nascimento()
        if data_nascimento["dia"] == dia_atual and data_nascimento["mes"] == mes_atual:
            aniversariantes.append(cliente)

    return aniversariantes   

def get_clientes_por_mes_aniversario(mes: int) -> list[Cliente]:     
    clientes = get_todos_clientes()    
    aniversariantes = []
    for cliente in clientes:
        data_nascimento = cliente.get_data_nascimento()
        if data_nascimento["mes"] == mes:
            aniversariantes.append(cliente)

    return aniversariantes   
        