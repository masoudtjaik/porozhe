import socket, datetime
from weather_api import Weather
from database import WeatherDatabase


def client_get():
    host = '192.168.64.1'
    port = 9090
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    city = input("Enter city: ").strip()
    # client.send("Hello!".encode('utf-8'))
    weather_object = WeatherDatabase()
    weather_object.save_request_data(city, str(datetime.datetime.now()))
    client.send(city.encode('utf-8'))
    client.send(city.encode('utf-8'))
    # if client.recv(1024) == "error":
    #     client_get()
    weather_city = client.recv(1024)
    weather_city = weather_city.decode()

    if weather_city == 'error':
        print("invalid city ")
        weather_object.save_connect(1)
        client_get()
    else:
        weather_object.save_connect(0)
        print(weather_city)


if __name__ == '__main__':
    client_get()
    print('successfully: ', WeatherDatabase.get_successful_request_count())
    print('request count: ', WeatherDatabase.get_request_count())
