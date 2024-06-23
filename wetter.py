import requests
import tkinter as tk


def get_weather(api_key, city):
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen der Daten: {e}")
        return None
    
api_key=""
city="Berlin"
weather_data = get_weather(api_key, city)

if weather_data:
    print(weather_data)

def update_weather():
    city = city_entry.get()
    weather_data = get_weather(api_key, city)
    if weather_data:
        city_label.config(text=f"Stadt: {weather_data['name']}")
        temp_label.config(text=f"Temperatur: {weather_data['main']['temp']}°C")
        weather_label.config(text=f"Wetter: {weather_data['weather'][0]['description']}")
    else:
        city_label.config(text="Stadt: Fehler")
        temp_label.config(text="Temperatur: Fehler")
        weather_label.config(text="Wetter: Fehler")

# Dein API-Schlüssel (ersetze dies durch deinen tatsächlichen Schlüssel)
api_key = ""

# Erstellen des Hauptfensters
root = tk.Tk()
root.title("Wetterinformationen")

# Erstellen der GUI-Elemente
tk.Label(root, text="Stadt:").pack()
city_entry = tk.Entry(root)
city_entry.pack()

tk.Button(root, text="Wetter abrufen", command=update_weather).pack()

city_label = tk.Label(root, text="Stadt: ")
city_label.pack()

temp_label = tk.Label(root, text="Temperatur: ")
temp_label.pack()

weather_label = tk.Label(root, text="Wetter: ")
weather_label.pack()

# Hauptschleife starten
root.mainloop()
