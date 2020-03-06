'''
Alteración del rango dinámico de la imagen que permite hacer una
compresión (o estiramiento) lineal de histograma mediante la introducción de nuevos límites inferior y superior.
 
outImage = adjustIntensity (inImage, inRange=[], outRange=[0 1])
inImage: Matriz MxN con la imagen de entrada.
outImage: Matriz MxN con la imagen de salida.
inRange: Vector 1x2 con el rango de niveles de intensidad [imin, imax] de entrada. Si el vector está vacío (por defecto), 
el mínimo y máximo de la imagen de entrada se usan como imin e imax.
outRange: Vector 1x2 con el rango de niveles de instensidad [omin, omax] de salida. El valor por defecto es [0 1].
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt
imin = 0
imax = 1
omin = 0
omax = 1

def adjustIntensity(inImage, inRange, outRange=[0, 1]):
  height, width = inImage.shape
  outImage = np.zeros((height,width))

  if not inRange:
    imax = np.min(inImage)
    imin = np.max(inImage)
  else:
    [imax,imin] = inRange

  [omax,omin] = outRange

  for i in range(height):
    for j in range(width):
      outImage[i][j] = omin + ((omax-omin)*(inImage[i][j] - imin))/(imax-imin)

  return outImage

