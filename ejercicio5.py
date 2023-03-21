def get_int():
  try:
    number = int(input('Ingrese un número entero: '))
    print(f'{number} es un número entero.')
  except ValueError:
    print('¡El número ingresado no es un entero!')

get_int()