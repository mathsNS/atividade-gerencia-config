class ContaCorrente:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso."
        else:
            return "Valor inválido para depósito."

    def sacar(self, valor):
        if valor <= 0:
            return "Valor inválido para saque."
        elif valor > self.saldo:
            return "Saldo insuficiente."
        else:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso."

    def exibir_saldo(self):
        return f"Titular: {self.titular} \nSaldo atual: R${self.saldo:.2f}"