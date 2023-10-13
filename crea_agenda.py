#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 08:52:02 2023

@author: mchoaib

version: Diccionario
"""
from csv import DictWriter

"""
agenda = [
    { 
         'nombre': 'Choaib, Mario', 
         'telefono': '+542914392333',
         'correo': 'mchoaib@gmail.com',  
         'direccion': 'Manuel Alberti 292, Bahia Blanca' 
    } ,
    { 
         'nombre': 'Fernandez, Alejandra', 
         'telefono': '+542915013319',
         'correo': 'alechoaib@gmail.com',  
         'direccion': 'Manuel Alberti 292, Bahia Blanca' 
    } ,
    { 
         'nombre': 'Choaib, Alfredo', 
         'telefono': '+3459578688',
         'correo': 'achoaib@gmail.com',  
         'direccion': '134, Sacted Rd., Aberdeen, UK' 
    } ,
]
"""
agenda = []
finalizar = False

while not finalizar :
    dictContacto= {}
    
    name = input('Ingrese apellido y nombre: ')
    dictContacto['nombre'] = name
    
    phone = input('Ingrese numero de telefono: ')
    dictContacto['telefono'] = phone
    
    email = input('Ingrese el correo electronico: ')
    dictContacto['correo'] = email
    
    address = input('Ingrese la direccion: ')
    dictContacto['direccion'] = address
    
    agenda.append(dictContacto)
    
    resp = input('Desea ingresar otro contacto? (S/N) ')
    
    
    
    if resp != 'S' and resp != 's' :
        finalizar = True

columns = ['nombre', 'telefono', 'correo', 'direccion']

with open('agenda.csv', mode='w') as file:
    writer = DictWriter(file, delimiter=',', fieldnames=columns )
    writer.writeheader()

    for contacto in agenda:
        writer.writerow(contacto)