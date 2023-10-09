import sqlite3, datetime


# cnt = sqlite3.connect("weather.db")
# c = cnt.cursor()
#
# #
# # c.execute("""
# #     CREATE TABLE requests(id INTEGER PRIMARY KEY AUTOINCREMENT, city_name varchar(20),request_time varchar(250));
# # """)
# #
# # c.execute("""
# #    CREATE TABLE response(id INTEGER PRIMARY KEY AUTOINCREMENT, city_name varchar(20), temp DECIMAL(3,4),
# #     feel_likes DECIMAL(3,4),last_update varchar(250));
# # """)
# #
# # c.execute("""
# #    CREATE TABLE connect(id INTEGER PRIMARY KEY AUTOINCREMENT, sucessfully INTEGER  ,response_id INTEGER ,
# #     requests_id INTEGER ,
# #     FOREIGN KEY (response_id) REFERENCES response(id),
# #     FOREIGN KEY (requests_id) REFERENCES requests(id));
# # """)
# def max_id():
#     c.execute("""
#        SELECT max(id) FROM requests
#     """)
#     id = c.fetchone()
#     # print(id[0])
#     return id[0]


# print(max_id())


class WeatherDatabase:
    cnt = sqlite3.connect("weather.db")
    c = cnt.cursor()
    id = None

    def __init__(self):
        # def setup(self):
        #     self.cnt = sqlite3.connect("weather2.db")
        #     self.c = self.cnt.cursor()
        pass

    @classmethod
    def cursor_set(cls):
        cls.c.execute("""
            CREATE TABLE requests(id INTEGER PRIMARY KEY AUTOINCREMENT, city_name varchar(20),request_time varchar(250));
        """)

        cls.c.execute("""
           CREATE TABLE response(id INTEGER PRIMARY KEY AUTOINCREMENT, city_name varchar(20), temp DECIMAL(3,4),
            feel_likes DECIMAL(3,4),last_update varchar(250));
        """)

        cls.c.execute("""
           CREATE TABLE connect(id INTEGER PRIMARY KEY AUTOINCREMENT, sucessfully INTEGER  ,response_id INTEGER ,
            requests_id INTEGER ,
            FOREIGN KEY (response_id) REFERENCES response(id),
            FOREIGN KEY (requests_id) REFERENCES requests(id));
        """)

    @classmethod
    def max_id(cls):
        cls.c.execute("""
           SELECT max(id) FROM requests
        """)
        cls.id = cls.c.fetchone()
        # print(id[0])
        return cls.id[0]

    @classmethod
    def save_request_data(cls, city_name: str, request_time: str):
        cls.c.execute('INSERT INTO requests(city_name,request_time) VALUES (?, ?);',
                      (city_name, request_time))
        cls.cnt.commit()

    @classmethod
    def save_response_data(cls, city_name: str, response_data: dict):
        cls.c.execute('INSERT INTO response(city_name,temp,feel_likes,last_update) VALUES (?, ?,?,?);',
                      (city_name, response_data["main"]["temp"], response_data["main"]["feels_like"],
                       str(datetime.datetime.now())))
        cls.cnt.commit()

    @classmethod
    def save_connect(cls, successfully_: int):
        cls.c.execute('INSERT INTO connect(sucessfully,response_id,requests_id) VALUES (?, ?, ?);'
                      , (successfully_, cls.max_id(), cls.max_id()))
        cls.cnt.commit()

    @classmethod
    def get_request_count(cls):
        cls.c.execute("""
                   SELECT COUNT(id) FROM requests
                """)
        counter = cls.c.fetchone()
        return counter[0]

    @classmethod
    def get_successful_request_count(cls):
        cls.c.execute("""
                           SELECT COUNT(id) FROM connect WHERE sucessfully=0
                        """)
        counter = cls.c.fetchone()
        return counter[0]


if __name__ == '__main__':
    data = WeatherDatabase()
    WeatherDatabase.cursor_set()
