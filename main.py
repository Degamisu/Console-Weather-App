# main.py

from api_handler import get_weather
import geocoder

def get_user_choice():
    print("Choose an option:")
    print("1. Automatic GPS Location")
    print("2. City Select")
    
    while True:
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            return 'auto'
        elif choice == '2':
            return 'city'
        else:
            print("Invalid choice. Please enter '1' or '2'.")

def get_city_coordinates():
    city = input("Enter the city name: ")
    # You might want to add error handling and validation for the city input
    return city

def get_current_location_coordinates():
    location = geocoder.ip("me")
    if location and location.latlng:
        return tuple(location.latlng)
    else:
        print("Unable to determine current location.")
        return None

def main():
    choice = get_user_choice()

    if choice == 'auto':
        coordinates = get_current_location_coordinates()

        if coordinates:
            latitude, longitude = coordinates
        else:
            print("Exiting program.")
            return
    elif choice == 'city':
        city = get_city_coordinates()
        # Implement code to get coordinates for the specified city
        # For simplicity, let's assume fixed coordinates for now
        latitude, longitude = 40.7128, -74.0060
    else:
        print("Invalid choice. Exiting program.")
        return

    weather_data = get_weather(latitude, longitude)

    if weather_data:
        # Process and display the weather data as needed
        print("Current Weather:")
        print(f"Time: {weather_data['current']['time']}")
        print(f"Temperature at 2m: {weather_data['current']['temperature_2m']}°C")
        print(f"Wind Speed at 10m: {weather_data['current']['wind_speed_10m']} m/s")

        print("\nHourly Weather:")
        times = weather_data['hourly']['time']
        temperatures = weather_data['hourly']['temperature_2m']
        relative_humidity = weather_data['hourly']['relative_humidity_2m']
        wind_speeds = weather_data['hourly']['wind_speed_10m']

        for i in reversed(range(len(times))):
            print(f"Time: {times[i]}")
            print(f"Temperature at 2m: {temperatures[i]}°C")
            print(f"Relative Humidity at 2m: {relative_humidity[i]}%")
            print(f"Wind Speed at 10m: {wind_speeds[i]} m/s")
            print("\n---")

        else:
            print("Unable to fetch weather data.")

if __name__ == "__main__":
    main()
