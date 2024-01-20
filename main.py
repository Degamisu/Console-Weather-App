# main.py

from api_handler import get_weather
import geocoder
import os
import time

# Setup process ID variable
pid = os.getpid()

os.system('clear')

print("Welcome to Console Weather App".center(40))
print("© Degamisu 2024 | All Rights Reserved | Emi Yamashita".center(40))
print()

def get_user_choice():
    print("Choose an option:".center(40))
    print("1. Automatic GPS Location".center(40))
    print("2. City Select".center(40))
    
    while True:
        choice = input("Enter the number of your choice: ".center(40))
        
        if choice == '1':
            return 'auto'
        elif choice == '2':
            return 'city'
        else:
            os.system('clear')
            print("Invalid choice. Please enter '1' or '2.'".center(40))
            print("Error: 0x0001".center(40))
            print()
            input("Press enter to exit: ")
            os.system('clear')
            exit()


def get_city_coordinates():
    city = input("Enter the city name: ")
    # You might want to add error handling and validation for the city input
    print("City input is currently not implemented.")
    print("CWA will now quit")
    time.sleep(3)
    os.system('clear')
    exit()

def get_current_location_coordinates():
    location = geocoder.ip("me")
    if location and location.latlng:
        return tuple(location.latlng)
    else:
        print("Unable to determine current location.")
        print("Error: 0x0002")
        return None

def display_hourly_weather(times, temperatures, relative_humidity, wind_speeds):
    for i in reversed(range(len(times))):
        print(f"Time: {times[i]}")
        print(f"Temperature at 2m: {temperatures[i]}°C")
        print(f"Relative Humidity at 2m: {relative_humidity[i]}%")
        print(f"Wind Speed at 10m: {wind_speeds[i]} m/s")
        print("\n---")

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
        # Display the current weather data
        print("Current Weather:")
        print(f"Time: {weather_data['current']['time']}")
        print(f"Temperature at 2m: {weather_data['current']['temperature_2m']}°C")
        print(f"Wind Speed at 10m: {weather_data['current']['wind_speed_10m']} m/s")

        # Display hourly weather data for the last hour
        print("\nWeather in the Last Hour:")
        display_hourly_weather(
            weather_data['hourly']['time'][:1],
            weather_data['hourly']['temperature_2m'][:1],
            weather_data['hourly']['relative_humidity_2m'][:1],
            weather_data['hourly']['wind_speed_10m'][:1]
        )
        
        inp = input("Continue to display more Weather Data? | y/n: ")
        
        if inp.lower() == 'y':
            times = weather_data['hourly']['time']
            temperatures = weather_data['hourly']['temperature_2m']
            relative_humidity = weather_data['hourly']['relative_humidity_2m']
            wind_speeds = weather_data['hourly']['wind_speed_10m']
            print(f"Time: {weather_data['hourly']['time']}")
            print(f"Temperature at 2m: {weather_data['hourly']['temperature_2m']}°C")
            print(f"Wind Speed at 10m: {weather_data['hourly']['wind_speed_10m']} m/s")

            for i in reversed(range(len(times))):
                print(f"Time: {times[i]}")
                print(f"Temperature at 2m: {temperatures[i]}°C")
                print(f"Relative Humidity at 2m: {relative_humidity[i]}%")
                print(f"Wind Speed at 10m: {wind_speeds[i]} m/s")
                print("\n---")
            

        if inp.lower() == 'n':
            print("Exiting process", pid)
    else:
        print("Unable to fetch weather data.")

if __name__ == "__main__":
    main()
