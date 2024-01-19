# display_handler.py

def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Conditions: {weather_data['weather'][0]['description']}")
    else:
        print("Unable to fetch weather data.")
