'''
Ecualización de histograma.
 
outImage = equalizeIntensity (inImage, nBins=256) inImage, outImage: ...
nBins: Nu ́mero de bins utilizados en el procesamiento. Se asume que el intervalo de entrada [0 1] 
se divide en nBins intervalos iguales para hacer el procesamiento, y que la imagen de salida vuelve a 
quedar en el intervalo [0 1]. Por defecto 256.
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

def equalizeIntensity (inImage, nBins=256):
  height, width = inImage.shape
  outImage = np.zeros((height,width))

  hist,bins = np.histogram(inImage.flatten(),nBins,[0,1])
  cdf = hist.cumsum()

  histout = hist
  cdfmin = np.min(cdf)
  for i in range(nBins):
    histout[i] = round((nBins)*(cdf[i]-cdfmin)/((height*width)-cdfmin))

  for i in range(height):
    for j in range(width):
      outImage[i][j] = histout[int(inImage[i][j]*255)]/255

  return outImage

