from flask import Flask, render_template, request, redirect

import AuraBank

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/cadastrar-cliente", methods=["GET", "POST"])
def cadastrar_cliente ():

    if request.method == "POST":
        
        nome = request.form["nome"]
        cpf = request.form["cpf"]
        telefone = request.form["telefone"]
        email = request.form["email"]

        AuraBank.cadastrar_cliente(
            nome,
            cpf,
            telefone,
            email
        )

        return redirect("/")

    return render_template("cadastrar_cliente.html")


@app.route ("/criar-conta", methods=["GET", "POST"])
def criar_conta ():

    mensagem = None

    if request.method == "POST":

        numero_conta = request.form["numero_conta"]
        cpf_cliente = request.form["cpf_cliente"]

        sucesso = AuraBank.criar_conta(
            numero_conta,
            cpf_cliente
        )

        if sucesso:
            mensagem = "Conta criada com sucesso!"
        else:
            mensagem = "Já existe uma conta com esse número."

    return render_template(
        "criar_conta.html",
        mensagem=mensagem
    )

@app.route("/saldo", methods=["GET", "POST"])
def saldo():

    conta = None
    mensagem = None

    if request.method == "POST":

        numero_conta = request.form["numero_conta"]
        
        conta = AuraBank.ver_saldo(numero_conta)

        if conta is None:
            mensagem = "Conta não encontrada."

    return render_template(
        "saldo.html",
        conta=conta,
        mensagem=mensagem
    )

@app.route("/depositar", methods=["GET", "POST"])
def depositar():

    mensagem = None

    if request.method == "POST":

        numero_conta = request.form["numero_conta"]

        valor = float(request.form["valor"])

        sucesso = AuraBank.depositar(
            numero_conta,
            valor
        )

        if sucesso:
            mensagem = "Depósito realizado com sucesso!"

        else:
            mensagem = "Não foi posível realizar o depósito."

    return render_template(
        "depositar.html",
        mensagem=mensagem
    )


@app.route("/sacar", methods=["GET", "POST"])
def sacar():

    mensagem = None

    if request.method == "POST":

        numero_conta = request.form["numero_conta"]

        valor = float(request.form["valor"])

        sucesso = AuraBank.sacar(
            numero_conta,
            valor
        )

        if sucesso:
            mensagem = "Saque realizado com sucesso!"

        else:
            mensagem = "não foi possível realizar o saque."

    return render_template(
        "sacar.html",
        mensagem=mensagem
    )

@app.route("/contas")
def listar_contas():

    return render_template(
        "contas.html",
        contas = AuraBank.contas
    )

if __name__ == "__main__":
    app.run (debug = True)