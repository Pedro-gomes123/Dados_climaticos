import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

def fetch_data():
    url = "https://api.open-meteo.com/v1/forecast"

    # 🔹 Variáveis que queremos coletar
    variables = [
        "temperature_2m",
        "relative_humidity_2m",
        "wind_speed_10m",
        "weather_code"
    ]

    params = {
        "latitude": -8.0539,
        "longitude": -34.8811,
        "hourly": variables,
        "timezone": "America/Recife"
    }

    # 🔹 Configuração de cache + retry
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # 🔹 Requisição
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]

    # 🔹 Dados horários
    hourly = response.Hourly()

    # 🔹 Criando base de datas
    hourly_data = {
        "date": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left"
        )
    }

    # 🔹 Loop para pegar todas variáveis automaticamente
    for i, var in enumerate(variables):
        hourly_data[var] = hourly.Variables(i).ValuesAsNumpy()

    # 🔹 Traduzindo weather_code
    weather_map = {
        0: "Céu limpo",
        1: "Parcialmente nublado",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Neblina",
        48: "Neblina com gelo",
        51: "Garoa leve",
        53: "Garoa moderada",
        55: "Garoa intensa",
        61: "Chuva leve",
        63: "Chuva moderada",
        65: "Chuva forte",
        71: "Neve leve",
        73: "Neve moderada",
        75: "Neve forte",
        95: "Tempestade"
    }

    hourly_data["weather_description"] = [
        weather_map.get(code, "Desconhecido")
        for code in hourly_data["weather_code"]
    ]

    # 🔹 Criando DataFrame
    df = pd.DataFrame(hourly_data)

    # 🔹 Ajuste opcional de timezone (de UTC para local)
    df["date"] = df["date"].dt.tz_convert("America/Recife")

    print("\n📊 Dados horários:\n")
    print(df.head())

    return df


# 🔹 Executar
if __name__ == "__main__":
    df = fetch_data()