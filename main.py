# main_curses_resizable.py

import curses
from api_handler import get_weather
import geocoder
import os
import time

# Setup process ID variable
pid = os.getpid()

class ConsoleWeatherApp:
    def __init__(self):
        self.height = 0
        self.width = 0
        self.screen = None

    def get_screen_size(self):
        time.sleep(0.1)  # prevents curses.error on rapid resizing
        while True:
            self.screen.clear()  # Clear the screen before refreshing
            self.screen.refresh()
            self.height, self.width = self.screen.getmaxyx()
            # Tracker list breaks if width smaller than 73
            if self.width < 73 or self.height < 16:
                self.screen.erase()
                self.screen.addstr(0, 0, "Terminal too small", curses.A_REVERSE + curses.A_BOLD)
                time.sleep(1)
            else:
                break
        self.manage_layout()

    def center_text(self, text, row):
        self.screen.addstr(row, (self.width - len(text)) // 2, text)

    def get_user_choice(self):
        self.screen.clear()
        self.center_text("Welcome to Console Weather App", 2)
        self.center_text("© Degamisu 2024 | All Rights Reserved | Emi Yamashita", 3)
        self.center_text("Choose an option:", 5)
        self.center_text("1. Automatic GPS Location", 6)
        self.center_text("2. City Select", 7)

        while True:
            choice = self.screen.getch()

            if choice == ord('1'):
                return 'auto'
            elif choice == ord('2'):
                return 'city'
            elif choice == curses.KEY_RESIZE:
                self.get_screen_size()
            else:
                os.system("clear")
                self.center_text("Invalid choice. Please enter '1' or '2.'", 9)
                self.center_text("Error: 0x0001", 10)
                self.screen.refresh()

    def get_city_coordinates(self):
        self.center_text("Enter the city name:", 12)
        city = self.screen.getstr(13, (self.width - len("")) // 2).decode('utf-8')

        # You might want to add error handling and validation for the city input
        self.center_text("City input is currently not implemented.", 14)
        self.center_text("CWA will now quit", 15)
        self.screen.refresh()
        self.screen.getch()
        exit()

    def get_current_location_coordinates(self):
        location = geocoder.ip("me")
        if location and location.latlng:
            return tuple(location.latlng)
        else:
            self.center_text("Unable to determine current location.", 30)
            self.center_text("Error: 0x0002", 31)
            self.center_text("CWA will now quit", 32)
            self.screen.refresh()
            self.screen.getch()
            exit()

    def display_hourly_weather(self, times, temperatures, relative_humidity, wind_speeds):
        max_rows, _ = self.screen.getmaxyx()
        rows_to_display = min(max_rows - 18, len(times) * 5)

        for i, time_data in enumerate(zip(times, temperatures, relative_humidity, wind_speeds), start=18):
            if i + 4 > 18 + rows_to_display:
                break

            self.center_text(f"Time: {time_data[0]}", i)
            self.center_text(f"Temperature at 2m: {time_data[1]}°C", i + 1)
            self.center_text(f"Relative Humidity at 2m: {time_data[2]}%", i + 2)
            self.center_text(f"Wind Speed at 10m: {time_data[3]} m/s", i + 3)
            self.center_text("---", i + 4)

        self.screen.refresh()

    def manage_layout(self):
        # Implement layout management logic here if needed
        pass

    def main(self, stdscr):
        self.screen = stdscr
        curses.curs_set(0)  # Hide the cursor
        os.system("clear")
        self.get_screen_size()

        while True:
            choice = self.get_user_choice()

            if choice == 'auto':
                coordinates = self.get_current_location_coordinates()

                if coordinates:
                    latitude, longitude = coordinates
                else:
                    self.center_text("Exiting program.", 30)
                    self.screen.refresh()
                    self.screen.getch()
                    os.system('clear')
                    return
            elif choice == 'city':
                self.get_city_coordinates()
                # Implement code to get coordinates for the specified city
                # For simplicity, let's assume fixed coordinates for now
                latitude, longitude = 40.7128, -74.0060
            else:
                self.center_text("Invalid choice. Exiting program.", 30)
                self.screen.refresh()
                self.screen.getch()
                return

            weather_data = get_weather(latitude, longitude)

            if weather_data:
                # Display the current weather data
                self.center_text("Current Weather:", 17)
                self.center_text(f"Time: {weather_data['current']['time']}", 18)
                self.center_text(f"Temperature at 2m: {weather_data['current']['temperature_2m']}°C", 19)
                self.center_text(f"Wind Speed at 10m: {weather_data['current']['wind_speed_10m']} m/s", 20)

                # Display hourly weather data for the last hour
                self.center_text("Weather in the Last Hour:", 22)
                self.display_hourly_weather(
                    weather_data['hourly']['time'][:1],
                    weather_data['hourly']['temperature_2m'][:1],
                    weather_data['hourly']['relative_humidity_2m'][:1],
                    weather_data['hourly']['wind_speed_10m'][:1]
                )

                self.center_text("Continue to display more Weather Data? | y/n:", 30)
                inp = self.screen.getch()

                if inp == ord('y'):
                    self.center_text("Fetching more weather data...", 32)
                    self.screen.refresh()
                    # Implement logic for fetching more weather data if needed
                    # For now, let's assume there's more data to display
                    self.display_hourly_weather(
                        weather_data['hourly']['time'],
                        weather_data['hourly']['temperature_2m'],
                        weather_data['hourly']['relative_humidity_2m'],
                        weather_data['hourly']['wind_speed_10m']
                    )

                self.center_text(f"Exiting process {pid}", 34)
                self.screen.refresh()
                self.screen.getch()
            else:
                self.center_text("Unable to fetch weather data.", 30)
                self.screen.refresh()
                self.screen.getch()

if __name__ == "__main__":
    curses.wrapper(ConsoleWeatherApp().main)
