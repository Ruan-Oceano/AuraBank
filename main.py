saldo = 0

def ver_saldo():
    print(f'Saldo atual: R${saldo}')
    return saldo

def depositar():
    global saldo
    valor_deposito = float(input("Digite o valor do depósito: "))
    saldo += valor_deposito
    print(f'Depósito realizado! Novo valor do saldo: R${saldo}')
    return saldo

def sacar():
    global saldo
    valor_saque = float(input("Digite o valor do saque: "))
    if valor_saque <= saldo:
        saldo -= valor_saque
        print(f'Saque realizado! Novo valor do saldo: R${saldo}')
        return saldo
    else:
        print("Saldo insuficiente para saque.")
        return saldo
  
while True:
    print("\n--- MENU ---")
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        ver_saldo()
    elif opcao == "2":
        depositar()
    elif opcao == "3":
        sacar()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
