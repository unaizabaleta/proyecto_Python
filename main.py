import streamlit
from code.cotizaciones import get_criptos, recoger_datos
from code.media_movil import calcular_estocastico
from code.plot import plot_cotizacion, plot_indicadores, combinar_figuras
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots as subplt
## Elegir divisa
streamlit.title("Cotización de criptomonedas - Indicadores Estocásticos")
# Selección de la divisa:
divisas=['USD','EUR']
divisa=streamlit.selectbox('¿En qué divisa está la criptomoneda a representar?',divisas)
# Selección de la criptomoneda:
if divisa:
    pair_list=get_criptos(divisa)
cripto=streamlit.selectbox('Elije una divisa:',pair_list)
## Sacar las criptomonedas con tal divisa
# Selección del intervalo de las velas:
intervals=[15, 60, 1440, 10080]
interval=streamlit.selectbox('Elije un intervalo en minutos:',intervals)
streamlit.write(f'Se analizará la criptomoneda {cripto}, con un intervalo temporal de  {interval} minutos')
## Bajar los datos de tal divisa
data = recoger_datos(cripto,interval)
## Plotearla (Igual se pueden meter mas cosas aqui, opciones de escala y tal)

k = streamlit.slider("Selecciona el periodo para el cálculo de %K", 10, 100, 28)
n1 = streamlit.slider("Selecciona el intervalo para la media móvil de %SK", 2, 20, 5)
n2 = streamlit.slider("Selecciona el intervalo para la media móvil de %SD", 2, 20, 5)
mostrar_graficas_juntas = streamlit.checkbox("¿Quieres ver las gráficas juntas?", value=False)
data = calcular_estocastico(data,k,n1,n2)
fig = plot_cotizacion(data)
fig2 = plot_indicadores(data)
figc = combinar_figuras(fig, fig2)
if mostrar_graficas_juntas:
    streamlit.plotly_chart(figc)
else:
    streamlit.plotly_chart(fig)
    streamlit.plotly_chart(fig2)