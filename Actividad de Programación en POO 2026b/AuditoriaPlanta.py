class AuditoriaPlanta:

  def __init__(self, nombre_supervisor):
    self.nombre_supervisor = nombre_supervisor
    self.reportes = []

  def registrar_turno(self, turno, eficiencia):
    self.reportes.append({"turno": turno, "eficiencia": eficiencia})

  def generar_evaluacion(self):
    print(f"\n--- AUDITORÍA A CARGO DE: {self.nombre_supervisor} ---")
    for r in self.reportes:
      estado = (
          "Sobresaliente" if r["eficiencia"] >= 90 else "Requiere Ajuste"
      )
      print(
          f"Turno: {r['turno']} | Eficiencia: {r['eficiencia']}% | Calificación:"
          f" {estado}"
      )