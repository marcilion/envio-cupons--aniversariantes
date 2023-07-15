import repositorio.clientes as clientes_repositorio
from entidades.cliente import Cliente
import dotenv
def iniciar_menu_principal():
    while True: 
        print("1- Consultar clientes\n2- Cadastrar cliente\3- Eviar cupons via email aos clientes aniversariantes\n 4 - Sair")
        opcao_escolhida = input("Digite uma opção: ")
        match opcao_escolhida:
            case '1':
                print("CONSULTAR CLIENTES")
                iniciar_submenu_consulta_clientes()
            case '2':
                print(" CADASTRAR CLIENTES")
            case '3':
                print("ENVIAR CUPONS VIA EMAIL")
            case '4':
                break
            case other:
                print("opção inválida")    


def iniciar_submenu_consulta_clientes():    
     while True:
        print("1- Todos\n2- Anivesariantes\3- Aniversariantes de um mês especifico\n 4 - Voltar para o menu principal")
        opcao_escolhida = input("Digite uma opção: ")        
        match opcao_escolhida:
            case '1':
                mostrar_todos_clientes
                break       
            case '2':
                mostrar_clientes_aniversariantes()               
                break
            case '3':
                mostrar_clientes_por_mes_aniversario
                break
            case '4':
                break
            case other:
                print("opção inválida")

def mostrar_todos_clientes():
    print("\nCONSULTAR  TODOS OS CLIENTES")
    clientes = clientes_repositorio.get_todos_clientes()
    Cliente.mostrar_clientes(clientes)
    
def mostrar_clientes_aniversariantes():
    print("CONSULTAR CLIENTES ANIVERSARIANTES")
    hoje = datetime.today()
    dia_atual = hoje.day
    mes_atual = hoje.month
 
    anivesariantes = clientes_repositorio.get_clientes_por_mes_aniversario(dia=dia_atual, mes=mes_atual)
    Cliente.mostrar_clientes(anivesariantes)

def mostrar_clientes_por_mes_aniversario():
    print("CONSULTAR CLIENTES ANIVERSARIANTES DE UM MÊS ESPECIFICO")
    mes = int(input("Digite o número do mês (1-12)"))
    anivesariantes = clientes_repositorio.get_clientes_por_mes_aniversario(mes)
    Cliente.mostrar_clientes(anivesariantes)
   

