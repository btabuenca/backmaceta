#!/usr/bin/env python3
# -*- mode: python; coding: utf-8 -*-
#
###########################################################################
# Filename:    cesped.sh
#--------------------------------------------------------------------------
# Project:     C.E.S.P.E.D.
# Author:      José L. Domenech
# Description:
#--------------------------------------------------------------------------
# Historia:
#   + 05/11/2019 - First version
################################################################################

# import cesped.configure as conf
import cesped


def start():

    ep = cesped.endpoint.EndPoint("http://teamchibi.com:8080/api/v1/TOKENAQUI/telemetry", TOKENAQUI='uMNyGKqKGu0WdUoqg1TY')
#    ep = cesped.endpoint.EndPoint("http://localhost:5000/api/v1/TOKENAQUI/telemetry", TOKENAQUI='uMNyGKqKGu0WdUoqg1TY')

    
    ctrl = cesped.controlador.Controlador('temperature', f_envio=ep.enviar_post_json, f_lector=cesped.utilidades.constantemente(18.3))

    ctrl.iniciar()


if __name__ == "__main__":

    print("Iniciando")
    start()
