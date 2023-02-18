from calculo_estacionalidad.estacionalidad import Estacionalidad
from nivel_serie import Nivel_serie
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#plt.style.use('_mpl-gallery')

# make data
df = pd.read_table("tempsantiago.dat", header=None, sep='\s+')

# Se segmenta el numero de la variable parados.
tiempo = np.linspace(1, len(df[0]), len(df[0]))
parados = df[0]


nivel_serie = Nivel_serie(tiempo, parados)
# Tendencia con la serie con el método de regresión lineal.
#tendencia = nivel_serie.calculo()

#Tendencia de la serie con el método de la media móvil.
tendencia = nivel_serie.caculco_media_movil()

#Cálculo de la serie sin tendencia y medición de la tendencia de
#la misma.
E_t = parados - tendencia 
nivel_serie_Et = Nivel_serie(tiempo, E_t)
#tendencia_Et = nivel_serie_Et.calculo()
tendencia_Et = nivel_serie_Et.caculco_media_movil()

Estacionalidad = Estacionalidad(E_t, tiempo)
S_t = Estacionalidad.calculo(periodo=4)

# Grafica de series
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, sharex=True)
fig.suptitle('Métodos de descomposición para series estacionales')
ax1.plot(tiempo, parados, linewidth=2.0)
ax1.plot(tiempo, tendencia, linewidth=2.0)
ax2.plot(tiempo, E_t, linewidth=2.0)
ax2.plot(tiempo, tendencia_Et, linewidth=2.0)
ax3.plot(tiempo, S_t, linewidth=2.0)
ax4.plot(tiempo, parados, linewidth=2.0)
ax4.plot(tiempo, S_t+tendencia, linewidth=2.0)
plt.show()

