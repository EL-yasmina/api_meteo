import requests

def get_weather_data(city, api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"


    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        temperature = data["current"]["temp_c"]
        feels_like = data["current"]["feelslike_c"]
        conditions = data["current"]["condition"]["text"]

        return temperature, feels_like, conditions
    else:

        print(f"Erreur lors de la récupération des données météorologiques: {response.status_code}")
        return None, None, None


api_key = "61064c6295144de9b63101812242904"
city = "Paris"

# Appel à la fonction get_weather_data
temperature, feels_like, conditions = get_weather_data(city, api_key)


print(f"Les conditions météorologiques actuelles à {city}:")
print(f"Température: {temperature:.1f}°C")
print(f"Ressentie: {feels_like:.1f}°C")
print(f"Conditions: {conditions}")
