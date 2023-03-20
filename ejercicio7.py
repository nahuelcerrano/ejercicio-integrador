class Cuenta:
  def __init__(self, titular, cantidad):
    self.__titular = titular
    self.__cantidad = cantidad

  
  @property
  def titular(self):
    return self.__titular

  
  @titular.setter
  def titular(self, value):
    self.__titular = value

  
  @property
  def cantidad(self):
    return self.__cantidad
  
  
  @cantidad.setter
  def cantidad(self, value):
    self.__cantidad = value

  
  def mostrar(self):
    print(f' Titular: {self.__titular} \n Balance: {self.__cantidad} pesos \n')

  
  def ingresar(self, cantidad):
    self.__cantidad += cantidad
    if cantidad < 0:
      raise ValueError('¡¡El valor no puede ser en negativo!!')
    else:
      print(f' Se agregó {cantidad} pesos al balance de la cuenta \n')

  
  def retirar(self, cantidad):
    self.__cantidad -= cantidad
    print(f' Se retiró {cantidad} pesos al balance de la cuenta \n')


'''
  Operaciones de la cuenta
'''

# Ale = Cuenta('Alejandro', 350000)
# Ale.mostrar()
# Ale.ingresar(25000)
# Ale.mostrar()
# Ale.retirar(2500)
# Ale.mostrar()