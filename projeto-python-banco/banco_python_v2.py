def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    [nu] Novo usuario
    [nc] Nova Conta
    [lc] Listar Conta

    => """

    return menu

def sacar(*,saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor > saldo:
        print("Operação falhou ! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! Valor superior ao limite de saque.")
    elif numero_saques > LIMITE_SAQUES:
        print("Operação falhou! Você atingiu o limite de saques diários.")    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}"
        numero_saques += 1
        print(f"Sucesso! Você Sacou: R$ {valor:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def extratos(saldo,*, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Digite seu CPF: ")
    verifica_usuario = validar_cpf(cpf,usuarios)

    if verifica_usuario:
        print("Usuario já cadastrado!")
        return
    
    nome = input("Digite seu Nome: ")
    data_nascimento = input("Digite sua Data de Nascimento: ")
    endereco = input("Digite seu endereco: ")

    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})  
    
def validar_cpf(cpf,usuarios):
    usuario_validado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_validado[0] if usuario_validado else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o número do CPF (Somente numeros): ")
    usuario_validado = validar_cpf(cpf, usuarios)

    if usuario_validado:
        print("Conta Criada com Sucesso!")
        return {"agencia":agencia , "numero_conta":numero_conta, "usuario":usuario_validado}
    
    print("Usuario nao encontrado!")

def listar_contas(contas):
    for conta in contas:
        print(f"""
        Agencia:\t{conta["agencia"]}
        Numero da Conta:{conta["numero_conta"]}
        Nome:\t\t{conta["usuario"]["nome"]}
    """)

def main():
    AGENCIA = "001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = input(menu())

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "e":
            extratos(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()