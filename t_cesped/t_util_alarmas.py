# -*- mode: python; coding: utf-8 -*-
#
################################################################################
# Filename:    t_tarea.py
#-------------------------------------------------------------------------------
# Project:     C.E.S.P.E.D.
# Author:      José L. Domenech
# Description:
#
#   Test del módulo util_alarmas.py
#
# Dependencias:
#   cesped
#   subprocess
#-------------------------------------------------------------------------------
# Historia:
#   + 29/11/2019 - First version
################################################################################

def prueba_gta():
    device = "7a0dc1a0-f5ad-11e9-aeab-298698774def"
    ep1 = ep.EndPoint(
        "http://teamchibi.com:9000" + API_ALARMAS + query_alarmas(limit=123),
        _TIPO_ALARMA_="General Alarm",
        _DEVICE_=device)
    print(ep1.peticion_get())


if __name__ == "__main__":
    prueba_gta()
