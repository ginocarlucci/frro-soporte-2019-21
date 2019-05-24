# Implementar la funcion listar_pesos, que devuelva el historial de pesos para una persona dada.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).

# Debe devolver:
# - Lista de (fecha, peso), donde fecha esta representado por el siguiente formato: AAAA-MM-DD.
#   Ejemplo:
#   [
#       ('2018-01-01', 80),
#       ('2018-02-01', 85),
#       ('2018-03-01', 87),
#       ('2018-04-01', 84),
#       ('2018-05-01', 82),
#   ]
# - False en caso de no cumplir con alguna validacion.

import datetime
import sqlite3

<<<<<<< HEAD:practico_03A/ejercicio_08.py
from ejercicio_02 import agregar_persona
from ejercicio_06 import reset_tabla
from ejercicio_07 import agregar_peso
from ejercicio_04 import buscar_persona
from ORM import Base,engine,Persona,session,PersonaPeso


def listar_pesos(id_persona):
    if (buscar_persona(id_persona)):
        pesos = session.query(PersonaPeso).filter(PersonaPeso.idPersona == id_persona).all()
        lista = []
        for peso in pesos:
            tup = (peso.fecha.strftime('%Y-%m-%d'),peso.peso)
            lista.append(tup)
        return lista
    else:
        return False;
=======
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_06 import reset_tabla
from practico_03.ejercicio_07 import agregar_peso
from practico_03.ejercicio_04 import buscar_persona

def listar_pesos(id_persona):
    persona = buscar_persona(id_persona)
    if(persona):
        db = sqlite3.connect('mibase')
        cursor = db.cursor()
        cSQL='SELECT Fecha,peso from PersonaPeso where idPersona = '+str(id_persona)
        cursor.execute(cSQL)
        lista = cursor.fetchall()
        lista2 = []
        for row in lista:
            lista2.append(row)
        return lista2
    else:
        return False
>>>>>>> master:practico_03/ejercicio_08.py


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01 00:00:00', 80),
        ('2018-06-01 00:00:00', 85)
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) == False


if __name__ == '__main__':
    pruebas()