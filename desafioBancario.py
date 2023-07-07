class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.saques = 0

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if self.saques < 3 and valor <= 500:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saques += 1
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Limite de saques excedido ou valor de saque inválido.")
        self.extrato()

    def extrato(self):
        print(f"Saldo atual: R${self.saldo:.2f}")


# Exemplo de uso:
conta = ContaBancaria()  # Criando uma conta com saldo inicial zero

valor_deposito = float(input("Digite o valor a depositar: "))
conta.depositar(valor_deposito)

for _ in range(3):
    valor_saque = float(input("Digite o valor a sacar: "))
    conta.sacar(valor_saque)