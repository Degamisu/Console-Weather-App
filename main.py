import curses
from io import SEEK_SET
from api_handler import get_weather
import geocoder
import os
import time
import csv

# Import the display_weather function from display_handler
from display_handler import display_weather

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
            try:
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
            except curses.error as e:
                print(f"Terminal error: {e}")
        self.manage_layout()

    def center_text(self, text, row):
        self.screen.addstr(row, (self.width - len(text)) // 2, text)

    def get_user_choice(self):
        self.screen.clear()
        self.center_text("Welcome to Console Weather App", 2)
        self.center_text("=======================================", 4)
        self.center_text("|Choose an option:                    |", 5)
        self.center_text("|1. Automatic GPS Location            |", 6)
        self.center_text("|2. City Select                       |", 7)
        self.center_text("|3. Important Information             |", 8)
        self.center_text("=======================================", 9)
        self.center_text("© Degamisu 2024 | All Rights Reserved", 11)

        while True:
            choice = self.screen.getch()

            if choice == ord('1'):
                return 'auto'
            elif choice == ord('2'):
                return 'city'
            elif choice == ord('3'):
                return 'info'
            elif choice == 10:  # Enter key
                return 'enter'
            elif choice == curses.KEY_RESIZE:
                self.get_screen_size()
            else:
                os.system("clear")
                self.center_text("Invalid choice. Please enter '1', '2', '3', or press Enter.", 9)
                self.center_text("Error: 0x0001", 10)
                self.screen.refresh()

    def display_info_screen(self):
        self.screen.clear()
        self.center_text("Important Information", 2)
        self.center_text("CWA", 4)
        self.center_text("===========================================================", 5)
        self.center_text("|Programming: Emi Yamashita                                |", 6)
        self.center_text("|Cover Art: Yumi Sasaki                                    |", 7)
        self.center_text("|Ideas and Suggestions: The wonderful community of Github. |", 8)
        self.center_text("===========================================================", 9)
        self.center_text("Press Enter to Return", 10)
        self.screen.refresh()
        enter = self.screen.getch()
        self.get_user_choice()

    def city_select(self):
        self.screen.clear()
        self.center_text("City Select", 2)
        self.center_text("Choose a city:", 4)

        # Load city data from CSV
        cities = self.load_cities()

        for i, city in enumerate(cities, start=6):
            self.center_text(f"{i - 5}. {city['City']}", i)

        while True:
            choice = self.screen.getch()

            if ord('1') <= choice <= ord(str(len(cities))):
                city_index = choice - ord('1')
                selected_city = cities[city_index]
                self.center_text(f"Selected City: {selected_city['City']}", len(cities) + 8)
                self.screen.refresh()

                # Fetch weather for the selected city
                weather_data = get_weather(selected_city['Latitude'], selected_city['Longitude'])
                self.display_weather_data(weather_data)
                return 'city'
            elif choice == curses.KEY_RESIZE:
                self.get_screen_size()
            else:
                self.center_text(f"Invalid choice. Press a number between 1 and {len(cities)}.", len(cities) + 8)
                self.screen.refresh()

    def load_cities(self):
        # Load city data from CSV file
        cities = []
        with open('cities_japan.csv', 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                cities.append(row)
        return cities

    def display_weather_data(self, weather_data):
        # Display weather data using the display_weather function
        display_weather(weather_data)
        # Alternatively, you can customize the display logic here if needed
        # ...

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

        # Define these variables before calling display_hourly_weather
        times = []
        temperatures = []
        relative_humidity = []
        wind_speeds = []

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
                self.city_select()
                # Fetch weather data for the city and populate the variables
                weather_data = get_weather(latitude, longitude)
                times = weather_data['hourly']['time']
                temperatures = weather_data['hourly']['temperature_2m']
                relative_humidity = weather_data['hourly']['relative_humidity_2m']
                wind_speeds = weather_data['hourly']['wind_speed_10m']

                self.display_hourly_weather(times, temperatures, relative_humidity, wind_speeds)
            elif choice == 'info':
                self.display_info_screen()
                # Wait for Enter key to return to the main menu
                self.screen.getch()
            elif choice == 'enter':
                # Add logic for handling Enter key press (e.g., return to the main menu)
                self.get_user_choice()
            else:
                self.center_text("Invalid choice. Exiting program.", 30)
                self.screen.refresh()
                self.screen.getch()
                return None
    def get_current_location_coordinates(self):
        location = geocoder.ip("me")
        latitude, longitude = None, None

        if location and location.latlng:
            latitude, longitude = tuple(location.latlng)
        elif not location and location.latlng:
            self.center_text("Unable to determine current location.", 30)
            self.center_text("Error: 0x0002", 31)
            self.center_text("CWA will now quit", 32)
            self.screen.refresh()
            self.screen.getch()

    def get_current_location_coordinates(self):
        location = geocoder.ip("me")
        latitude, longitude = None, None

        if location and location.latlng:
            latitude, longitude = tuple(location.latlng)
            weather_data = get_weather(latitude, longitude)

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

            # Display weather using the display_weather function
            self.display_weather_data(weather_data)

            self.center_text(f"Exiting process {pid}", 34)
            self.screen.refresh()
            self.screen.getch()
        else:
            self.center_text("Unable to determine current location.", 30)
            self.center_text("Error: 0x0002", 31)
            self.center_text("CWA will now quit", 32)
            self.screen.refresh()
            self.screen.getch()
            return None

        

if __name__ == "__main__":
    curses.wrapper(ConsoleWeatherApp().main)
