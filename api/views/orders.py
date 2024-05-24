import sqlite3
import json
from nss_handler import status


class OrderView():

    def get(self):
        with sqlite3.connect('coffee.sqlite3') as connection:
            connection = sqlite3.connect('coffee.sqlite3')
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()

            query = """
            SELECT
                o.OrderID,
                o.ChosenMilkID,
                o.ChosenSizeID,
                m.Description AS MilkDescription,
                m.MilkID,
                s.Description AS SizeDescription,
                s.SizeID
            FROM Orders o
            JOIN Milks m ON m.MilkID = o.ChosenMilkID
            JOIN Sizes s ON s.SizeID = o.ChosenSizeID
            """
            cursor.execute(query)
            rows = cursor.fetchall()

            orders = []
            for row in rows:
                order = {
                    'id': row['OrderID'],
                    'size': {
                        'sizeId': row['SizeID'],
                        'description': row['SizeDescription']
                    },
                    'milk': {
                        'milkId': row['MilkID'],
                        'description': row['MilkDescription']
                    }
                }
                orders.append(order)

        return json.dumps(orders)

    def create(self, request_body):
        with sqlite3.connect('coffee.sqlite3') as connection:
            connection = sqlite3.connect('coffee.sqlite3')
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()

            query = """
            INSERT INTO Orders
            (
                ChosenMilkID,
                ChosenSizeID
            )
            VALUES ( ?, ? )
            """

            param_values = ( request_body['milkId'], request_body['sizeId'] )

            cursor.execute(query, param_values)
            new_order_id = cursor.lastrowid

            for flavor_id in request_body['flavors']:
                query = """
                INSERT INTO OrderFlavors
                (
                    OrderID,
                    FlavorID
                )
                VALUES ( ?, ? )
                """

                param_values = ( new_order_id, flavor_id )

                cursor.execute(query, param_values)

            connection.commit()

        return json.dumps({
            'OrderId': new_order_id,
            'ChosenMilkId': request_body['milkId'],
            'ChosenSizeId': request_body['sizeId'],
            'Flavors': request_body['flavors']
        })
