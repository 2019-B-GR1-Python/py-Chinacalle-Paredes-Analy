#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
import json
import sys

print('as')
sexo_mascota = ['hembra', 'macho']


personas = []
mascotas = []
path_mascotas ='./mascotas.json'
path_personas = './personas.json'


def abrir_archivo(path):
    try:
        with open(path_personas) as archivo_abierto:
            contenido = json.load(archivo_abierto)
        archivo_abierto.close()
        return contenido
    except Exception as error:
        print(f'error en lectura {error}')

def escribir_archivo(path, contenido):
    try:
        with open(path, 'w') as archivo_escritura:
            json.dump(contenido, archivo_escritura, indent=4)
        archivo_escritura.close()
    except Exception as error:
        print(f'error de escritura {error}')

def inicializar_mascotas_personas():
    personas.append(abrir_archivo(path_personas))
    # mascotas.append(abrir_archivo(path_mascotas))

def listar_personas():
    for persona in personas:
        print(f"Nombre: {persona['nombre']}")
        print(f"Fecha de nacimiento: {persona['fecha']}")
        print(f"Cedula: {persona['cedula']}")
        print(f"Direccion: {persona['direccion']}")
        print('Mascotas: ')
        for mascota in persona['mascotas']:
              print(buscar_mascota_id(mascota))
    return True

inicializar_mascotas_personas()
# print(listar_personas())
# print('ya listo')


def guardar_persona(respuestas):

    respuestas['id'] = len(personas)

    personas.insert(0,respuestas)
    print(personas)
    escribir_archivo(path_personas, personas)

def buscar_persona(respuesta):
    for persona in personas:
        print(persona)
        if (persona['nombre'] == respuesta['nombre']):
            print(f"{persona['nombre']} con {respuesta['nombre']}")
            return persona

def eliminar_persona(respuesta):
    persona = buscar_persona(respuesta)
    if(persona):
        print('eliminar')
        personas.remove(persona)
        escribir_archivo(path_personas, personas)
    else:
        return False

def editar_persona(nombre, persona_editar):
    persona = buscar_persona(nombre)
    if(persona):
        print('editar')
        print(persona)
        for key in persona.keys():
            if persona_editar[key] != '':
                persona[key] = persona_editar[key]
        personas.remove(persona)
        personas.insert(int(persona['id']), persona)
        escribir_archivo(path_personas, personas)
    else:
        print('Persona no encontrada')
        return False


def editar_persona_mascota(persona_editar, id_mascota, editar = True):
    print('editar persona')
    # print(persona)
    if editar:
        personas.remove(persona_editar)
        persona_editar['mascotas'].push(id_mascota)
        personas.insert(int(persona_editar['id']), persona_editar)
        escribir_archivo(path_personas, personas)
    else:
        personas.remove(persona_editar)
        persona_editar['mascotas'].remove(id_mascota)
        personas.insert(int(persona_editar['id']), persona_editar)
        escribir_archivo(path_personas, personas)

def guardar_mascota(respuestas):
    respuestas['id'] = len(mascotas)
    mascotas.insert(0,respuestas)
    escribir_archivo(path_mascotas, mascotas)

def buscar_mascota(respuesta):
    for mascota in mascotas:
        if (mascota['nombre'] == respuesta['nombre']):
            # print(f"{persona['nombre']} con {respuesta['nombre']}")
            return mascota

def buscar_mascota_id(id):
    for mascota in mascotas:
        if (mascota['id'] == id):
            # print(f"{persona['nombre']} con {respuesta['nombre']}")
            return mascota

def eliminar_mascota(respuesta):
    mascota = buscar_mascota(respuesta)
    if(mascota):
        mascotas.remove(mascota)
        escribir_archivo(path_mascotas, mascotas)
    else:
        return False




def mostrar_menu_principal():
    print('Menú de personas')
    opciones = [
            {'name': 'crear persona', 'numero': 1},
            {'name': 'buscar persona', 'numero': 2},
            {'name': 'listar persona', 'numero': 3},
            {'name': 'eliminar persona', 'numero':4},
            {'name': 'editar persona', 'numero':5},
            {'name': 'salir', 'numero': 6},
    ]
    for opcion in opciones:
        print(f"{opcion['numero']}. {opcion['name']}")
    opcion = int(input())
    return opcion

