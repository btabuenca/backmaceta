# -*- mode: python; coding: utf-8 -*-
#
###########################################################################
# Filename:    configure.py
# -------------------------------------------------------------------------
# Project:     C.E.S.P.E.D.
# Author:      José L. Domenech
# Description:
#
#   Configuración que se utilizará en el script de lanzamiento para
#   añadir los controladores que se van a utilizar
#
# -------------------------------------------------------------------------
# Historia:
#   + 05/11/2019 - First version
###########################################################################

# EndPoint del servidor Thingsboard
ENDPOINT_THINGSBOARD = "http://teamchibi.com:8080/api/v1/TOKENAQUI/telemetry"

# Token necesario para la autentificación en el servidor Thingsboard
ENDPOINT_THINGSBOARD_TOKEN = 'uMNyGKqKGu0WdUoqg1TY'

# Lista de tuplas: (clase sensor, nombre, {parametros})
# LISTA_CONTROLADORES = [('Controlador', 'temperature',{'f_lector':utils.identidad})]

