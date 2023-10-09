import unittest, sqlite3
from database import WeatherDatabase


class DataTest(unittest.TestCase):
    def test_connect(self):
        weather_object = WeatherDatabase()
        WeatherDatabase.save_request_data('tehran', '1402')
        list_dict = {'main': {
            'temp': 2.9,
            'feels_like': 6.9
        }
        }
        WeatherDatabase.save_response_data('tehran', list_dict)
        WeatherDatabase.c.execute("SELECT * FROM requests order by id desc")
        results = WeatherDatabase.c.fetchall()
        self.assertEqual(results[0][1], 'tehran')
        self.assertEqual(results[0][2], '1402')
        WeatherDatabase.c.execute("SELECT * FROM response order by id desc")
        results = WeatherDatabase.c.fetchall()
        self.assertEqual(results[0][1], 'tehran')
        self.assertEqual(results[0][2], 2.9)
        self.assertEqual(results[0][3], 6.9)
        # WeatherDatabase.c.execute("SELECT * FROM connect  order by id desc")
        #         # results = WeatherDatabase.c.fetchall()
        #         # self.assertEqual(results[0][1], 0)
        #         # self.assertEqual(results[0][2], 1)
        #         # self.assertEqual(results[0][2], 1)


if __name__ == '__main__':
    unittest.main()
