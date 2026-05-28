class ContaPoupanca:

    def __init__(self, titular, numero_conta, saldo=0):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > 0:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")

    def mostrar_saldo(self):
        print(f"[Poupança] {self.titular} | Conta: {self.numero_conta} | Saldo: R${self.saldo:.2f}")
