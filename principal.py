from integrantes import Integrante
from cuotas import Cuota
from gastos import Gasto

class GestorPrincipal:
    def __init__(self):
        self.integrantes = []
        self.cuotas = []
        self.gastos = []


    def agregar_integrante(self, nombre, direccion, telefono):
        integrante = Integrante(nombre, direccion, telefono)
        self.integrantes.append(integrante)
        return integrante


    def registrar_cuota(self, integrante, mes, fecha, monto):
        cuota = Cuota(integrante, mes, fecha, monto)
        self.cuotas.append(cuota)
        return cuota


    def registrar_gasto(self, nombre, fecha):
        gasto = Gasto(nombre, fecha)
        self.gastos.append(gasto)
        return gasto
    

