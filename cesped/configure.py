# -*- mode: python; coding: utf-8 -*-
#
################################################################################
# Filename:    configure.py
#-------------------------------------------------------------------------------
# Project:     C.E.S.P.E.D.
# Author:      José L. Domenech
# Description:
#
#   Configuración que se utilizará en el script de lanzamiento para
#   añadir los controladores que se van a utilizar
#
#-------------------------------------------------------------------------------
# Historia:
#   + 05/11/2019 - First version
################################################################################
import cesped.utilidades as utils

# EndPoint del servidor Thingsboard
ENDPOINT_THINGSBOARD=""

# Token necesario para la autentificación en el servidor Thingsboard
ENDPOINT_THINGSBOARD_TOKEN=""

# Lista de tuplas: (clase sensor, nombre, {parametros})
LISTA_CONTROLADORES = [('Controlador','temp-1',{'f_lector':utils.identidad})]


