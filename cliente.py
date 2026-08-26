class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    def exibir_dados(self):
        return f"Cliente: {self.nome} | CPF: {self.cpf}"