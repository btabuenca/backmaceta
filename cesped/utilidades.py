# -*- mode: python; coding: utf-8 -*-
#
###########################################################################
# Fichero:    utilidades.py
# -------------------------------------------------------------------------
# Proyecto:     C.E.S.P.E.D.
# Autor:      José L. Domenech
# Descripcion:
#
#   Varias utilidades
#
# Requiere:    random, time
# -------------------------------------------------------------------------
# Historia:
#   + 05/11/2019 - Primera version
###########################################################################

import random
import time

FLOAT_MS_IN_SEG = 1000.0


def identidad(arg):
    "Función que devuelve sus argumentos sin modificar"
    return arg


class __Constante:
    '''Clase que sirve de closure del valor pasado para la función
`constantemente' '''
    def __init__(self, val):
        '''Constructor'''
        self.valor = val
    
    def obtener_valor(self):
        '''Devuelve el valor pasado en el constructor'''
        return self.valor
            
    valor = None

    
def constantemente(arg):
    '''Función que devuelve una función que siempre devuelve el mismo
valor (el indicado en el parámetro)'''
    c = __Constante(arg)

    return c.obtener_valor


def timestamp():
    '''funcion que devuelve un timestamp en ms. (si esta disponible por el
sistema, si no s.), desde el epoch: time.gmtime(0)'''
    return int(time.time() * FLOAT_MS_IN_SEG)


# Inicializar módulo
random.seed(timestamp())
