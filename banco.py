from cliente import Cliente
from conta import ContaBancaria

class Banco:
    def __init__(self, nome: str):
        self.nome = nome
        self.contas = {}

    def criar_conta(self, nome_cliente: str, cpf: str, numero_conta: str) -> ContaBancaria:
        if numero_conta in self.contas:
            print("Erro: Já existe uma conta cadastrada com esse número.")
            return None
        
        novo_cliente = Cliente(nome=nome_cliente, cpf=cpf)
        nova_conta = ContaBancaria(numero_conta=numero_conta, titular=novo_cliente)
        self.contas[numero_conta] = nova_conta
        print(f"Conta {numero_conta} criada para o cliente {nome_cliente}!")
        return nova_conta

    def buscar_conta(self, numero_conta: str) -> ContaBancaria:
        return self.contas.get(numero_conta, None)