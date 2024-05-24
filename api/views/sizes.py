import sqlite3
import json


class SizeView:

    def get(self, url):
        with sqlite3.connect('coffee.sqlite3') as connection:
            connection = sqlite3.connect('coffee.sqlite3')
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()

            query = "SELECT * FROM Sizes"
            cursor.execute(query)
            rows = cursor.fetchall()

            sizes = []
            for row in rows:
                sizes.append(dict(row))

        return json.dumps(sizes)
