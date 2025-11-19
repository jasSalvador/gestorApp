#clase cuota
class Cuota:
    def __init__(self, integrante, mes, fecha, monto):
        self.integrante = integrante
        self.mes = mes
        self.fecha = fecha
        self.monto = monto

    #mostrar pago cuota
    def mostrar(self):
        return f"{self.integrante.nombre} - {self.mes} - {self.fecha} - {self.monto}"



