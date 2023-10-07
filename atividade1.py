class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor

    def ver_saldo(self):
        print(f"Saldo atual da conta de {self.titular}: R${self.saldo:.2f}")


# Criando um objeto da classe ContaBancaria
conta1 = ContaBancaria("João")

# Realizando alguns depósitos e saques
conta1.depositar(1000)
conta1.sacar(500)
conta1.depositar(200)
conta1.sacar(800)

# Verificando o saldo
conta1.ver_saldo()