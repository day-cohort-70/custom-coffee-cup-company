import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status


# Add your imports below this line
from views import MilkView, OrderView, SizeView, FlavorView


class JSONServer(HandleRequests):

    def do_GET(self):
        url = self.parse_url(self.path)
        view = self.determine_view(url)

        try:
            json_data = view.get()
            return self.response(json_data, status.HTTP_200_SUCCESS.value)
        except AttributeError:
            return self.response("No view for that route", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

    def do_POST(self):
        # Parse the URL
        url = self.parse_url(self.path)

        # Determine the correct view needed to handle the requests
        view = self.determine_view(url)

        # Get the request body
        body = self.get_request_body()

        # Invoke the correct method on the view
        json_of_new_order = view.create(body)

        # Once you implement this method, delete the following line of code
        return self.response(json_of_new_order, status.HTTP_201_SUCCESS_CREATED.value)


    def determine_view(self, url):
        """Lookup the correct view class to handle the requested route

        Args:
            url (dict): The URL dictionary

        Returns:
            Any: An instance of the matching view class
        """
        try:
            routes = {
                "milks": MilkView,
                "flavors": FlavorView,
                "orders": OrderView,
                "sizes": SizeView
            }

            matching_class = routes[url["requested_resource"]]
            return matching_class()
        except KeyError:
            return status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value








#
# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ''
    port = 9000
    HTTPServer((host, port), JSONServer).serve_forever()

if __name__ == "__main__":
    main()