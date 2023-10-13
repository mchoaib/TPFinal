#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:48:43 2023

@author: mchoaib
"""

from csv import DictReader 

with open('agenda.csv') as file:

    csv_reader = DictReader(file, delimiter=',')
    dictUsuario = {}
    
    for row in csv_reader:
        name = row['nombre']
        phone = row['telefono']
        email = row['correo']
        address = row['direccion']
        
        
        
        usuario = {}
        usuario['nombre'] = name
        usuario['telefono'] = phone
        usuario['correo'] = email
        usuario['direccion'] = address
        
        dictUsuario[f'{name}'] = usuario
    
    for contacto in dictUsuario :
        name = dictUsuario[contacto].get('nombre')
        print(f'Apellido y Nombre: {name}')
        
        fono = dictUsuario[contacto].get('telefono')
        print(f'Telefono: {fono}')
        
        email = dictUsuario[contacto].get('correo')
        print(f'Correo: {email}')
        
        address = dictUsuario[contacto].get('direccion')
        print(f'Direccion: {address}')
        
        print('')
        
    print (len(dictUsuario))
