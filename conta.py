from cliente import Cliente

class ContaBancaria:
    def __init__(self, numero_conta: str, titular: Cliente, saldo_inicial: float = 0.0):
        self.numero_conta = numero_conta
        self.titular = titular
        self._saldo = saldo_inicial  # Atributo protegido

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            return True
        print("Valor de depósito inválido.")
        return False

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("Valor de saque inválido.")
            return False
        if valor > self._saldo:
            print(f"Saldo insuficiente. Saldo atual: R$ {self._saldo:.2f}")
            return False
        
        self._saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        return True

    def consultar_saldo(self) -> float:
        return self._saldo

    def exibir_extrato(self):
        print("\n--- EXTRATO DA CONTA ---")
        print(f"Número da Conta: {self.numero_conta}")
        print(self.titular.exibir_dados())
        print(f"Saldo Atual: R$ {self._saldo:.2f}")
        print("------------------------")