#clase gasto
class Gasto:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha
        self.detalles = []
        self.gasto_total = 0

    def agregar_detalle(self, item, monto):
        self.detalles.append({"item": item, "monto": monto})
        self.gasto_total += monto

    def mostrar(self):
        detalles_str = ", ".join([f"{d['item']}: ${d['monto']}" for d in self.detalles])
        return f"{self.nombre} ({self.fecha}) - Total: ${self.gasto_total} - {detalles_str}"
    
    