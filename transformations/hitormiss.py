'''Transformada hit-or-miss de una imagen, dados dos elementos estructurantes de objeto y fondo
 
outImage = hit or miss (inImage, objSEj, bgSE, center=[]) inImage, outImage, center: ...
objSE: Matriz PxQ de zeros y unos definiendo el elemento estructurante del objeto.
bgSE: Matriz PxQ de zeros y unos definiendo el elemento estructurante del fondo.
Nota. Se debe indicar “Error: elementos estructurantes incoherentes” si para alguna posición de PxQ hay unos simult ́aneamente en objSE y bgSE.
'''
import numpy as np
import matplotlib.pyplot as plt
from morfologicos_en_eg import erode
from negativo import adjustIntensity

def hit_or_miss(inImage, objSE, bgSE, center):
  height, width = inImage.shape
  (P,Q) = objSE.shape
  negativo = adjustIntensity(inImage,[0,1.0],[])
  outImage = np.bitwise_and(erode(inImage, objSE, center),erode(negativo, bgSE, center).astype(int))
  
  return outImage
