class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    def mostrar_saldo(self):
        print(f"\ntitular: {self.titular}")
        print(f"saldo actual: ${self.saldo:.2f}")
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"deposito exitoso de ${monto:.2f}")
        else:
            print("el monto a depositar debe ser mayor que cero.")
    def retirar(self, monto):
        if monto <= 0:
            print("el monto debe ser mayor que cero.")
        elif monto > self.saldo:
            print("fondos insuficientes.")
        else:
            self.saldo -= monto
            print(f"retiro exitoso de ${monto:.2f}")
cuenta1 = CuentaBancaria("genis Maria", 1000)
cuenta1.mostrar_saldo()
cuenta1.depositar(500)
cuenta1.retirar(300)
cuenta1.retirar(2000)
cuenta1.mostrar_saldo()