menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

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

def criar_usuario():
    nome = input("Digite seu Nome: "),
    data_nascimento = input("Digite sua Data de Nascimento: "),
    cpf = int(input("Digite seu CPF: ")),
    endereco = input("Digite seu endereco: ")

    usuario = { cpf: {nome,cpf,data_nascimento,endereco} }

    print(usuario)
       


while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = depositar(saldo, valor, extrato)


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

    elif opcao == "e":
        extratos(saldo, extrato=extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")