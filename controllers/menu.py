import datetime
import repositorio.clientes as clientes_repositorio
from entidades.cliente import Cliente
from datetime import datetime
from servicos.servico_email import email_eh_valido, enviar_emails
def iniciar_menu_principal():
    while True: 
        print("1- Consultar clientes\n2- Cadastrar cliente\3- Eviar cupons via email aos clientes aniversariantes\n 4 - Sair")
        opcao_escolhida = input("Digite uma opção: ")
        match opcao_escolhida:
            case '1':               
                iniciar_submenu_consulta_clientes()
            case '2':
                iniciar_cadastro_cliente()
            case '3':
                iniciar_cadastro_cliente()
            case '4':
                break
            case other:
                print("opção inválida")    


def iniciar_submenu_consulta_clientes():  
     print("\nCONSULTAR CLIENTES\n")  
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
    print("\nCONSULTAR CLIENTES ANIVERSARIANTES\n")
    anivesariantes = clientes_repositorio.get_clientes_aniversariantes()
    if len(anivesariantes) > 0:
        Cliente.mostrar_clientes(anivesariantes)
    else:
        print("ninguem faz aniversario hoje")


def mostrar_clientes_por_mes_aniversario():
    print("\nCONSULTAR CLIENTES ANIVERSARIANTES DE UM MÊS ESPECIFICO\n")
    mes = int(input("Digite o número do mês (1-12): \n"))
    anivesariantes = clientes_repositorio.get_clientes_por_mes_aniversario(mes)
    if len(anivesariantes) > 0:
        Cliente.mostrar_clientes(anivesariantes)
    else:
        print("ninguem faz aniversario neste mês") 

def iniciar_cadastro_cliente():
    print("\nCADASTRAR CLIENTES\n") 
    
    nome_completo = input("nome completo: ")
    data_nascimento = input("data nascimento: ")
    email = input("email: ")
    data_registro = datetime.today().strftime('%d/%m/%y, %H:%M:%S')

    novo_cliente = Cliente(
        data_criacao=data_registro,
        data_nascimento=data_nascimento,
        email=email,
        nome_completo=nome_completo
    )

    foi_salvo = clientes_repositorio.salvar_cliente(novo_cliente)
    if foi_salvo:
        print("cliente salvo com sucesso")
    else:
        print("cliente não foi salvo")

def iniciar_envio_emails():
    print("\nENVIAR CUPONS VIA EMAIL\n")
    aniversariantes = clientes_repositorio.get_clientes_aniversariantes()
    aniversariantes_com_email_valido = [aniversariantes for aniversariante in aniversariantes if email_eh_valido(aniversariante.email)]

    quantidade = len(aniversariantes)

    if quantidade == 0:
        print("ninguém com email valido faz anivesário hoje")
        return 

    escolha = input(f"{quantidade} email(s) para ser(em) envado(s), deseja enviar ou ver os destiantarios")
    escolha == escolha.upper()
    if escolha == "VER":
        Cliente.mostrar_clientes(aniversariantes_com_email_valido)
    elif escolha == "ENVIAR":
        destinartarios = [aniversariantes_com_email_valido]
        for aniversariante in aniversariantes:
            destinartarios.append(aniversariantes.motar_objeto_email())
        quantidade_emails_enviados = enviar_emails()

        if quantidade_emails_enviados > 0:
           print(f"{quantidade_emails_enviados} email(s) enviado(s)")  
        else: 
            print("nenhum email enviado")
    else:
        print("Escolha inválida") 