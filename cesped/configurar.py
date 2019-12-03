# -*- mode: python; coding: utf-8 -*-
#
###########################################################################
# Fichero:    configurar.py
# -------------------------------------------------------------------------
# Proyecto:     C.E.S.P.E.D.
# Autor:      José L. Domenech
# Descripcion:
#
#   Configuración que se utilizará en el script de lanzamiento para
#   añadir los controladores que se van a utilizar
#
# -------------------------------------------------------------------------
# Historia:
#   + 05/11/2019 - Primera version
###########################################################################

import random
import cesped.controlador as ctrl
import cesped.tb as tb
# Lista de tuplas: (clase sensor, nombre, {parametros})
#LISTA_CONTROLADORES = [('Controlador', 'temperatura',{'f_lector':utils.identidad})]

# EndPoint del servidor Thingsboard
ENDPOINT_THINGSBOARD_HOST = "teamchibi.com"
ENDPOINT_THINGSBOARD_PORT = 8080
# Token necesario para la autentificación en el servidor Thingsboard
THINGSBOARD_DEVICE_TOKEN = 'uMNyGKqKGu0WdUoqg1TY'

def devuelve_aleatorio_1():
    r = (random.randint(20*100, 50*100)) / 100.0
    print (str(r))
    return r


def devuelve_aleatorio_2():
    r = (random.randint(500, 520))
    print (str(r))
    return r


def lista_controladores():
    '''Devuelve una lista con los controladores que se utilizarán en el sistema.'''
    
    ep_tc = tb.tb_func_insertar_telemetria(ENDPOINT_THINGSBOARD_HOST, ENDPOINT_THINGSBOARD_PORT, THINGSBOARD_DEVICE_TOKEN)
    ctrl_temperature_rnd = ctrl.Controlador('temperature', 3000, devuelve_aleatorio_1, f_envio=ep_tc)
    ctrl_luz_rnd = ctrl.Controlador('luz', 5000, devuelve_aleatorio_2, f_envio=ep_tc)
    
    lst_ctrl = [ctrl_temperature_rnd, ctrl_luz_rnd]

    return lst_ctrl
