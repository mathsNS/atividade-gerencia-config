import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== NEXUSBANK ===")
    print("1 - Criar conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Exibir saldo")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Encerrando sistema...")
        break