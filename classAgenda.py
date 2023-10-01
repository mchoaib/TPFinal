""" 
Realizar un programa que gestione una Agenda donde ingrese el nombre, teléfono,
correo y dirección del Cliente. El programa debe permitir agregar, modificar, eliminar y
consultar un contacto desde una lista. (Se puede utilizar con archivos o bases de datos).
Siempre se debe validar los datos ingresados.
Puede implementar con interfaz gráfica o mediante consola
"""
from classCliente import Cliente

class Agenda:
    # __Agenda = list
    cli = Cliente

    def __init__(self):
        self.__Agenda = []
    
    def agregarCliente(self, Cliente):
        self.__Agenda.append(Cliente)
    
    def modificar(self, Cliente):
        self.__Agenda.remove(Cliente)
        self.__Agenda.append(Cliente)
    
    def eliminar(self, Cliente):
        self.__Agenda.remove(Cliente)
    
    def consultar(self, nombre):
        for Cliente in self.__Agenda:
            if Cliente.getNombre() == nombre:
                print(Cliente)
    
    def listar(self):
        for Cliente in self.__Agenda:
            print(Cliente)
    
    def __str__(self):
        cadena = ""
        for Cliente in self.__Agenda:
            cadena += str(Cliente)
        return cadena
    
    def mostrarAgenda(self) :
        for cli in self.__Agenda:
            print(cli.__str__())
    
    
    
