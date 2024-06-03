def menu():
    print("[1] - Depósito\n[2] - Saque\n[3] - Extrato\n[4] - Criar Usuário\n[5] - Criar Conta Corrente\n[6] - Listar Contas\n[0] - Sair\n")
    return int(input("Opção -> "))




def deposito(saldo, extrato):
    valor = float(input("Insira o valor para depositar -> R$"))

    if valor < 0:
        print("Valor inválido !")
    else:
        saldo += valor
        extrato = extrato + f"\nDepósito : R${valor:0.2f}"

    return saldo, extrato



def saque(*, saldo, extrato, quantidade_saques, LIMITE_SAQUES):
    valor = float(input("Insira o valor para sacar -> R$"))

    if quantidade_saques == LIMITE_SAQUES:
        print("Quantidade de saques diários excedidos !")
    elif saldo < valor:
        print("Saldo indisponível !")
    elif valor > 500:
        print("Esse valor excede o limite de R$500.00")
    else:
        quantidade_saques += 1
        saldo -= valor
        extrato = extrato + f"\nSaque : R${valor:0.2f}"

    return saldo, extrato, quantidade_saques




def mostrar_extrato(saldo, /, *, extrato):
    print(extrato)
    print(f"\nSaldo : R${saldo:.2f}")



def criar_usuario(usuarios):
    cpf = input("Insira o CPF -> ")
    nome = input("Insira o nome -> ")
    data_nascimento = input("Insira a Data de Nascimento (dd-mm-aaaa) -> ")

    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            print("Usuário já Existe!")
            return

    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado) -> ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})



def criar_conta(AGENCIA, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = None
    
    for user in usuarios:
        if cpf == user["cpf"]:
            usuario = user
            break

    if usuario:
        numero_conta += 1
        contas.append({"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario})
    else:
        print("\nUsuário não encontrado. A conta não pode ser criada.")
    return numero_conta



def listar_contas(contas):
    print("\n########## CONTAS ##########\n")
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {conta['usuario']['cpf']}")
 


def main():
    extrato = "\n########## EXTRATO ##########\n"
    opcao = 0
    saldo = 0.0
    LIMITE_SAQUES = 3
    quantidade_saques = 0
    usuarios = []
    contas = []
    numero_conta = 0
    AGENCIA = "0001"
    
    while True:
        opcao = menu()
        
        if opcao == 1: 
            saldo, extrato = deposito(saldo, extrato)
        
        elif opcao == 2: 
            saldo, extrato, quantidade_saques = saque(saldo=saldo, extrato=extrato, quantidade_saques=quantidade_saques, LIMITE_SAQUES=LIMITE_SAQUES)
            
        elif opcao == 3:
            mostrar_extrato(saldo, extrato=extrato)
        
        elif opcao == 4:
            criar_usuario(usuarios)
        
        elif opcao == 5:
            numero_conta = criar_conta(AGENCIA, numero_conta, usuarios, contas)
        
        elif opcao == 6:
            listar_contas(contas)
            
        elif opcao == 0:
            print("Saindo...")
            break
    
        else:
            print("Comando não reconhecido !")
        
        print("\n===================================")
        
main()
