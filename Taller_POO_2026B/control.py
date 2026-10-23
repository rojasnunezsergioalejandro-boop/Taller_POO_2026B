cantidad_sensores = int(
    input("Ingrese la cantidad de sensores de temperatura instalados: ")
)

frio = 0
optimo = 0
critico = 0

for i in range(1, cantidad_sensores + 1):
  temperatura = float(
      input(f"Ingrese la temperatura registrada por el sensor {i}: ")
  )

  if temperatura < 18:
    frio += 1
    print("-> Estado: Frío")
  elif 18 <= temperatura <= 25:
    optimo += 1
    print("-> Estado: Óptimo")
  else:
    critico += 1
    print(
        "-> ¡ALERTA! Supera los 25°C. Aire acondicionado activo. Estado: Crítico"
    )

print("\n--- RESUMEN FINAL ---")
print(f"Habitaciones con Frío (< 18°C): {frio}")
print(f"Habitaciones Óptimas (18°C - 25°C): {optimo}")
print(f"Habitaciones Críticas (> 25°C): {critico}")