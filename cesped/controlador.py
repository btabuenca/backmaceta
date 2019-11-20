# -*- mode: python; coding: utf-8 -*-
#
###########################################################################
# Filename:    controlador.py
# -------------------------------------------------------------------------
# Project:     C.E.S.P.E.D.
# Author:      José L. Domenech
# Description:
#
#   Controla un sensor, permite la lectura de datos (tras indicarle un
#   método para leerlo y calcularlo) y su envio (indicale una función
#   de endpoint) y su ejecución automatizada cada X ms
#
#
# -------------------------------------------------------------------------
# Historia:
#   + 05/11/2019 - First version
###########################################################################

import cesped.utilidades as utils
import cesped.tarea as tr


class Controlador:
    def __init__(self, nombre,
                 periodo_ms=1000,
                 f_lector=utils.constantemente(True),
                 f_calibrador=utils.identidad,
                 f_envio=utils.constantemente(True)):
        ''' nombre:       string     - nombre de la propiedad que se controla
            f_lector:     f() -> D   - función que obtiene/devuelve un dato
            f_calibrador: f(D) -> X  - función que transforma un dato en otro
            periodo_ms:   int        - periodo cíclico de ejecución de las funciones
            f_envio:      f(X) -> requests.Result'''

        self.nombre       = nombre
        self.f_lector     = f_lector
        self.f_calibrador = f_calibrador
        self.periodo_ms   = periodo_ms
        self.f_envio      = f_envio
        self.task         = tr.Tarea(self, self.enviar_dato, periodo_ms)

    def iniciar(self):
        '''Inicia una tarea que cada `self.periodo_ms' ms recogerá (mediante
        `self.f_lector', trasformado por `self.f_calibrador') y enviará
        un dato (mediante `f_envio')'''

        self.task.start()

    def parar(self):
        "Para la tarea de recogida, transformación y envio"
        self.task.parar()

    def obtener_dato(self):
        """Devuelve un dato leido mediante `self.f_lector' y tratado con
 `f_calibrador'"""

        return self.f_calibrador(self.f_lector())

    def componer_dato(self, dato):
        '''Devuelve un formato listo para ser serializado en formato JSON.

Utiliza un dict, al que añade un campo de timestamp 'ts', y el dato
como campo del nombre del controlador)

        '''

        return {'ts': utils.timestamp(), str(self.nombre): dato}

    def enviar_dato(self):
        '''Obtiene (`obtener_dato') y envía un dato (usando `f_envio').

Es la función que se le pasa a la `cesped.tarea.Tarea' '''

        dato_envio = self.componer_dato(self.obtener_dato())
        return self.f_envio(dato_envio)

    nombre       = "None"
    f_lector     = utils.constantemente(True)
    f_calibrador = utils.identidad
    periodo_ms   = 1000
    f_envio      = utils.constantemente(True)
    task         = None
