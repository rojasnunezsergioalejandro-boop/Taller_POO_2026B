class BrazoRobotico:

  def __init__(self, id_brazo, modelo):
    self.id_brazo = id_brazo
    self.modelo = modelo
    self.energia = 100.0
    self.piezas_instaladas = 0

  def ejecutar_ensamblaje(self, pieza):
    if self.energia >= 15:
      self.piezas_instaladas += 1
      self.energia -= 15
      print(
          f"[{self.modelo}] Brazo {self.id_brazo}: Parabrisas '{pieza}'"
          " instalado con éxito."
      )
    else:
      print(
          f"[{self.modelo}] ¡Alerta! Energía baja ({self.energia}%). Recargue"
          " el sistema."
      )

  def mostrar_estado(self):
    print(
        f"\n--- ESTADO DEL BRAZO {self.id_brazo} ---"
        f"\nModelo: {self.modelo}\nEnergía Restante: {self.energia}%"
        f"\nPiezas Totales Instaladas: {self.piezas_instaladas}"
    )