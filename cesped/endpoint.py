# -*- mode: python; coding: utf-8 -*-
#
###########################################################################
# Ficjero:    endpoint.py
# -------------------------------------------------------------------------
# Proyecto:     C.E.S.P.E.D.
# Autor:      José L. Domenech
# Descripcion:
#
#   Define un EndPoint, como una url y los parámetros necesarios, con
#   el que se puede realizar una petición POST para enviar datos que
#   serán codificados como JSON
#
# Requiere:   requests, json (usado por requests)
# -------------------------------------------------------------------------
# Historia:
#   + 05/11/2019 - Primera version
###########################################################################

import requests
import os

class EndPoint:

    def __init__(self, url, timeout_s=3.0, sesion=None, **kwargs):
        '''url:     string
           timeout_s: tiempo de espera antes de cerrar la conexión (3 s)
           sesion:    objeto de tipo requests.Session ó None (por defecto)
           kwargs:  se usará como dict con keys como strings que se
                    sustituiran por su valor en la url

             e.j.) EndPoint('https://api.com?param=_KEY_',_KEY_='clave')
              sería equivalente a EndPoint('https://api.com?param=clave')
        '''
        self.url       = url
        self.timeout_s = timeout_s
        self.subst     = kwargs
        self.sesion    = sesion

    def enviar_post_json(self, dato):
        '''envia un `dato' que será previamente convertido a formato JSON'''

        mi_url = self.url
        for k in self.subst:
            mi_url = mi_url.replace(k, self.subst[k])

        if self.sesion is None:
            resultado = requests.post(mi_url, timeout=self.timeout_s, json=dato)
        else:
            resultado = self.sesion.post(mi_url, timeout=self.timeout_s, json=dato)

        if (os.getenv('DEBUG_CESPED')):
            print("enviar_post_json: Resultado=" + str(resultado))
            print(resultado.content)
        
        return resultado
    
    def peticion_get(self):
        mi_url = self.url
        for k in self.subst:
            mi_url = mi_url.replace(k, self.subst[k])

        if self.sesion is None:
            resultado = requests.get(mi_url, timeout=self.timeout_s)
        else:
            resultado = self.sesion.get(mi_url, timeout=self.timeout_s)

        if (os.getenv('DEBUG_CESPED')):
            print("peticion_get: Resultado=" + str(resultado))
            print(resultado.json)

        return resultado
