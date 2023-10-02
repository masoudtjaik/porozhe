from weather_server import Weather


def start_server():
    while True:
        weather_input = input("enter name city: ")
        weather1 = Weather(weather_input)
        if weather1.get_city_weather():
            break
        print("Error retrieving weather data: No matching location found.")
    print(weather1)


if __name__ == "__main__":
    start_server()
