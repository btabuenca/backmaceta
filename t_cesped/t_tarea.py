# -*- mode: python; coding: utf-8 -*-
#
################################################################################
# Filename:    t_tarea.py
#-------------------------------------------------------------------------------
# Project:     C.E.S.P.E.D.
# Author:      José L. Domenech
# Description:
#
#   Test del módulo tarea.py
#
# Dependencias:
#   cesped
#   time
#-------------------------------------------------------------------------------
# Historia:
#   + 05/11/2019 - First version
################################################################################
import time
import cesped

res = 0

def inc_res():
    global res

    res = res+1

def t_tarea():
    global res
    res = 0
    
    # ejecutar la tarea cada 1 s...
    t1=cesped.tarea.Tarea(None,inc_res,1000)
    t1.start()
    # ...durante 3 s
    time.sleep(3)
    t1.stop()
    
    # comprobar el resultado 1*3s + 1 (inicial)
    ESPERADO = 3
    assert res==ESPERADO,"El valor esperado debería ser "+str(ESPERADO)+ ", pero es " + str(res)
    print("Ok: ",__package__)
    
if __name__=='__main__':
    t_tarea()
