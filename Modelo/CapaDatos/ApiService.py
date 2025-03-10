import requests
from config import API_KEY, BASE_URL

def obtener_tasa(moneda_base, moneda_destino):
    """ Obtiene la tasa de cambio entre dos monedas usando currencyapi. """
    url = f"{BASE_URL}?apikey={API_KEY}&base_currency={moneda_base}"
    
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        
        if "data" in datos and moneda_destino in datos["data"]:
            return datos["data"][moneda_destino]["value"]
        else:
            return None
    except Exception as e:
        print(f"Error al obtener la tasa de cambio: {e}")
        return None
