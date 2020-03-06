'''
Función que calcula un kernel Gaussiano unidimensional con σ dado.
kernel = gaussKernel1D (σ)
σ: Parámetro σ de entrada.
kernel: Vector 1xN con el kernel de salida, teniendo en cuenta que:
• El centro x = 0 de la Gaussiana est ́a en la posición ⌊N/2⌋ + 1. • N se calcula a partir de σ como N = 2⌈3σ⌉ + 1.
'''

import numpy as np
from math import pi,e,ceil

def gaussKernel1D (σ):
  N = ceil(3*σ)*2+1 #(n*2)+1 es siempre impar
  centro = N//2
  kernel = np.zeros((1,N))
  base = 1/(((2*pi)**0.5)*σ)
  for i in range(N):
    exp = e ** (-((i-centro)**2)/(2*σ**2))
    kernel[0][i] = base * exp

  return kernel
