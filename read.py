#!/usr/import/epd/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pylab as pl
from utils import utils
from constants import *

class image:
    """RADMC-3D CLASS: Image
    """
    def __init__(self):
        self.radian  = 0
        self.nx      = 0
        self.ny      = 0
        self.nf      = 0
        self.sp_x    = 0
        self.sp_y    = 0
        self.Lambda  = 0
        self.image   = np.array([])
        self.flux    = 0.
        self.size_x  = 0.
        self.size_y  = 0.
        self.x       = np.array([])
        self.y       = np.array([])

class spectrum:
    """RADMC-3D CLASS: Spectrum
    """
    def __init__(self):
        self.nf       = 0
        self.Lambda   = np.array([])
        self.spectrum = np.array([])
        self.freq     = np.array([])
    
def readimage(file = "image.out"):
    """RADMC-3D READING FUNCTION: Read an image
    Usage:
          im = readimage(args)
    Args:
         - file: file to read. Default: image.out
    Return:
         im: an image object"""
    im         = image()
    data       = open(file)
    iformat    = int(data.readline())
    im.radian  = not(iformat)
    ndim       = data.readline()
    j          = 0
    nx         = np.zeros(2)
    for i in ndim.split():
        nx[j]  = int(i)
        j     += 1
    im.nx      = nx[0]
    im.ny      = nx[1]
    im.nf      = int(data.readline())
    sizepix    = data.readline()
    j          = 0
    sp         = np.zeros(2)
    for i in sizepix.split():
        sp[j]  = float(i)
        j     += 1
    im.sp_x    = sp[0]
    im.sp_y    = sp[1]
    im.Lambda  = float(data.readline())
    data.close()
    col        = np.loadtxt(file, usecols=(0,))
    im.image   = col[5:]
    im.image   = im.image.reshape((im.nx,im.ny))
    flux       = utils.compute_flux(im.image,im.nx,im.ny)
    if(not(im.radian)):
        im.flux = flux/pc.val**2
    im.size_x  = im.sp_x*im.nx
    im.size_y  = im.sp_y*im.ny
    im.x       = np.linspace(-im.size_x/2,im.size_x/2,im.nx)
    im.y       = np.linspace(-im.size_y/2,im.size_y/2,im.ny)
    return(im)

def readspectrum(file = "spectrum.out"):
    """RADMC-3D READING FUNCTION: Read an spectrum
    Usage:
          sp = readspectrum(args)
    Args:
         - file: file to read. Default: spectrum.out
    Return:
         sp: a spectrum object"""
    sp          = spectrum()
    header      = open(file)
    iformat     = int(header.readline())
    sp.nf       = int(header.readline())
    header.close()
    sp.Lambda   = np.loadtxt(file, usecols=(0,), skiprows=2)
    sp.spectrum = np.loadtxt(file, usecols=(1,), skiprows=2)
    sp.freq     = 1e4*cc/sp.Lambda
    return(sp)
