# display_handler.py

import curses

def display_weather(stdscr, weather_data):
    # Check if the necessary keys exist in the weather_data dictionary
    if 'name' in weather_data and 'sys' in weather_data and 'country' in weather_data['sys']:
        city_name = weather_data['name']
        country_code = weather_data['sys']['country']
        stdscr.addstr(2, 2, f"Weather in {city_name}, {country_code}:")
    
    if weather_data:
        stdscr = curses.initscr()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        stdscr.bkgd(curses.color_pair(1))

        stdscr.addstr(2, 2, f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        stdscr.addstr(4, 2, f"Temperature: {weather_data['main']['temp']}°C")
        stdscr.addstr(6, 2, f"Conditions: {weather_data['weather'][0]['description']}")
        
        stdscr.refresh()
        stdscr.getch()
        curses.endwin()
    else:
        stdscr.addstr(2, 2, "Weather data is incomplete. Unable to display.")