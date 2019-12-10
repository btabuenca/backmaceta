# -*- mode: python; coding: utf-8 -*-
#
###########################################################################
# Filename:    cesped.sh
# -------------------------------------------------------------------------
# Project:     C.E.S.P.E.D.
# Author:      José L. Domenech
# Description:
#
#   Ejecutar el programa de demo `valvula.py'
#
# -------------------------------------------------------------------------
# Historia:
#   + 04/12/2019 - First version
###########################################################################
import mraa as m
import spidev
import time

def encenderValvula():
    pin_rele = m.Gpio(37)
    pin_rele.write(1)

encenderValvula()
