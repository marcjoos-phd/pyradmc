#!/usr/import/epd/bin/python
# -*- coding: utf-8 -*-
import numpy as np

class unit:
    """RADMC-3D CLASS: Unit
    contains name & value of the unit in cgs"""
    def __init__(self):
        self.name = ''
        self.val  = 0.

# Constants
cc = 2.99792458000e10          # [cm/s], light speed
mp = 2.33*1.67299999999999e-24 # proton mass, with mu = 2.33

# Units
cm = unit()
cm.name = 'cm'
cm.val  = 1.0              # [cm]

AU = unit()
AU.name = 'AU'
AU.val  = 1.49597870700e13 # [cm] Astronomical Unit according to the IAU (2009)

pc = unit()
pc.name = 'pc'
pc.val  = 3.08567758147e18 # [cm], parsec = (1 AU)/np.tan(np.pi/180/3600)

Jy = unit()
Jy.name = 'Jy'
Jy.val  = 1.e-23           # [Jy] = 1e-23 [erg/s/cm^2/Hz], Jansky
