import sqlite3
import json


class FlavorView:

    def get(self, url):
        with sqlite3.connect('coffee.sqlite3') as connection:
            connection = sqlite3.connect('coffee.sqlite3')
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()

            query = "SELECT * FROM Flavors"
            cursor.execute(query)
            rows = cursor.fetchall()

            flavors = []
            for row in rows:
                flavors.append(dict(row))

        return json.dumps(flavors)
