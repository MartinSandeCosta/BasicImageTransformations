'''
Filtro de medianas bidimensional, especificando el tamaño del filtro.
outImage = medianFilter (inImage, filterSize) inImage, outImage: ...
filterSice: Valor entero N indicando que el tamaño de ventana es de NxN. La posición central de la ventana es (⌊N/2⌋ + 1, ⌊N/2⌋ + 1).
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

def medianFilter( inImage, filterSize):
  height, width = inImage.shape
  center = filterSize//2
  outImage = np.zeros((height,width))
  
  padding = np.zeros(((height+center*2),(width+center*2)))
  height2, width2 = padding.shape
  #Creamos la nueva imagen con padding en los bordes
  for i in range (center, (height2-center)):
    for j in range (center, (width2-center)):
      padding[i][j] = inImage[i-center][j-center] 
  
  #Recorremos la matriz ignorando el padding
  for i in range (center, (height2-center)):
    for j in range (center, (width2-center)):
      submatrix = padding[i-center:i+center+1,j-center:j+center+1]
      median = np.median(submatrix)
      outImage[i-center][j-center] = median

  return outImage

