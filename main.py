import os

from banco import Banco
from cliente import Cliente
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

banco = Banco("NexusBank")


def encontrar_conta(numero):
    for conta in banco.contas:
        if conta.numero_conta == numero:
            return conta
    return None


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== NEXUSBANK ===")
    print("1 - Criar conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Exibir saldo")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("\n-- Criar Conta --")
        nome = input("Nome do titular: ")
        cpf = input("CPF: ")
        numero = input("Número da conta: ")
        tipo = input("Tipo (1 - Corrente / 2 - Poupança): ")

        cliente = Cliente(nome, cpf, numero)
        print(banco.adicionar_cliente(cliente))

        if tipo == "1":
            conta = ContaCorrente(nome, numero)
        else:
            conta = ContaPoupanca(nome, numero)

        print(banco.adicionar_conta(conta))
        input("\nPressione Enter para continuar...")

    elif opcao == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Encerrando sistema...")
        break