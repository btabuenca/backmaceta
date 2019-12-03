#!/usr/bin/env python3
# -*- mode: python; coding: utf-8 -*-
#
###########################################################################
# Filename:    cesped.py
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
    return cesped.configurar.lista_controladores()

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
