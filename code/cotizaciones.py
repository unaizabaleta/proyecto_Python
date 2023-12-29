import krakenex
from pykrakenapi import KrakenAPI as KrakenAPI
import pandas as pd

def get_criptos(tipo):
    '''
    Función que pasada una divisa devuelve una lista con los pares de cripto disponibles a descargar.
    '''
    api = krakenex.API()
    krakenapi = KrakenAPI(api)
    aux = krakenapi.get_tradable_asset_pairs()
    aux = aux[aux["altname"].str.contains(tipo,case=False)]
    aux = aux["altname"]

    return aux.to_list()

def recoger_datos(moneda, intervalo):
    '''
    Función que extrae la tabla de cotización OHLC.
    '''
    api = krakenex.API()
    krakenapi = KrakenAPI(api)
    ohlc,_ = krakenapi.get_ohlc_data(moneda, interval=intervalo)
    ohlc['time_dt'] = pd.to_datetime(ohlc['time'], unit='s')
    return ohlc