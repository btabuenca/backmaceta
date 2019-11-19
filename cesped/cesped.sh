#!/usr/bin/env python3
# -*- mode: python; coding: utf-8 -*-
#
################################################################################
# Filename:    cesped.sh
#-------------------------------------------------------------------------------
# Project:     C.E.S.P.E.D.
# Author:      José L. Domenech
# Description:
#-------------------------------------------------------------------------------
# Historia:
#   + 05/11/2019 - First version
################################################################################

import cesped.configure as conf

controladores=[]

def instanciarControlador(control_conf):
   """ """
   module_=__import__('controlador')
   class_=getattr(module_, control_conf[0])
   instance = class_(*control_conf[1],**control_conf[2])

   return instance

def start():
    controladores=[instanciarControlador(ctrl) for ctrl in conf.LISTA_SENSORES]
    for c in controladores:
        c.iniciar()

def stop():
    for c in controladores:
        c.parar()
