nome = ""
cpf = ""
numero_conta = ""
saldo = 0

def cadastrar_cliente():
    global nome, cpf, telefone, email
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    telefone = input("Digite o número de celular do cliente: ")
    email = input("Digite o email do cliente: ")
    print("Cliente cadastrado com sucesso!")
    

def criar_conta():
        global numero_conta
        numero_conta = input("Digite o número da conta: ")
        print(f"Conta criada com sucesso! Nome: {nome}, CPF: {cpf}, Número da Conta: {numero_conta}, Telefone: {telefone}, Email: {email}.")

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
    print("1. Cadastrar cliente")
    print("2. Criar conta")
    print("3. Ver saldo")
    print("4. Depositar")
    print("5. Sacar")
    print("6. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        criar_conta()
    elif opcao == "3":
        ver_saldo()
    elif opcao == "4":
        depositar()
    elif opcao == "5":
        sacar()
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
