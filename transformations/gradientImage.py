'''
Función que permite obtener las componentes Gx y Gy del gradiente de una imagen, 
pudiendo elegir entre los operadores de Roberts, CentralDiff (Diferencias centrales de Prewitt/Sobel sin promedio), Prewitt y Sobel.
[gx, gy] = gradientImage (inImage, operator)
inImage: ...
gx, gy: Componentes Gx y Gy del gradiente.
operator: Permite seleccionar el operador utilizado mediante los valores: ’Roberts’, ’CentralDiff’, ’Prewitt’ o ’Sobel’.
'''

import cv2
import numpy as np
from filterImage import filterImage

def toString(argument):
    switcher = {
        0: "Roberts",
        1: "CentralDiff",
        2: "Prewitt",
        3: "Sobel",
    }
    return switcher.get(argument)

def create(argument):
  switcher = {
    "Roberts": (np.array([[-1, 0],[0, 1]]),np.array([[0, -1],[1, 0]])),
    "CentralDiff": (np.array([[-1, 0, 1]]),np.array([[-1],[0],[1]])),
    "Prewitt": (np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]]),np.array([[-1, -1, -1],[0, 0, 0],[1, 1, 1]])),
    "Sobel": (np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]]),np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]]))
  }
  return switcher.get(argument)

def gradientImage (inImage, operator):

  Gx, Gy = create(operator)

  gx = filterImage(inImage, Gx)
  gy = filterImage(inImage, Gy)   
  
  return [gx, gy]
