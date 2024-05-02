import requests

def get_historical_weather_data(city, api_key, date):
    url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={city}&dt={date}"


    response = requests.get(url)


    if response.status_code == 200:
        data = response.json()
        
        temperature = data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
        conditions = data["forecast"]["forecastday"][0]["day"]["condition"]["text"]

        return temperature, conditions
    else:

        print(f"Erreur lors de la récupération des données: {response.status_code}")
        return None, None


api_key = "61064c6295144de9b63101812242904"
city = "casablanca"
date = "2024-04-20"  

temperature, conditions = get_historical_weather_data(city, api_key, date)



print(f"Les conditions météorologiques historiques à {city} le {date}:")
print(f"Température moyenne: {temperature:.1f}°C")
print(f"Conditions: {conditions}")
