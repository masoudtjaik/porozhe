import socket
from weather_api import Weather
from database import WeatherDatabase

host = '192.168.64.1'
port = 9090
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
while True:
    commiunication_socket, address = server.accept()
    print(f'connected to {address}')
    message = commiunication_socket.recv(1024).decode('utf-8')
    print(f'message from client is :{message}')
    object1 = Weather(message)
    weather_object = WeatherDatabase()
    list_dict = object1.get_city_weather()
    if list_dict:
        print(object1)
        weather_object.save_response_data(object1.city, list_dict)
        commiunication_socket.send(f'{object1}'.encode('utf-8'))



    else:
        list_dict = {'main': {
            'temp': 'null',
            'feels_like': 'null'
        }
        }
        # weather_object.save_connect(0)
        weather_object.save_response_data(message, list_dict)
        commiunication_socket.send(f'error'.encode('utf-8'))

    commiunication_socket.close()
    print(f'connection with {address} ended')