def mostrar_menu_mascotas():
    print('Menú de mascotas')
    opciones = [
            {'name': 'crear mascota', 'numero': 1},
            {'name': 'buscar mascota', 'numero': 2},
            {'name': 'eliminar mascota', 'numero':3},
            {'name': 'editar mascota', 'numero':4},
            {'name': 'volver al menú principal', 'numero': 5},
    ]
    for opcion in opciones:
        print(f"{opcion['numero']}. {opcion['name']}")
    opcion = int(input())
    return opcion

def mostrar_menu_persona():
    persona = {
        'id': 0,
        'nombre': '',
        'cedula': '',
        'fecha': '',
        'direccion': '',
        'mascotas': []
    }
    print('Datos personales')
    opciones = [
            {'name': 'Ingrese su nombre', 'numero': 'nombre'},
            {'name': 'Ingrese su cedula', 'numero': 'cedula'},
            {'name': 'Ingrese su fecha de nacimiento', 'numero': 'fecha'},
            {'name': 'Ingrese su direccion', 'numero':'direccion'},
    ]
    for opcion in opciones:
        print(opcion['name'])
        persona[opcion['numero']] = input()
    return persona

                  
def mostrar_info_mascota():
    mascota = {
        'id': 0,
        'nombre': '',
        'tipo': '',
        'sexo': sexo_mascota[0],
        'edadAproximada': ''
    }
    print('Datos mascotales')
    opciones = [
            {'name': 'Ingrese su nombre', 'numero': 'nombre'},
            {'name': 'Ingrese su tipo (hembra o macho)', 'numero': 'tipo'},
            {'name': 'Ingrese su sexo', 'numero': 'sexo'},
            {'name': 'Ingrese su edad aproximada', 'numero':'edadAproximada'},
    ]
    for opcion in opciones:
        print(opcion['name'])
        mascota[opcion['numero']] = input()
    return mascota

def mostrar_menu_buscar_editar_eliminar():
    print('Cuál es el nombre de la persona')
    nombre = input()
    return nombre

def mostrar_menu_buscar_editar_eliminar_mascota():
    print('Cuál es el nombre de la mascota')
    nombre = input()
    return nombre

def menu_persona():
    persona = mostrar_menu_persona()
    guardar_persona(persona)

def menu_mascota(persona):
    persona = mostrar_info_mascota()
    guardar_mascota(persona)
    editar_persona_mascota(persona, len(mascotas), True)


def menu_buscar_eliminar_editar(opcion):
    nombre = mostrar_menu_buscar_editar_eliminar()
    if opcion == 'eliminar':
        return eliminar_persona({'nombre': nombre})
    elif opcion == 'editar':
        persona = mostrar_menu_persona()
        editar_persona({'nombre': nombre}, persona)
    else:
        return buscar_persona({'nombre': nombre})

def menu_buscar_eliminar_editar_mascota(opcion, persona = {}):
    nombre = mostrar_menu_buscar_editar_eliminar_mascota()
    if opcion == 'eliminar':
        eliminar_mascota({'nombre': nombre})
        editar_persona_mascota(persona, -1, False)
    elif opcion == 'editar':
        mascota = mostrar_info_mascota()
        editar_mascota({'nombre': nombre}, mascota)
    else:
        return buscar_mascota({'nombre': nombre})

def menu_principal():
    opcion = mostrar_menu_principal()
    if opcion == 3:
        listar()
        menu_principal()
    elif opcion == 1:
        menu_persona()
        menu_principal()
    elif opcion == 2:
        persona = menu_buscar_eliminar_editar('buscar')
        menu_mascotas(persona)
    elif opcion == 4:
        menu_buscar_eliminar_editar('eliminar')
        menu_principal()
    elif opcion == 5:
        menu_buscar_eliminar_editar('editar')
        menu_principal()
    elif opcion == 6:
        sys.exit()
    else:
        mostrar_menu_principal()

def menu_mascotas(persona):
    opcion = mostrar_menu_mascotas()

    if opcion == 1:
        menu_mascota(persona)
    elif opcion == 2:
        menu_buscar_eliminar_editar_mascota('buscar')
    elif opcion == 3:
        menu_buscar_eliminar_editar_mascota('eliminar')
    elif opcion == 4:
        menu_buscar_eliminar_editar_mascota('editar', persona)
    else:
        menu_principal()





# print(personas)
""" guardar_persona({
"nombre": "martin",
"cedula": "1716425671",
"fecha": "1996/12/26",
"direccion": ""
}) """
# print(personas)


# In[172]:


""" eliminar_persona({"nombre": "bely"})
print(personas) """


# In[ ]:


def inicio():
    menu_principal()



inicio()
