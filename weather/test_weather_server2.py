import unittest, datetime
from unittest.mock import patch
from weather_server import Weather


class Mytest(unittest.TestCase):
    @patch('requests.get')
    def test_get_city_weather(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'main': {'temp': 20,
                     'feels_like': 33
                     }
        }
        weather = Weather('tehran')
        a = weather.get_city_weather()
        self.assertEqual(a.temp, 20)
        self.assertEqual(a.feels_like, 33)
        self.assertIsInstance(a.lst_update, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
