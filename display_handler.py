# display_handler.py

import curses

def display_weather(weather_data):
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
        print("Unable to fetch weather data.")