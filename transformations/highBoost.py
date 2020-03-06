'''
Filtro de realce High Boost que permite especificar, 
además del factor de amplificación A, el método de suavizado utilizado y su parámetro.

outImage = highBoost (inImage, A, method, param)
inImage, outImage: ...
A: Factor de amplificación del filtro high-boost. method: 
Método de suavizado. Los valores pueden ser:
• ’gaussian’, indicando que usará la función gaussianFilter.
• ’median’, indicando que se usará la función medianFilter.
param: Valor del parámetro del filtro de suavizado. 
Proporcionará el valor de σ en el caso del filtro Gaussiano, y el tamaño de ventana en el caso del filtro de medianas.
'''
import cv2
import matplotlib.pyplot as plt
from gaussianFilter import gaussianFilter
from medianFilter import medianFilter
from filterImage import filterImage
from gaussKernel1D import gaussKernel1D
from adjustIntensity import adjustIntensity

def highBoost (inImage, A, method, param):
  if (method == "gaussian"):
      outImage = (gaussianFilter(inImage, param)) 
  if (method == "median"):
      outImage = (medianFilter(inImage, param))
 
  outImage = adjustIntensity((A)*(inImage)-(outImage), [], [0, 1])
  
  return outImage
