class Cliente:
    def __init__(self, nome, cpf, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

class Conta:
    def __init__(self, numero_conta, cpf_cliente):
        self.numero_conta = numero_conta
        self.cpf_cliente = cpf_cliente
        self.saldo = 0.0

    def depositar(self, valor):
        if valor <= 0:
            return False

        self.saldo += valor
        return True

    def sacar(self, valor):
        if valor <= 0:
            return False

        self.saldo -= valor
        return True

    def ver_saldo(self):
        return self.saldo

class Banco:
    def __init__(self):
        
        self.clientes = {}
        self.contas = {}

    def cadastrar_cliente(self, nome, cpf, telefone, email):
        if cpf in self.clientes:
            return False

        novo_cliente = Cliente(nome, cpf, telefone, email)
        self.clientes[cpf] = novo_cliente

        return True

    def criar_conta(self, numero_conta, cpf_cliente):
        if numero_conta in self.contas:
            return False

        if cpf_cliente not in self.clientes:
            return False

        nova_conta = Conta(numero_conta, cpf_cliente)
        self.contas[numero_conta] = nova_conta

        return True

    def depositar(self, numero_conta, valor):
        
        conta = self.contas.get(numero_conta)

        if conta is None:
            return False

        return conta.depositar(valor)

    def sacar(self, numero_conta, valor):
        conta = self.contas.get(numero_conta)

        if conta is None:
            return False

        return conta.sacar(valor)

    def ver_saldo(self, numero_conta):
        return self.contas.get(numero_conta)