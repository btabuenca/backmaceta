# -*- mode: python; coding: utf-8 -*-
#
################################################################################
# Fichero:    setup.py
#-------------------------------------------------------------------------------
# Proyecto:     C.E.S.P.E.D.
# Autor:      José L. Domenech
# Descripcion:
#  Entrada principal
#   - configurar el sistema
#-------------------------------------------------------------------------------
# Historia:
#   + 05/11/2019 - Primera version
################################################################################

from setuptools import setup

setup(
    name='cesped',
    version='0.1.0',    
    description='''Control y Exposición de un Sistema de Pradera Ecológica Durable
(C.E.S.P.E.D.)

Proyecto de Macetero del Grupo 05 de la asignatura Sistemas Basados en
Computador de la Escuela Técnica Superior de Ingenieros de Sistemas
Informáticos de la Universidad Politécnica de Madrid''',
    url='https://github.com/jldm.upm/cesped',
    author='José L. Domenech',
    author_email='jldm.upm@google.es',
    packages=['cesped','cesped_tests'],
    install_requires=['json',
                      'requests',                     
                      ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
