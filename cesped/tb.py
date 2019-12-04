# -*- mode: python; coding: utf-8 -*-
#
###########################################################################
# Fichero:    tb.py
# -------------------------------------------------------------------------
# Proyecto:     C.E.S.P.E.D.
# Autor:      José L. Domenech
# Descripcion:
#
#   Funcionalidad para acceder a los servicios que proporciona un servidor
#   thingsboard.
#
# Requiere:
#  requests: para crear un objeto de tipo sesion configurado según parámetros
# -------------------------------------------------------------------------
# Historia:
#   + 30/11/2019 - Primera version
###########################################################################

import cesped.endpoint as cep
import requests

TB_API_TELEMETRIA = "/api/v1/_TOKEN_DISPOSITIVO_/telemetry"

TB_API_ALARMAS = "/api/alarm/_DEVICE_TYPE_/_DEVICE_ID_/"

# parámetros válidos:
TB_QUERY_ALARMAS_PARAMS_VALIDOS = ["searchStatus", "status", "limit",
                                   "startTime", "endTime", "ascOrder",
                                   "offset", "fetchOriginator"]


def tb_query_alarmas(**args):
    '''genera la query de la petición a la api de alarmas de
thingsboard'''
    res = '?'  # una query url comienza por '?'
    
    for k in args:
        res += str(k) + '=' + str(args[k]) + '&'

    return res[:-1]  # el útimo será: ? ó & (en cualquier caso se puede eliminar)


def tb_func_insertar_telemetria(host, puerto, token_dispositivo, protocolo='http', auth=None):
    '''Devuelve una función que recibe un dato y lo envía como JSON
(mediante el método POST) al servidor thingsboard indicado por el host
y el puerto, usando la API de telemetría del dispositivo indicado por
el token de dispositivo

El token de autorización se puede obtener con: curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"username":"tenant@thingsboard.org", "password":"tenant"}' 'http://THINGSBOARD_URL/api/auth/login'
    '''
    sesion = requests.Session() if auth is not None else None
    if sesion is not None:
        sesion.headers.update({'X-Authorization': "Bearer " + auth})
    url_tb_ept = protocolo + '://' + host + ':' + str(puerto) + TB_API_TELEMETRIA.replace('_TOKEN_DISPOSITIVO_', token_dispositivo)
    ep = cep.EndPoint(url_tb_ept, sesion=sesion)

    return ep.enviar_post_json


def tb_func_consultar_alarmas(host, puerto, device_type, device_id, protocolo='http', auth='', limit=10, **params):
    '''Devuelve una función (sin parámetros) que obtiene (mediante método
GET) del servidor thingsboard indicado por el host y el puerto, usando
la API de alarmas del dispositivo indicado por el identificado y el tipo de
dispositivo, las alarmas del tipo `tipo_alarma' filtradas por los
parámetros que se le pasan.

    Los parámetros admitidos (los mismos que la API thingsboard) son:
      - searchStatus
      - status
      - limit [OBLIGATORIO] (por eso lo incluyo como keyword, por defecto=10)
      - startTime
      - endTime
      - ascOrder
      - offset
      - fetchOriginator

El token de autorización se puede obtener con: curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"username":"tenant@thingsboard.org", "password":"tenant"}' 'http://THINGSBOARD_URL/api/auth/login'

    '''
    # filtrar los parámetros para incluir sólo los admitidos por la API thingsboard de alarmas
    parametros_ok = {}
    for k in params:
        if k in TB_QUERY_ALARMAS_PARAMS_VALIDOS:
            parametros_ok[k] = params[k]
    parametros_ok['limit']=limit
    query_string = tb_query_alarmas(**parametros_ok)

    sesion = requests.Session() if auth is not None else None
    if sesion is not None:
        sesion.headers.update({'X-Authorization': "Bearer " + auth})
    
    url_tb_epa = protocolo + '://' + host + ':' + str(puerto) + TB_API_ALARMAS.replace('_DEVICE_ID_', device_id).replace('_DEVICE_TYPE_', device_type) + query_string

    ep = cep.EndPoint(url_tb_epa, sesion=sesion)

    return ep.peticion_get
