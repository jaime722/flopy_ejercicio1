# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import flopy

name = "ejercicio1"
h1 = 100
h2 = 90
Nlay = 10
N = 101
L = 400.0
H = 50.0
k = 1.0

sim = flopy.mf6.MFSimulation(
    sim_name=name, exe_name="C:/Users/Lenovo/Desktop/Diapositivas PyS/DIPLOMADO/mf6.2.0/bin", version="mf6", sim_ws="workspace"
) 

#guarda mf6 en la carpeta especfica y guarada los archivos

tdis = flopy.mf6.ModflowTdis(
    sim, pname="tdis", time_units="DAYS", nper=1, perioddata=[(1.0, 1, 1.0)]
)

#Crea el TDISobjeto Flopy
ims = flopy.mf6.ModflowIms(sim, pname="ims", complexity="SIMPLE")

#Crea el IMSobjeto Flopy Package

model_nam_file = "{}.nam".format(name)
gwf = flopy.mf6.ModflowGwf(sim, modelname=name, model_nam_file=model_nam_file)

#Crear el objeto de modelo de flujo de agua subterránea Flopy (gwf)