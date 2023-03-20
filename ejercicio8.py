from ejercicio7 import *

class CuentaJoven(Cuenta):
  def __init__(self, titular, cantidad, bonificacion):
    super().__init__(titular, cantidad)
    self.__bonificacion = bonificacion

  
  @property
  def bonificacion(self):
    return self.__bonificacion
  

  @bonificacion.setter
  def bonificacion(self, value):
    self.__bonificacion = value


  def mostrar(self):
    print(f' Cuenta Joven \n Bonificación: {self.__bonificacion}% \n')


# Ale = CuentaJoven('Alejandro', 350000, 10)
# Ale.mostrar()
# Ale.valido(17)