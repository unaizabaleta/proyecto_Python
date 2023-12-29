import krakenex
from pykrakenapi import KrakenAPI as KrakenAPI
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import plotly.graph_objects as go
from plotly.subplots import make_subplots as subplt
import streamlit as st
import numpy as np
#from cotizaciones import recoger_datos

def plot_cotizacion(data):
    fig = go.Figure()

    # Gráfico de precios
    fig.add_trace(
        go.Scatter(x=data["time_dt"], y=data['close'], mode='lines', name='Precio', line=dict(color='blue')))

    # Configuración del primer gráfico
    fig.update_layout(
        title='Gráfico de Precios',
        xaxis=dict(title='Fecha'),
        yaxis=dict(title='Precio', color='blue'),
    )

    return fig

def plot_indicadores(data):
    # Gráfico separado para %K y %D
    fig2 = go.Figure()

    # Gráfico de %K y %D
    fig2.add_trace(go.Scatter(x=data["time_dt"], y=data['SK'], mode='lines', name='%K', line=dict(color='green')))
    fig2.add_trace(go.Scatter(x=data["time_dt"], y=data['SD'], mode='lines', name='%D', line=dict(color='red')))

    # Configuración del segundo gráfico
    fig2.update_layout(
        title='Gráfico de Indicador Estocástico',
        xaxis=dict(title='Fecha'),
        yaxis=dict(title='SK/SD', color='black'),
    )

    return fig2


def combinar_figuras(figura1, figura2):
    # Crear subgráfico con escalas y ejes y diferentes
    fig = subplt(rows=1, cols=1, shared_xaxes=True, vertical_spacing=0.1, specs=[[{"secondary_y": True}]])

    # Agregar traza de la figura 1
    for trace in figura1.data:
        fig.add_trace(trace, secondary_y=False)

    # Agregar traza de la figura 2 con eje y secundario
    for trace in figura2.data:
        fig.add_trace(trace, secondary_y=True)

    # Configurar layout y ejes
    fig.update_layout(title_text='Figuras Combinadas')

    return fig

