class Persona:
  def __init__(self, nombre, edad, dni):
    self.__nombre = nombre
    self.__edad = edad
    self.__dni = dni

  @property
  def nombre(self):
    return self.__nombre
  
  @nombre.setter
  def nombre (self, value):
    self.__nombre = value

  @property
  def edad(self):
    return self.__edad
  
  @edad.setter
  def edad (self, value):
    self.__edad = value

  @property
  def dni(self):
    return self.__dni

  @dni.setter
  def dni (self, value):
    self.__dni = value

  def mostrar(self):
    print(f' Nombre:{self.__nombre} \n Edad:{self.__edad} \n DNI:{self.__dni} \n')

  def es_mayor_de_edad(self):
    if self.__edad >= 18:
      return True
    else:
      return False

Ale = Persona('Alejandro', 38, 29950188)
Ale.mostrar()