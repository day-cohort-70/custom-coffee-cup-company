import sqlite3
import json
from nss_handler import status


class OrderView:

    def get(self, url):
        with sqlite3.connect("coffee.sqlite3") as connection:
            connection = sqlite3.connect("coffee.sqlite3")
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
                s.SizeID,
                s.Price AS SizePrice,
                m.Price AS MilkPrice,
                GROUP_CONCAT(f.FlavorID || '|' || f.Description || '|' || f.Price, ',') AS Flavors
            FROM Orders o
            JOIN Milks m ON m.MilkID = o.ChosenMilkID
            JOIN Sizes s ON s.SizeID = o.ChosenSizeID
            JOIN OrderFlavors of ON of.OrderID = o.OrderID
            JOIN Flavors f ON f.FlavorID = of.FlavorID
            GROUP BY o.OrderID, o.ChosenMilkID, o.ChosenSizeID, m.Description, m.MilkID, s.Description, s.SizeID, s.Price, m.Price;
            """

            cursor.execute(query)
            rows = cursor.fetchall()

            orders = []
            for row in rows:
                order = {
                    "id": row["OrderID"],
                    "milkId": row["ChosenMilkID"],
                    "sizeId": row["ChosenSizeID"]
                }

                if "_expand" in url["query_params"]:
                    for resource in url["query_params"]["_expand"]:
                        if resource == "milk":
                            order["milk"] = {
                                "milkId": row["MilkID"],
                                "description": row["MilkDescription"],
                                "price": row["MilkPrice"],
                            }
                        if resource == "size":
                            order["size"] = {
                                "sizeId": row["SizeID"],
                                "description": row["SizeDescription"],
                                "price": row["SizePrice"],
                            }
                        if resource == "flavors":
                            flavors_list = row["Flavors"].split(',')
                            flavors = []
                            for flavor in flavors_list:
                                flavor_id, description, price = flavor.split('|')
                                flavors.append({
                                    "id": int(flavor_id),
                                    "description": description,
                                    "price": float(price)
                                })
                            order["flavors"] = flavors

                orders.append(order)

            return json.dumps(orders)

    def create(self, request_body):
        with sqlite3.connect("coffee.sqlite3") as connection:
            connection = sqlite3.connect("coffee.sqlite3")
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

            param_values = (request_body["milkId"], request_body["sizeId"])

            cursor.execute(query, param_values)
            new_order_id = cursor.lastrowid

            for flavor_id in request_body["flavors"]:
                query = """
                INSERT INTO OrderFlavors
                (
                    OrderID,
                    FlavorID
                )
                VALUES ( ?, ? )
                """

                param_values = (new_order_id, flavor_id)

                cursor.execute(query, param_values)

            connection.commit()

        return json.dumps(
            {
                "OrderId": new_order_id,
                "ChosenMilkId": request_body["milkId"],
                "ChosenSizeId": request_body["sizeId"],
                "Flavors": request_body["flavors"],
            }
        )
