

#Programacion orientada a objetos.
'''
class personaje:
    def __init__(self, ataque, vida):
        self.ataque = ataque
        self.vida = vida

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f'Hola, soy {self.nombre} y tengo {self.edad} años.')
        
p1 = Persona('Antonela', 34)
p1.saludar()
'''
class CuentaBancaria:
    def __init__(self,saldo):
        self.__saldo = saldo
    
    def mostrar_saldo(self):
        print(f'Saldo actual: ${self.__saldo}')
        
    def despositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            
mi_cuenta = CuentaBancaria(1000)

mi_cuenta.mostrar_saldo()

mi_cuenta.despositar(500)

mi_cuenta.mostrar_saldo()