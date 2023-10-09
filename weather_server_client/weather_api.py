import requests, datetime


class Weather:
    api_key = "8b382996075d868e6628ae385aa81abb"

    def __init__(self, city):
        self.city = city
        self.url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={Weather.api_key}&units=metric"
        self.temp = None
        self.feels_like = None
        self.lst_update = None
        pass

    def get_city_weather(self):
        response_dict = self.validate_city()
        if response_dict:
            self.temp = response_dict['main']['temp']
            self.feels_like = response_dict['main']['feels_like']
            self.lst_update = datetime.datetime.now()
            return response_dict
        else:
            return False

    def validate_city(self):
        try:
            response = requests.get(self.url)
        except requests.exceptions.RequestException as e:
            raise "Dont find link "
        if response.status_code == 200:
            response_dict = response.json()
            return response_dict
        else:
            return False

    def __str__(self):
        return f'temp : {self.temp}°C\nfeels like : {self.feels_like}°C\nlast update : {self.lst_update}'
