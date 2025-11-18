#clase integrante
class Integrante: 
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    #editar integrante
    def editar(self, nombre=None, direccion=None, telefono=None):
        if nombre: self.nombre = nombre
        if direccion: self.direccion = direccion
        if telefono: self.telefono = telefono

    #mostrar integrante
    def mostrar(self):
        return f"{self.nombre} - {self.direccion} - {self.telefono}"
