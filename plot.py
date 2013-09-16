#!/usr/import/epd/bin/python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import pylab as pl
from constants import *

bold  = "\033[1m"
reset = "\033[0;0m"

def plotimage(im, unit=cm, contour=False, log=False, min=None, max=None, save=False):
    """RADMC-3D PLOTTING FUNCTION: Plot an image read with readimage()
    Usage:
          plotimage(args)
    Args:
         - im:      the image to be plotted
         - unit:    unit of the axes.                    Default: cm
         - contour: if True, make a contour plot.        Default: False
         - log:     if True, plot the log of the image.  Default: False
         - min:     min value for the intensity to plot. Default: None
         - max:     max value for the intensity to plot. Default: None
         - save:    if True, save png & eps image.       Default: False"""
    scale = 1./unit.val
    sx    = im.size_x/2.
    sy    = im.size_y/2.
    ext   = np.array([-sx,sx,-sy,sy])*scale
    if(log):
        image  = np.log10(im.image)
        clabel = r'log(I) (erg cm$^{-2}$ s$^{-1}$ Hz$^{-1}$ ster$^{-1}$)'
    else:
        image  = im.image
        clabel = r'I (erg cm$^{-2}$ s$^{-1}$ Hz$^{-1}$ ster$^{-1}$)'
    xlabel = 'X [' + unit.name + ']'
    ylabel = 'Y [' + unit.name + ']'
    pl.figure(figsize=(8,6))
    pl.xlabel(xlabel)
    pl.ylabel(ylabel)
    pl.imshow(image.transpose(), origin='lower', extent=ext, vmin = min, vmax = max)
    cbar = pl.colorbar()
    cbar.set_label(clabel)
    if(contour):
        pl.contour(image.transpose(), origin='lower', extent=ext, colors='k')
    if(save):
        for format in ("png", "eps"):
            namefig = "image." + format
            print(bold + "Save figure: " + reset + namefig)
            pl.savefig(namefig)
        pl.close()
    else:
        pl.show()

def plotspectrum(sp, rpc=1., kind='nuLnu', ymin=None, save=False):
    """RADMC-3D PLOTTING FUNCTION: Plot a spectrum read with readspectrum()
    Usage:
          plotspectrum(args)
    Args:
         - sp:   the spectrum to be plotted
         - rpc:  distance of observer in parsec. Default: 1
         - kind: type of SED: nuLnu, nuFnu, Fnu. Default: 'nuLnu'
         - ymin: minimum value for the spectrum. Default: None
         - save: if True, save png & eps image.  Default: False"""
    if(kind == 'nuLnu'):
        distfact = 4*np.pi*(rpc*pc.val)**2
        lumfact  = sp.freq
        ylabel   = r"$\nu$L$_{\nu}$ [erg s$^{-1}$]"
    elif(kind == 'nuFnu'):
        distfact = 1./(rpc**2)
        lumfact  = sp.freq
        ylabel   = r"$\nu$F$_{\nu}$ [erg cm$^{-2}$ s$^{-1}$]"
    elif(kind == 'Fnu'):
        distfact = 1./(rpc**2)
        lumfact  = 1./Jy.val
        ylabel   = r"F$_{\nu}$ [Jy]"
    else:
        print(bold + 'Wrong SED quantity!' + reset)
        sys.exit(1)
    xcoord   = sp.Lambda
    xlabel   = r"$\lambda$ [$\mu$m]"
    pl.figure(figsize=(8,6))
    pl.xlabel(xlabel)
    pl.ylabel(ylabel)
    pl.loglog(xcoord,distfact*lumfact*sp.spectrum)
    pl.ylim(ymin=ymin)
    if(save):
        for format in ("png", "eps"):
            namefig = "spectrum." + format
            print(bold + "Save figure: " + reset + namefig)
            pl.savefig(namefig)
        pl.close()
    else:
        pl.show()
