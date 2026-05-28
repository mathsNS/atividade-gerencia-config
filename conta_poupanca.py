class ContaPoupanca:

    def __init__(self, titular, numero_conta, saldo=0):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado."

    def sacar(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente."
        elif valor > 0:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado."

    def aplicar_rendimento(self, taxa=0.05):
        self.saldo *= (1 + taxa)
        return f"Rendimento de {taxa*100:.0f}% aplicado. Novo saldo: R${self.saldo:.2f}"

    def mostrar_saldo(self):
        return f"[Poupança] {self.titular} | Conta: {self.numero_conta} | Saldo: R${self.saldo:.2f}"
