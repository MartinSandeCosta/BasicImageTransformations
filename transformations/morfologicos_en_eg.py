'''
Operadores morfológicos de erosión, dilatación, apertura y cierre para imágenes binarias y elemento estructurante arbitrario.
 
outImage = erode (inImage, SE, center=[]) 
outImage = dilate (inImage, SE, center=[]) 
outImage = opening (inImage, SE, center=[]) 
outImage = closing (inImage, SE, center=[])
inImage, outImage: ...
SE: heightmatriz PxQ de zeros y unos definiendo el elemento estructurante.
center: Vector 1x2 con las coordenadas del centro de SE. Se asume que el [0 0] es la esquina superior izquierda. 
Si es un vector vac ́ıo (valor por defecto), el centro se calcula como (⌊P /2⌋ + 1, ⌊Q/2⌋ + 1).
'''
import numpy as np
import matplotlib.pyplot as plt
import math
import cv2

def dilate (inImage, SE, center=[]):
  height, width = inImage.shape
  (P,Q) = SE.shape
  imagen = list()
  element = list()

  if not center:
    y,x = P//2, Q//2
  else:
    y,x = center

  if (SE[x][y] == 1):
    outImage = inImage
  else:
    outImage = np.zeros((height,width))
  
  for i in range (height):
    for j in range (width):
      if (inImage[i][j] == 1):
        imagen.append((j,i))

  for i in range (P):
    for j in range (Q):
      if (SE[i][j] == 1):
        element.append((i-x,j-y))
  
  for i in range (height):
    for j in range (width):
      for k in range (len(element)):
        element_translated = (element[k][0]+j, element[k][1]+i)
        if (element_translated in imagen):
          outImage[i][j] = 1
          k = len(element)-1

  return outImage

def erode (inImage, SE, center=[]): 
  height, width = inImage.shape
  (P,Q) = SE.shape
  imagen = list()
  element = list()
  outImage = inImage

  if not center:
    y,x = P//2, Q//2
  else:
    y,x = center

  if (SE[x][y] == 1):
    outImage = inImage
  else:
    outImage = np.zeros((height,width))
  
  for i in range (height):
    for j in range (width):
      if (inImage[i][j] == 1):
        imagen.append((j,i))

  for i in range (P):
    for j in range (Q):
      if (SE[i][j] == 1):
        element.append((i-x,j-y))

  for i in range (height):
    for j in range (width):
      for k in range (len(element)):
        element_translated = (element[k][0]+j, element[k][1]+i)
        x = element_translated[0]
        y = element_translated[1]
        if ((element_translated not in imagen) and (x >= 0 and y>= 0) and (x < width and y < height)):
          outImage[i][j] = 0
          k = len(element)-1
  
  return outImage

def opening (inImage, SE, center=[]):
  erosion = erode(inImage, SE, center)
  outImage = dilate(erosion, SE, center)

  return outImage


def closing (inImage, SE, center=[]):
  dilatacion = dilate(inImage, SE, center)
  outImage = erode(dilatacion, SE, center)
  
  return outImage

