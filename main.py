clientes = []
contas = {}

def cadastrar_cliente():
    
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    telefone = input("Digite o número de celular do cliente: ")
    email = input("Digite o email do cliente: ")

    novo_cliente = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "email": email
    }
   
    clientes.append(novo_cliente)
    print("Cliente cadastrado com sucesso!")
    

def criar_conta():

    numero_conta = input("Digite o número da conta: ")
    
    if numero_conta in contas:
        print("Já existe uma conta com esse número!")

    cpf_cliente = input("Digite o CPF do titular: ")

    contas[numero_conta] = {
        "cpf_cliente": cpf_cliente,
        "saldo": 0.0
    }

    print(f'Conta {numero_conta} criada com sucesso!')

def listar_contas():

    if len(contas) == 0:
        print("Ainda não existem contas cadastradas.")
        return
    
    for numero_conta, dados in contas.items():
        print(f'Conta: {numero_conta} | CPF do titular: {dados["cpf_cliente"]} | Saldo: R${dados["saldo"]}')

def ver_saldo():
    
    numero_conta = input("Digite o número da conta: ")
    
    if numero_conta in contas:
        print(f'CPF do titular: {contas[numero_conta]["cpf_cliente"]}')
        print(f'Saldo da conta: {contas[numero_conta]["saldo"]}')
    else:
        print("Erro. Conta não encontrada.")

def depositar():
    
    numero_conta = input("Digite o número da conta para depósito: ")

    if numero_conta in contas:
        valor_deposito = float(input("Digite o valor do depósito: R$"))
        if valor_deposito > 0:
            contas[numero_conta]["saldo"] += valor_deposito
            print(f'Depósito realizado! Novo valor do saldo: R${contas[numero_conta]["saldo"]}')
        else:
            print("Valor mínimo de depósito não foi atingido")
    else:
        print("Erro. Conta não encontrada.")

def sacar():
    
    numero_conta = input("Digite o número da conta para saque: ")

    if numero_conta in contas:
        valor_saque = float(input("Digite o valor do saque: R$"))
        if valor_saque > 0:
            if valor_saque <= contas[numero_conta]["saldo"]:
                contas[numero_conta]["saldo"] -= valor_saque
                print(f'Saque realizado! Novo valor do saldo: R${contas[numero_conta]["saldo"]}')
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("O valor do saque tem que ser maior que 0")
    else:
        print("Erro. Conta não encontrada.")
  
while True:
    print("\n--- MENU ---")
    print("1. Cadastrar cliente")
    print("2. Criar conta")
    print("3. Ver saldo")
    print("4. Depositar")
    print("5. Sacar")
    print("6. Listar contas")
    
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
        listar_contas()
    elif opcao == "7":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
