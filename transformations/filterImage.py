'''
Filtrado espacial mediante convolución sobre una imagen con un kernel arbitrario 
que se le pasa como parametro.
outImage = filterImage (inImage, kernel) inImage, outImage: ...
kernel: heightatriz PxQ con el kernel del filtro de entrada. 
Se asume que la posición central del filtro está en (⌊P/2⌋ + 1, ⌊Q/2⌋ + 1).
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

def filterImage (inImage, kernel):
  height, width = inImage.shape
  (P,Q) = kernel.shape
  y,x = P//2, Q//2
  outImage = np.zeros((height,width))
  
  padding = np.zeros(((height+y*2),(width+x*2)))
  height2, width2 = padding.shape
  #Creamos la nueva imagen con padding en los bordes
  for i in range (y, (height2-y)):
    for j in range (x, (width2-x)):
      padding[i][j] = inImage[i-y][j-x] 
  
  #Recorremos la matriz ignorando el padding
  for i in range (y, (height2-y)):
    for j in range (x, (width2-x)):
      newpixel = 0
      #Recorremos kernel
      for p in range (P):
        for q in range (Q):
          newpixel += kernel[p][q] * padding[i+p-y][j+q-x]
      outImage[i-y][j-x] = newpixel

  return outImage
