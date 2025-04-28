'''
class Animal:
    def hablar(self):
        print('Este animal hace sonido')
        
class Perro(Animal):
    def hablar(self):
        print('Guau!')

class Gato(Animal):
    def hablar(self):
        print('Miau!')
        
        
perro = Perro()
gato = Gato()

perro.hablar()
gato.hablar()

class Vehiculo:
    def __init__(self,marca):
        self.marca = marca       
    def moverse(self):
        print(f'El auto de marca {self.marca} se esta moviendo')
class Auto(Vehiculo):
    def moverse(self):
        print(f'El auto {self.marca} va por la ruta')

class Bicicleta(Vehiculo):
    def moverse(self):
        print(f'La bici {self.marca} esta pedaleando')
        
v = Vehiculo('Generica')
a = Auto ('Toyota')
b= Bicicleta ('Oxford')

v.moverse()
a.moverse()
b.moverse()
'''