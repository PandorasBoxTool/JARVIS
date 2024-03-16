import requests
import pyttsx3

def get_weather_info(city_name):

    # API-Key für WeatherAPI
    api_key = "YOUR_KEY_FROM_WEATHERAPI"
    
    # URL für die Wetter-API
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}"
    
    # Anfrage an die Wetter-API senden
    response = requests.get(url)
    data = response.json()
    
    # Wetterinformationen aus der API-Antwort extrahieren
    if 'error' in data:
        print("Fehler beim Abrufen der Wetterdaten:", data['error']['message'])
        return
    
    location = data['location']['name']
    condition = data['current']['condition']['text']
    temperature = data['current']['temp_c']
    humidity = data['current']['humidity']
    
    # Text für die Wetterinformationen erstellen
    weather_text = f"In {location} ist das Wetter {condition}. Die Temperatur beträgt {temperature} Grad Celsius und die Luftfeuchtigkeit beträgt {humidity} Prozent."
    
    # Text vorlesen
    engine = pyttsx3.init()
    engine.say(weather_text)
    engine.runAndWait()
