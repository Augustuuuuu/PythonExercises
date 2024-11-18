import numpy as np
import matplotlib.pyplot as plt
def afim(distancia):
    bandeirada = 4.8
    valorPorKm = 0.4
    resultado = bandeirada + valorPorKm * distancia
    resultado_zero = bandeirada + valorPorKm * 0
    return resultado_zero, resultado

plt.plot(afim(4))


