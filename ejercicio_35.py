# 35.- Crea la clase UsuarioBanco
#     Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
#     Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
#     Código a seguir:
#         Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
#         Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
#         Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
#         Implementar agregar_dinero para aumentar el saldo del usuario.
#     Caso de uso:
#         a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#         b. Agregar 20 unidades al saldo de Bob.
#         c. Transferir 80 unidades de Bob a Alicia.
#         d. Retirar 50 unidades del saldo de Alicia.

class UsuarioBanco():
    def __init__(self, nombre, saldo, tiene_cuenta):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta = tiene_cuenta
    
    def retirar_dinero(self, cantidad):
        if self.saldo - cantidad < 0:
            raise Exception(f"No hay saldo suficiente en la cuenta de {self.nombre}.")
        else:
            self.saldo += cantidad
            print(f"Se han añadido {cantidad}€ a la cuenta de {self.nombre}.")

    def transferir_dinero(self, usuario_banco, cantidad):
        if usuario_banco.saldo - cantidad < 0:
            raise Exception(f"No hay saldo suficiente en la cuenta de {usuario_banco.nombre}.")
        else:
            self.saldo += cantidad
            usuario_banco.saldo -= cantidad
            print(f"Se han transferido {cantidad}€ de la cuenta de {usuario_banco.nombre} a la cuenta de {self.nombre}.")

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"Se han añadido {cantidad}€ a la cuenta de {self.nombre}")

alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

bob.agregar_dinero(20)

try:
    alicia.transferir_dinero(bob, 80)
except Exception as e:
    print(e)

try:
    alicia.retirar_dinero(50)
except Exception as e:
    print(e)