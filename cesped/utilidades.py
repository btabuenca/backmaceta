# -*- mode: python; coding: utf-8 -*-
#
################################################################################
# Filename:    utilidades.py
#-------------------------------------------------------------------------------
# Project:     C.E.S.P.E.D.
# Author:      José L. Domenech
# Description:
#   Varias utilidades
#-------------------------------------------------------------------------------
# Historia:
#   + 05/11/2019 - First version
################################################################################

import random
import time

FLOAT_MS_IN_SEG=1000.0

def identidad(*args):
    "funcion que devuelve sus argumentos sin modificar"
    return args

def timestamp():
    '''funcion que devuelve un timestamp en ms. (si esta disponible por el
sistema, si no s.), desde el epoch: 
 >>> time.gmtime(0) '''
    return int(time.time() * FLOAT_MS_IN_SEG)

# Inicializar módulo
random.seed(timestamp())
