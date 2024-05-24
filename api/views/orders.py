import sqlite3
import json
from nss_handler import status


class OrderView():

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
