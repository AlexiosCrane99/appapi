from Modelo.CapaDatos.ApiService import obtener_tasa
from Modelo.CapaDatos.ModeloDivisa import Divisa

def convertir_moneda(monto, moneda_base, moneda_destino):
    """ Convierte una cantidad de una moneda a otra. """
    tasa = obtener_tasa(moneda_base, moneda_destino)
    if tasa:
        conversion = monto * tasa
        return Divisa(moneda_base, moneda_destino, conversion)
    else:
        return None
