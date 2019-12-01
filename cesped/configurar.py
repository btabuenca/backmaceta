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

# Lista de tuplas: (clase sensor, nombre, {parametros})
#LISTA_CONTROLADORES = [('Controlador', 'temperatura',{'f_lector':utils.identidad})]


def lista_controladores():
    '''Devuelve una lista con los controladores que se utilizarán en el sistema.'''

    # EndPoint del servidor Thingsboard
    ENDPOINT_THINGSBOARD = "http://teamchibi.com:8080"

    # Token necesario para la autentificación en el servidor Thingsboard
    THINGSBOARD_TOKEN = 'uMNyGKqKGu0WdUoqg1TY'

    return None
