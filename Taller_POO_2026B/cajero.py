saldo = float(input("Ingrese el saldo inicial de la cuenta: "))
opcion = 0

while opcion != 4:
  print("\n=== MENÚ CAJERO AUTOMÁTICO ===")
  print("1. Consultar saldo")
  print("2. Retirar dinero")
  print("3. Depositar dinero")
  print("4. Salir")
  opcion = int(input("Seleccione una opción: "))

  if opcion == 1:
    print(f"Su saldo actual es: ${saldo}")
  elif opcion == 2:
    retiro = float(input("Ingrese la cantidad a retirar: "))
    if 0 < retiro <= saldo:
      saldo -= retiro
      print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
    else:
      print("Monto inválido o fondos insuficientes.")
  elif opcion == 3:
    deposito = float(input("Ingrese la cantidad a depositar: "))
    if deposito > 0:
      saldo += deposito
      print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
    else:
      print("Monto inválido.")
  elif opcion == 4:
    print(f"Saliendo del sistema. Saldo final: ${saldo}")
  else:
    print("Opción inválida, intente de nuevo.")