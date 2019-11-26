#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
import json
import sys

print('as')
sexo_mascota = ['hembra', 'macho']
persona = {
    'id': 0,
    'nombre': '',
    'cedula': '',
    'fecha': '',
    'direccion': '',
    'mascotas': []
}
mascota = {
    'id': 0,
    'nombre': '',
    'tipo': '',
    'sexo': sexo_mascota[0],
    'edadAproximada': ''
}
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


def guardar_mascota(respuestas):
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


preguntas_menu_principal = [
    {
        'type': 'list',
        'name': 'opcion',
        'message': 'Menú persona',
        'choices': [
            {'name': 'crear persona'},
            {'name': 'buscar persona'},
            {'name': 'listar persona'},
            {'name': 'eliminar persona'},
            {'name': 'salir'},
        ],
        'filter': lambda val: val.split()[0]
     }
]

preguntas_persona = [
    {
        'type': 'input',
        'name': 'nombre',
        'message': 'Cual es su nombre',
#         'validate': PhoneNumberValidator
    },
    {
        'type': 'input',
        'name': 'cedula',
        'message': 'Cual es su cedula',
#         'validate': PhoneNumberValidator
    },
    {
        'type': 'input',
        'name': 'fecha',
        'message': 'Cual es su fecha de nacimiento aaaa/mm/dd',
#         'validate': PhoneNumberValidator
    },
    {
        'type': 'input',
        'name': 'direccion',
        'message': 'Cual es su dirección',
#         'validate': PhoneNumberValidator
    },
]

pregunta_editar_eliminar_buscar = [
    {
        'type': 'input',
        'name': 'nombre',
        'message': 'Cuál es el nombre de la persona?'
    }
]

pregunta_confirmar = [
    {
        'type': 'confirm',
        'name': 'confirma',
        'message': 'Confirma para confirmar?'
    }
]


def imprimir_pregunta(pregunta):
    return prompt(pregunta)
                  
def respuesta_menu_princ(opcion = 'listar'):
    if opcion == 'listar':
        listar()
        break
    elif opcion == 'crear':
        imprimir_pregunta(preguntas_persona)
        break
    elif opcion == 'buscar':
        imprimir_pregunta(pregunta_editar_eliminar_buscar)
        break
    elif opcion == 'eliminar':
        imprimir_pregunta(pregunta_editar_eliminar_buscar)
        break
    else:
        sys.exit()
"""
    def opcion_seleccionada():
        opciones = {
            'listar': listar(),
            'crear': imprimir(preguntas_persona),
            'buscar': imprimir(pregunta_editar_eliminar_buscar),
            'eliminar': imprimir(pregunta_editar_eliminar_buscar)
        }
        print(opciones['crear'])
        return opciones.get(opcion, "respuesta invalida")
    
    return  opcion_seleccionada()
"""

def respuesta_menu_principal(opcion,respuesta):
    def opcion_seleccionada():
        opciones = {
            'crear': guardar_persona(respuesta),
            'buscar': buscar_persona(respuesta),
            'listar': listar_personas(),
            'eliminar': eliminar_persona(respuesta)
        }
        return opciones[opcion]
    return opcion_seleccionada()


def respuesta_submenu_persona(opcion):
    def opcion_seleccionada():
        opciones = {
            'editar': '',
            'menu-mascota': menu_mascota()
        }
        return opciones[opcion]
    return opcion_seleccionada()

def respuesta_menu_mascota(opcion, respuesta):
    def opcion_seleccionada():
        opciones = {
            'crear': guardar_mascota(respuesta),
            'editar': '',
            'buscar': buscar_mascota(respuesta),
            'eliminar': eliminar_mascota(respuesta)
        }
        return opciones[opcion]
    return opcion_seleccionada()


                  



def auxilio(opcion):
    respuesta_promp_menu = respuesta_menu_princ(opcion)



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

#    print(listar_personas())
    respuesta_prompt_menu_princ = imprimir_pregunta(preguntas_menu_principal)
    print(respuesta_prompt_menu_princ)
    opcion = (respuesta_prompt_menu_princ['opcion'])
    print("tipoOpc", type(opcion))
    

    respuesta_menu_princ(opcion)



inicio()
