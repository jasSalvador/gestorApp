from integrantes import Integrante
from cuotas import Cuota
from gastos import Gasto

class GestorPrincipal:
    def __init__(self):
        self.integrantes = []
        self.cuotas = []
        self.gastos = []

    #integrantes
    def agregar_integrante(self, nombre, direccion, telefono):
        integrante = Integrante(nombre, direccion, telefono)
        self.integrantes.append(integrante)
        return integrante

    def eliminar_integrante(self, nombre):
        for i in self.integrantes:
            if i.nombre.lower() == nombre.lower():
                self.integrantes.remove(i)
                return True
        return False


    #cuotas
    def registrar_cuota(self, integrante, mes, fecha, monto):
        cuota = Cuota(integrante, mes, fecha, monto)
        self.cuotas.append(cuota)
        return cuota

    def eliminar_cuota(self, nombre_integrante, mes):
        for i in self.cuotas:
            if i.integrante.nombre.lower() == nombre_integrante.lower() and i.mes.lower() == mes.lower():
                self.cuotas.remove(i)
                return True
        return False


    #gastos
    def registrar_gasto(self, nombre, fecha):
        gasto = Gasto(nombre, fecha)
        self.gastos.append(gasto)
        return gasto
    
    def eliminar_gasto(self, nombre, fecha):
        for i in self.gastos:
            if i.nombre.lower() == nombre.lower() and i.fecha.lower() == fecha.lower():
                self.gastos.remove(i)
                return True
        return False