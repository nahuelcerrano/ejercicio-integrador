from ejercicio7 import *

class CuentaJoven(Cuenta):
  def __init__(self, titular, cantidad, edad, bonificacion):
    super().__init__(titular, cantidad)
    self.__cantidad = cantidad
    self.__bonificacion = bonificacion
    self.__edad = edad

  @property
  def cantidad(self):
    return self.__cantidad
    
  @cantidad.setter
  def cantidad(self, cantidad):
      self.__cantidad = cantidad

  @property
  def bonificacion(self):
    return self.__bonificacion
  

  @bonificacion.setter
  def bonificacion(self, value):
    self.__bonificacion = value

  @property
  def edad(self):
    return self.__edad
  
  @edad.setter
  def edad(self, value):
    self.__edad = value

  def es_titular_valido(self):
    if self.__edad >= 18 and self.__edad <= 25:
      return True
    else:
      return False

  def retirar(self, cantidad):
    if not (Ale.es_titular_valido()):
      print(' !No puede retirar en una CUENTA JOVEN! \n')
    else:
      self.__cantidad -= cantidad
      print(f' Se retiró {cantidad} pesos al balance de la cuenta \n')


  def mostrar(self):
    print(f' Cuenta Joven \n Bonificación: {self.__bonificacion}% \n Balance de Cuenta: {self.__cantidad} pesos \n')


'''
  Operaciones de la cuenta
'''

Ale = CuentaJoven('Alejandro', 350000, 18, 25)
Ale.mostrar()
Ale.retirar(25000)
Ale.mostrar()