from banco import Banco

def menu():
    meu_banco = Banco("Banco Central POO")
    
    while True:
        print("\n=== SISTEMA BANCÁRIO ===")
        print("1. Criar Nova Conta")
        print("2. Realizar Depósito")
        print("3. Realizar Saque")
        print("4. Consultar Extrato")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            num_conta = input("Digite o número da nova conta: ")
            meu_banco.criar_conta(nome, cpf, num_conta)

        elif opcao == "2":
            num_conta = input("Digite o número da conta: ")
            conta = meu_banco.buscar_conta(num_conta)
            if conta:
                valor = float(input("Digite o valor para depósito: R$ "))
                conta.depositar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "3":
            num_conta = input("Digite o número da conta: ")
            conta = meu_banco.buscar_conta(num_conta)
            if conta:
                valor = float(input("Digite o valor para saque: R$ "))
                conta.sacar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            num_conta = input("Digite o número da conta: ")
            conta = meu_banco.buscar_conta(num_conta)
            if conta:
                conta.exibir_extrato()
            else:
                print("Conta não encontrada.")

        elif opcao == "5":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()