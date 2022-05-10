from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_string_list)

        if "name" in dictionary:
            url = "https://restcountries.com/v3.1/name/"
            request = requests.get(url + dictionary["name"])
            data = request.json()

            country_name = str(data[0]["name"]['common'])
            capital_name = str(data[0]["capital"][0])
            message = f"The capital of {country_name} is {capital_name}"
        elif "capital" in dictionary:
            url = "https://restcountries.com/v3.1/capital/"
            request = requests.get(url + dictionary["capital"])
            data = request.json()

            country_name = str(data[0]["name"]['common'])
            capital_name = str(data[0]["capital"][0])
            message = f"{capital_name} is the capital of {country_name}"

        else:
            message = "Please enter a country name"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return
