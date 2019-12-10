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

import cesped.utilidades as util
import cesped.controlador as ctrl
import cesped.tb as tb
import cesped.dispositivos as disp

# EndPoint del servidor Thingsboard
ENDPOINT_THINGSBOARD_HOST = "teamchibi.com"
ENDPOINT_THINGSBOARD_PORT = 8080
# Token necesario para la autentificación en el servidor Thingsboard
THINGSBOARD_DEVICE_TOKEN = 'uMNyGKqKGu0WdUoqg1TY'


def lista_controladores():
    '''Devuelve una lista con los controladores que se utilizarán en el sistema.'''
    
    ep_tc = tb.tb_func_insertar_telemetria(ENDPOINT_THINGSBOARD_HOST, ENDPOINT_THINGSBOARD_PORT, THINGSBOARD_DEVICE_TOKEN)

    ctrl_LDR     = ctrl.Controlador('luz', 1000, disp.leerLDR, f_envio=ep_tc)
    ctrl_goteo   = ctrl.Controlador('goteo', 1001, disp.leerGoteo, f_envio=ep_tc)
    ctrl_peso    = ctrl.Controlador('peso', 1002, disp.leerPeso, f_envio=ep_tc)
    ctrl_valvula = ctrl.Controlador('valvula', 2 * 60 * 1000, disp.encenderValvula, f_envio=util.identidad)

    lst_ctrl = [ctrl_LDR, ctrl_goteo, ctrl_valvula, ctrl_peso]
    
    return lst_ctrl
