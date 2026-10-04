clientes = []
contas = {}


def cadastrar_cliente(nome, cpf, telefone, email):

    novo_cliente = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "email": email
    }

    clientes.append(novo_cliente)

    return True


def criar_conta(numero_conta, cpf_cliente):

    if numero_conta in contas:
        return False

    contas[numero_conta] = {
        "cpf_cliente": cpf_cliente,
        "saldo": 0.0
    }

    return True


def ver_saldo(numero_conta):

    if numero_conta in contas:
        return contas[numero_conta]

    return None


def depositar(numero_conta, valor):

    if numero_conta not in contas:
        return False

    if valor <= 0:
        return False

    contas[numero_conta]["saldo"] += valor

    return True


def sacar(numero_conta, valor):

    if numero_conta not in contas:
        return False

    if valor <= 0:
        return False

    if valor > contas[numero_conta]["saldo"]:
        return False

    contas[numero_conta]["saldo"] -= valor

    return True