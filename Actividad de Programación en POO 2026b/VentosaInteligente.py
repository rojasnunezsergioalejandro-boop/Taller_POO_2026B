class VentosaInteligente:

  def __init__(self, codigo_ventosa):
    self.codigo_ventosa = codigo_ventosa
    self.presion_kpa = 0.0
    self.estado_seguro = False

  def calibrar_presion(self, presion):
    self.presion_kpa = presion
    if 60.0 <= self.presion_kpa <= 85.0:
      self.estado_seguro = True
      print(
          f"Ventosa {self.codigo_ventosa}: Presión óptima"
          f" ({self.presion_kpa} kPa). Sujeción segura."
      )
    else:
      self.estado_seguro = False
      print(
          f"Ventosa {self.codigo_ventosa}: ¡PRESIÓN DE RIESGO"
          f" ({self.presion_kpa} kPa)! Activando freno de emergencia."
      )