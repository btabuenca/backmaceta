#!/usr/bin/env python3
# -*- mode: python; coding: utf-8 -*-
#
###########################################################################
# Filename:    cesped.sh
# -------------------------------------------------------------------------
# Project:     C.E.S.P.E.D.
# Author:      José L. Domenech
# Description:
# -------------------------------------------------------------------------
# Historia:
#   + 05/11/2019 - First version
###########################################################################

import cesped


def configurar():
    '''devuelve una lista de `cesped.Controlador' '''
    ep = cesped.endpoint.EndPoint(
        cesped.configure.ENDPOINT_THINGSBOARD,
        TOKENAQUI=cesped.configure.ENDPOINT_THINGSBOARD_TOKEN)

    ctrl = cesped.controlador.Controlador(
        'temperature',
        f_envio=ep.enviar_post_json,
        f_lector=cesped.utilidades.constantemente(20.1))

    return [ctrl]


def iniciar(lst_ctrl):
    '''inicia todos los controladores incluidos en la lista, haciendo que
su procesos se ejecuten en threads diferentes.

Devuelve la misma lista con los controladores ya iniciados

    '''
    for ctrl in lst_ctrl:
        ctrl.iniciar()

    return lst_ctrl


def parar(lst_ctrl):
    '''para las tareas de los controladores de la lista.

Devuelve la misma lista con los controladores ya parados'''
    for ctrl in lst_ctrl:
        ctrl.parar()


def prueba():
    print("Iniciando controladores:")
    lst_ctr = configurar()
    for c in lst_ctr:
        print(c.nombre)
    iniciar(lst_ctr)

    
if __name__ == "__main__":
    prueba()
