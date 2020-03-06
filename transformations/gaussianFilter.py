'''
Suavizado Gaussiano bidimensional usando 
un filtro N × N de parámetro σ, donde N se calcula igual que en la función anterior.

outImage = gaussianFilter (inImage, σ)
inImage, outImage, σ: ...
Nota. Como el filtro Gaussiano es lineal y separable podemos implementar este suavizado simplemente convolucionando la imagen, 
primero, con un kernel Gaussiano unidimensional 1×N y, luego, convolucionando el resultado con el kernel transpuesto N × 1.
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
from filterImage import filterImage
from gaussKernel1D import gaussKernel1D

def gaussianFilter (inImage, σ):
  kernel = gaussKernel1D(σ)
  shifted_kernel = kernel.transpose()   
  outImage = filterImage(inImage, kernel)
  outImage = filterImage(outImage, shifted_kernel)
    
  return outImage
