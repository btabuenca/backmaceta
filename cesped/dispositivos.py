
#!/usr/bin/python

import mraa as m
import spidev
import time
 
def leerAdc(adcnum):
    #Inicializar SPI
    spi = spidev.SpiDev()
    spi.open(1, 0)
    # leer datos , 4 canales del MCP3004
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data    

def leerGoteo():
    canal_gotas = 1
    valor_gotas=leerAdc(canal_gotas)
    
    if valor_gotas < 300:
        apagarValvula()
    
    return valor_gotas

def leerLDR():
    canal_ldr = 0
    valor_ldr=leerAdc(canal_ldr)
    encenderLed(valor_ldr)
    return valor_ldr

def encenderLed(valor):
    #variables rgb e inicializacion de pines RGB
    rojo=40        #corresponde al pin de la placa
    verde=36    #corresponde al pin de la placa
    azul=38        #corresponde al pin de la placa
    pin_r=m.Gpio(rojo)
    pin_b=m.Gpio(azul)
    pin_r.dir(m.DIR_OUT)
    pin_b.dir(m.DIR_OUT)
    if valor > 800:
        pin_r.write(1)
        pin_b.write(1)
    else:
        pin_r.write(0)
        pin_b.write(0)

def encenderValvula():
    pin_rele = m.Gpio(37)
    pin_rele.write(1)

    
def apagarValvula():
    pin_rele = m.Gpio(37)
    pin_rele.write(0)


def leerHumedad1()
    canal_humedad_suelo_1=2
    valor_humedad1=leerAdc(canal_humedad_suelo_1)
    return valor_humedad1

def leerHumedad2()
    canal_humedad_suelo_2=3
    valor_humedad2=leerAdc(canal_humedad_suelo_2)
    return valor_humedad2

def leerPeso()
    canal_peso=4
    valor_peso=leerAdc(canal_peso)
    valor_kilos=(valor_peso*18.41)/1000
    return valor_kilos
