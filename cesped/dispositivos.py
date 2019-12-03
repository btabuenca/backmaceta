# -*- mode: python; coding: utf-8 -*-
#
###########################################################################
# Fichero:    dispositivos.py
# -------------------------------------------------------------------------
# Proyecto:     C.E.S.P.E.D.
# Autor:      José L. Domenech
# Descripcion:
#
#   Proporciona funciones para la lectura de dispositivos:
#    + SHT85 - lectura del sensor SHT85 (conexión I2C)
#
# Requiere:
#   mraa
# -------------------------------------------------------------------------
# Historia:
#   + 02/12/2019 - Primera version
###########################################################################

import mraa
import time


def SHT85(bus):
    SHT85_DIRECCION = 0x44
    SHT85_CMD_LECTURA_LENTA = bytearray(b'\x24\x16')
    SHT85_TIEMPO_LECTURA_MAX = 0.045  # segundos

    # inicializar I2C
    i2c = mraa.I2c(bus)

    for i in range(1, 5):
        print('.', end='')
        time.sleep(1)
    print()
        
    # iniciar el proceso de lectura
    # enviar comando de escritura
    error = i2c.address(SHT85_DIRECCION)
    # TODO: comprobar error
    print('A_ERROR: ' + str(error))
    ack = i2c.write(SHT85_CMD_LECTURA_LENTA)
    time.sleep(SHT85_TIEMPO_LECTURA_MAX)

    print('ACK:     ' + str(ack))

    error = i2c.address(SHT85_DIRECCION)
    # TODO: comprobar error
    print('A_ERROR: ' + str(error))
    res = i2c.read(0)

    print('READ(0): ' + str(res))

    time.sleep(SHT85_TIEMPO_LECTURA_MAX)
    res = i2c.read(6)

    print('READ(6): ' + str(res))

    time.sleep(SHT85_TIEMPO_LECTURA_MAX)

    return res
