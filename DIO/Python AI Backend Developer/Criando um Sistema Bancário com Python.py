mensagem = f'''    
[1] - Depósito
[2] - Saque
[3] - Extrato
[0] - Sair
'''

opcao = 0

saldo = 0.0
valor = 0.0
extrato = "########## EXTRATO ##########\n"

LIMITE_SAQUES = 3
quantidade_saques = 0


while True:
    
    print(mensagem)
    opcao = int(input("Opção -> "))
    
    
    # Depósito
    if opcao == 1: 
        valor = float(input("Insira o valor para depositar -> R$"))
        
        if valor < 0:
            print("Valor inválido !")
        else:
            saldo += valor
            extrato = extrato + f"\nDepósito : R${valor:0.2f}"
    
        
    # Saque    
    elif opcao == 2:   
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
            
    
    # Extrato        
    elif opcao == 3:
        print(extrato)
        print(f"\nSaldo : R${saldo:.2f}")
        
        
    # Sair
    elif opcao == 0:
        print("Saindo...")
        break
    
    else:
        print("Comando não reconhecido !")
        
    print("\n===================================")
