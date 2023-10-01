""" 
Realizar un programa que gestione una Agenda donde ingrese el nombre, teléfono,
correo y dirección del cliente. El programa debe permitir agregar, modificar, eliminar y
consultar un contacto desde una lista. (Se puede utilizar con archivos o bases de datos).
Siempre se debe validar los datos ingresados.
Puede implementar con interfaz gráfica o mediante consola
"""

from classAgenda import Agenda
from classCliente import Cliente
from os import name, system
	
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if name == "posix" or name == "mac" :
        system ("clear")
    elif name == "ce" or name == "nt" or name == "dos":
        system ("cls")


if __name__ == '__main__' :
    borrarPantalla()
    miAgenda = Agenda()

    miCliente = Cliente('Mario Choaib', 542914393785, 'mchoaib@gmail.com', 'Alberti 292')
    miAgenda.agregarCliente(miCliente)
    miCliente2 = Cliente('Alejandra Fernandez', 542915013319, 'alechoaib@gmail.com', 'Alberti 292')
    miAgenda.agregarCliente(miCliente2)
    miAgenda.mostrarAgenda()
    
    
