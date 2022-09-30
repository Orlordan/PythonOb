def leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Es Bisiesto")
      else: print("No es Bisiesto")
    else: print("No es Bisiesto")
  else: print("No es Bisiesto")
leap(1700)



# Es secuncial los prints
def mifuncion():
  print("Nombre")
print("Antes")
mifuncion()
print("Despues")

#Funcion con parametros
def funConParametros(name):
  print("Hola", name)
funConParametros("Oriordan")

def operaciones(a, b):
  def add(a, b):
    print(a + b)
  def substract(a, b):
    print(a - b)
  add(a, b)
  substract(a, b)
operaciones(10, 5)