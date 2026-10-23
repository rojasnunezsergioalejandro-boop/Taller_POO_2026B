num_estudiantes = int(input("Ingrese el número de estudiantes del curso: "))
suma_promedios_curso = 0

for i in range(1, num_estudiantes + 1):
  print(f"\nEstudiante {i}")
  suma_notas = 0

  for j in range(1, 5):
    suma_notas += float(input(f"Ingrese la calificación {j}: "))

  promedio = suma_notas / 4
  suma_promedios_curso += promedio

  print(f"Promedio: {promedio:.2f} -> Categoría: ", end="")
  if promedio < 3.0:
    print("Reprobado")
  elif 3.0 <= promedio < 4.0:
    print("Regular")
  elif 4.0 <= promedio <= 4.5:
    print("Bueno")
  else:
    print("Excelente")

promedio_general = suma_promedios_curso / num_estudiantes
print("\n=== RESUMEN ESTADÍSTICO DEL CURSO ===")
print(f"Promedio general del curso: {promedio_general:.2f}")