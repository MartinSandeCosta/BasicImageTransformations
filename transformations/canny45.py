'''
Detector de bordes de Canny

outImage = edgeCanny (inImage, σ, tlow, thigh)
inImage, outImage: ...
Sigma: Parámetro σ del filtro Gaussiano.
tlow, thigh: Umbrales de hist ́eresis bajo y alto, respectivamente.
'''
import cv2
import numpy as np
from math import pi
from gaussKernel1D import gaussKernel1D
from gaussianFilter import gaussianFilter
from gradientImage import gradientImage, toString
import matplotlib.pyplot as plt
from negativo import adjustIntensity as negativo


def thresholding(I_n, tlow, thigh, orientacion):
	height,width = I_n.shape
	visitados = set()
	H = np.zeros((height,width))
	for i in range (height):
		for j in range (width):
			#Localizar el próximo punto borde no visitado, I_n(i,j) tal que IN(i,j) > thigh
			if ((I_n[i][j] > thigh) & ((i,j) not in visitados)):
				visitados.add((i,j))
				H[i][j] = I_n[i][j]
				#diagonal izquierda
				if ((orientacion[i][j] >= 112) & (orientacion[i][j] <= 157)):
					recorrerx = i-1
					recorrery = j-1
					#recorremos hacia izquierda el borde
					while((I_n[recorrerx][recorrery]>tlow) & (recorrerx>=0) & (recorrery <height)):
						visitados.add((recorrerx,recorrery))
						H[recorrerx][recorrery] = I_n[recorrerx][recorrery]
						recorrerx -= 1
						recorrery -= 1
					#recorremos hacia derecha el borde
					recorrerx = i+1
					recorrery = j+1
					while((I_n[recorrerx][recorrery]>tlow) & (recorrerx<width) & (recorrery >=0)):
						visitados.add((recorrerx,recorrery))
						H[recorrerx][recorrery] = I_n[recorrerx][recorrery]
						recorrerx+=1
						recorrery+=1
				
	return H

def edgeCanny (inImage, σ, tlow, thigh):
	#1.Mejora de la imagen
	#Suavizar la imagen y eliminar el ruido
	J = gaussianFilter(inImage, σ)
	#Localizar los bordes en la imagen mejorada
	[Jx, Jy] = gradientImage(J, toString(3))
	#Para cada pixel (i,j)
	#Usar un detector de bordes para calcular las componentes del gradiente Jx y Jy
	#Calcular la magnitud y orientación de los bordes
	E_m = np.sqrt(Jx**2 + Jy**2)
	E_o = np.arctan(np.divide(Jy, Jx))
	expanded = ((E_o +(pi/2))/(pi))*180
	
	#2.Supresión no máxima
	#Producir bordes de 1 pixel de grosor
	height,width = expanded.shape
	E_s = np.zeros((height,width))
	for i in range (height-2):
		for j in range (width-2):
			if ((expanded[i][j] >= 112) & (expanded[i][j] <= 157)):
				if not ((E_m[i][j] < E_m[i-1][j-1]) | (E_m[i][j] < E_m[i+1][j+1])):
					E_s[i][j] = E_m[i][j]

	#3.Umbralización con histéresis
	#Descartar los posibles máximos locales creados por ruido sin eliminar bordes débiles
	#Se utilizarán dos umbrales tlow y thigh, tlow < thigh
	H = thresholding(E_s, tlow, thigh, expanded)

	return H

