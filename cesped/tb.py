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
# -------------------------------------------------------------------------
# Historia:
#   + 30/11/2019 - Primera version
###########################################################################

import cesped.endpoint as cep


TB_API_TELEMETRIA = "/api/v1/_TOKEN_DISPOSITIVO_/telemetry"

TB_API_ALARMAS = "/api/alarm/_TIPO_ALARMA_/_DISPOSITIVO_/"

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


def tb_func_insertar_telemetria(host, puerto, token_dispositivo, protocolo='http'):
    '''Devuelve una función que recibe un dato y lo envía como JSON
(mediante el método POST) al servidor thingsboard indicado por el host
y el puerto, usando la API de telemetría del dispositivo indicado por
el token de dispositivo

    '''
    url_tb_ept = protocolo + '://' + host + ':' + str(puerto) + TB_API_TELEMETRIA.replace('_TOKEN_DISPOSITIVO_', token_dispositivo)
    ep = cep.EndPoint(url_tb_ept)

    return ep.enviar_post_json


def tb_func_consultar_alarmas(host, puerto, token_dispositivo, tipo_alarma, protocolo='http', **params):
    '''Devuelve una función (sin parámetros) que obtiene (mediante método
GET) del servidor thingsboard indicado por el host y el puerto, usando
la API de alarmas del dispositivo indicado por el token de
dispositivo, las alarmas del tipo `tipo_alarma' filtradas por los
parámetros que se le pasan.

    Los parámetros admitidos (los mismos que la API thingsboard) son:
      - searchStatus
      - status
      - limit
      - startTime
      - endTime
      - ascOrder
      - offset
      - fetchOriginator

    '''
    # filtrar los parámetros para incluir sólo los admitidos por la API thingsboard de alarmas
    parametros_ok = {}
    for k in params:
        if k in TB_QUERY_ALARMAS_PARAMS_VALIDOS:
            parametros_ok[k] = params[k]
    query_string = tb_query_alarmas(**parametros_ok)

    url_tb_epa = protocolo + '://' + host + ':' + str(puerto) + TB_API_ALARMAS.replace('_TIPO_ALARMA_', tipo_alarma).replace('_DISPOSITIVO_', token_dispositivo) + query_string

    ep = cep.EndPoint(url_tb_epa)

    return ep.peticion_get
