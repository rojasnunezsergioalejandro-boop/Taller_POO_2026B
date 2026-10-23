n = int(
    input("Ingrese la cantidad de productos en inventario a registrar: ")
)

for i in range(1, n + 1):
  print(f"\nProducto {i}")
  codigo = input("Código: ")
  nombre = input("Nombre: ")
  cantidad = int(input("Cantidad disponible: "))

  if cantidad < 10:
    print("-> Estado: URGENTE (Menor a 10 unidades)")
  elif 10 <= cantidad <= 50:
    print("-> Estado: REVISIÓN (Entre 10 y 50 unidades)")
  else:
    print("-> Estado: SUFICIENTE (Mayor a 50 unidades)")