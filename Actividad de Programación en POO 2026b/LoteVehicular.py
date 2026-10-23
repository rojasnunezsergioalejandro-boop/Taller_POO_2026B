class LoteVehicular:

  def __init__(self, numero_lote, modelo_auto):
    self.numero_lote = numero_lote
    self.modelo_auto = modelo_auto
    self.chasis_pendientes = []

  def agregar_chasis(self, id_chasis):
    self.chasis_pendientes.append(id_chasis)
    print(f"Chasis {id_chasis} registrado para el lote {self.numero_lote}.")

  def procesar_lote(self):
    print(
        f"\n--- PROCESANDO LOTE {self.numero_lote} ({self.modelo_auto}) ---"
    )
    for chasis in self.chasis_pendientes:
      print(
          f"-> Ensamblando parabrisas en chasis serial: {chasis} -> [COMPLETADO]"
      )