# -*- mode: python; coding: utf-8 -*-
#
################################################################################
# Filename:    t_tarea.py
#-------------------------------------------------------------------------------
# Project:     C.E.S.P.E.D.
# Author:      José L. Domenech
# Description:
#
#   Test del módulo endpoint.py
#
# Dependencias:
#   cesped
#   subprocess
#-------------------------------------------------------------------------------
# Historia:
#   + 10/11/2019 - First version
################################################################################
import cesped
import subprocess
import urllib3

def t_endpoint():
    # crear EndPoint
    ep = cesped.endpoint.EndPoint("http://_HOST_:8080/?q=_BUSQUEDA_",_HOST_='localhost',_BUSQUEDA_='cesped')
    # dato a enviar (lo que sea)
    ts = cesped.utilidades.timestamp()
    # iniciar un servidor
    sb=subprocess.Popen(['netcat', '-l', '-p', '8080'])
    # enviar
    try:
        val=ep.enviar_post_json({'timestamp':ts})
    except urllib3.exceptions.ReadTimeoutError:
        pass

    sb.kill()
    res=sb.stdout.raw.readall()
    assert res.find(str.encode(str(ts))), "No se encontró timestamp enviado ("+str(ts)+")"
    print "OK, recibido timestamp"
    
if __name__=='__main__':
    t_endpoint()
