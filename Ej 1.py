class alumnos(object):

    def __init__(self, nombre = None , apellido = None):
        self.listaNotas =[]
        self.nombre = nombre
        self.apellido = apellido
    def setNombre(self, nomb):
        self.nombre = nomb.title()
    def getNombre(self):
        return self.nombre


a = alumnos(nombre = 'pepe', apellido = 'perez')
print(a.getNombre())
n = input("Ingrese nombre: ")
a.setNombre(n)
print(a.getNombre())
