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
#      - SHT85_ID - leer ID del dispositivo
#      - SHT85_t_d - leer temperatura y humedad
#
# Requiere:
#   mraa
# -------------------------------------------------------------------------
# Historia:
#   + 02/12/2019 - Primera version
###########################################################################

#import mraa
import time

SHT85_DIRECCION = 0x44

SHT85_CMD_ID_DISPOSITIVO = bytearray(b'\x36\x82')
SHT85_CMD_LECTURA_LENTA = bytearray(b'\x24\x16')

SHT85_TIEMPO_ACK = 0.0015  # segundos = 1.5 ms
SHT85_TIEMPO_ID_DISPOSITVO = 0.0005  # segundos = 0.5 ms
SHT85_TIEMPO_LECTURA_PETICION = 0.001  # segundos = 1 ms
SHT85_TIEMPO_LECTURA_TH = 0.0155  # segundos = 15.5 ms


def SHT85_ID(bus):
    # inicializar I2C
    i2c = mraa.I2c(bus)

    # for i in range(1, 5):
    #     print('.', end='')
    #     time.sleep(1)
    # print()

    # ============================================
    # lectura del ID del dispositivo
    error = i2c.address(SHT85_DIRECCION)
    # TODO: comprobar error
    print('A_ERROR: ' + str(error))
    ack = i2c.write(SHT85_CMD_ID_DISPOSITIVO)
    time.sleep(SHT85_TIEMPO_ID_DISPOSITVO)
    print('ACK:     ' + str(ack))

    error = i2c.address(SHT85_DIRECCION)
    # TODO: comprobar error
    print('A_ERROR: ' + str(error))
    res = i2c.read(6)
    time.sleep(SHT85_TIEMPO_ID_DISPOSITVO)
    print('READ(6): ' + str(res))

    return res


def SHT85_t_d(bus):
    # inicializar I2C
    i2c = mraa.I2c(bus)

    # for i in range(1, 5):
    #     print('.', end='')
    #     time.sleep(1)
    # print()

    # ============================================
    # lectura single-shot de humedad y temperatura

    # iniciar el proceso de lectura
    # enviar comando de escritura
    error = i2c.address(SHT85_DIRECCION)
    # TODO: comprobar error
    print('A_ERROR: ' + str(error))
    ack = i2c.write(SHT85_CMD_LECTURA_LENTA)
    time.sleep(SHT85_TIEMPO_LECTURA_PETICION)

    print('ACK:     ' + str(ack))

    error = i2c.address(SHT85_DIRECCION)
    # TODO: comprobar error
    print('A_ERROR: ' + str(error))
    res = i2c.read(0)
    time.sleep(SHT85_TIEMPO_LECTURA_TH)
    print('READ(0): ' + str(res))
    res = i2c.read(6)
    time.sleep(SHT85_TIEMPO_LECTURA_TH)
    print('READ(6): ' + str(res))

    return res
