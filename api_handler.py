# api_handler.py

import requests
import os
import time

def get_weather(latitude, longitude):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        print(f"Response Status Code: {response.status_code}")
        print(f"Number of bytes received: {len(response.content)}")
        print(f"Raw Response Content: {response.content}")
        print()
        print("Crunching Data . . .")

        if not response.content:
            print("Empty response content. Unable to fetch weather data.")
            return None
        time.sleep(3)
        os.system('clear')
        data = response.json()
        

        # hourly data
        data['hourly']['time'] = list((data['hourly']['time']))
        data['hourly']['temperature_2m'] = list((data['hourly']['temperature_2m']))
        data['hourly']['relative_humidity_2m'] = list((data['hourly']['relative_humidity_2m']))
        data['hourly']['wind_speed_10m'] = list((data['hourly']['wind_speed_10m']))

        return data

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
    except Exception as err:
        print(f"Error: {err}")

    return None
