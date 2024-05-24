import sqlite3
import json


class MilkView:

    def get(self, url):
        with sqlite3.connect('coffee.sqlite3') as connection:
            connection = sqlite3.connect('coffee.sqlite3')
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()

            query = "SELECT * FROM Milks"
            cursor.execute(query)
            rows = cursor.fetchall()

            milks = []
            for row in rows:
                milks.append(dict(row))

        return json.dumps(milks)
