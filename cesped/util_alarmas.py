# -*- mode: python; coding: utf-8 -*-
#
###########################################################################
# Filename:    util_alarmas.py
# -------------------------------------------------------------------------
# Project:     C.E.S.P.E.D.
# Author:      José L. Domenech
# Description:
#
# -------------------------------------------------------------------------
# Historia:
#   + 27/11/2019 - First version
###########################################################################

import cesped.endpoint as ep
#import urllib

API_ALARMAS="/api/alarm/_TIPO_ALARMA_/_DEVICE_/"

def query_alarmas(**args):
    res = '?'
    for k in args:
        res += str(k) + '=' + str(args[k]) + '&'
    return res[:-1] # el útimo será: ? (y se puede eliminar) ó &

def prueba_gta():
    device = "7a0dc1a0-f5ad-11e9-aeab-298698774def"
    ep1 = ep.EndPoint(
        "http://teamchibi.com:9000" + API_ALARMAS + query_alarmas(limit=123),
        _TIPO_ALARMA_="General Alarm",
        _DEVICE_=device)
    print(ep1.peticion_get())


if __name__ == "__main__":
    prueba_gta()
