""" 
Realizar un programa que gestione una Agenda donde ingrese el nombre, teléfono,
correo y dirección del cliente. El programa debe permitir agregar, modificar, eliminar y
consultar un contacto desde una lista. (Se puede utilizar con archivos o bases de datos).
Siempre se debe validar los datos ingresados.
Puede implementar con interfaz gráfica o mediante consola
"""

class Cliente:
    __nombre = str
    __telefono = int
    __correo = str
    __direccion = str

    def __init__(self, nombre, telefono, correo, direccion):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__correo = correo
        self.__direccion = direccion
        
    def setNombre(self, name):
        self.__nombre = name
    
    def getNombre(self):
        return self.__nombre
    
    def setTelefono(self, phone):
        self.__telefono = phone

    def getTelefono(self):
        return self.__telefono
    
    def setCorreo(self, correo):
        self.__correo = correo

    def getCorreo(self):
        return self.__correo
    
    def setDireccion(self, direccion):
        self.__direccion = direccion
    
    def getDireccion(self):
        return self.__direccion
    
    def __str__(self):
        return "Nombre: {}\nTeléfono: {}\nCorreo: {}\nDirección: {}\n".format(self.__nombre, self.__telefono, self.__correo, self.__direccion)