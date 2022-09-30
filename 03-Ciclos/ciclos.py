cont = 100
while cont >= 1:
  print("contador con while: ", cont)
  cont -= 1  
a = 5 
b = 5
c = 6 
d = 7
res = (a > 5 and c < 6)
# a > 5 = false, c < 6 = false (false,false = False por Tablas de verdad) 
print(res)

#and -> true, false
print("t AND t", True and True)
print("t AND f", True and False)
print("f AND t", False and True)
print("f AND f", False and False)

print("t OR t", True or True)
print("t OR f", True or False)
print("f OR t", False or True)
print("f OR f", False or False)

g = 10
h = 11
j = 12

if g >= 9 and h <= 11:
  print("el resultado fue true")
elif j == 12:
  print("el primer if no fue true y salto a este")


lista = [1, 2, 3, 4, "a", 5, "b"]
for valorActual in lista:
  print("for de lista", valorActual)
for num in range(5, 11):
  print("range 5-10", num)
lista2 = ["hola", "pepe", "adios", "comer"]
if "pepe" in lista2:
  print("encontre a pepe")
if "adioses" not in lista2:
  print("no encontre la palabra adioses")
lista3 = [2, 4, 1, 10, 3, 7, 6, 1]
listOrder = sorted(lista3)
print(listOrder)
listInvOrder = sorted(lista3, reverse=True)
print(listInvOrder)