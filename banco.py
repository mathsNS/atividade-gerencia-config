class Banco:

    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente '{cliente.nome}' cadastrado.")

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        print(f"Conta {conta.numero_conta} adicionada.")

    def listar_clientes(self):
        print(f"\n-- Clientes do {self.nome} --")
        for cliente in self.clientes:
            print(f"  {cliente.nome} | CPF: {cliente.cpf} | Conta: {cliente.numero_conta}")

    def listar_contas(self):
        print(f"\n-- Contas do {self.nome} --")
        for conta in self.contas:
            if hasattr(conta, 'mostrar_saldo'):
                conta.mostrar_saldo()
            elif hasattr(conta, 'exibir_saldo'):
                conta.exibir_saldo()
