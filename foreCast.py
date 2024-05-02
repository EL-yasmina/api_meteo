import requests

def get_weather_forecast(city, api_key, days):
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": api_key,
        "q": city,
        "days": days
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'forecast' in data:
        forecast_data = data['forecast']['forecastday']
        return forecast_data
    else:
        print("Erreur: Impossible de récupérer les données de prévision.")
        return []


api_key = '61064c6295144de9b63101812242904'
city = 'Paris'
days = 4

forecast_data = get_weather_forecast(city, api_key, days)

for forecast in forecast_data:
    date = forecast['date']
    avg_temp_c = forecast['day']['avgtemp_c']
    condition_text = forecast['day']['condition']['text']

    print("Date:", date)
    print("Température moyenne:", avg_temp_c, "°C")
    print("Conditions météorologiques:", condition_text)
    print()
