from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    # https://restcountries.com/v3.1/name/peru

    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_list = parse.parse_qsl(url_components.query) # returns list, ['name', 'peru']
        dictionary = dict(query_list)  # turns list into dict

        if 'name' in dictionary:
            query = dictionary['name']
            url = "https://restcountries.com/v3.1/name/"
            complete_url = url + dictionary['name']
            # print(complete_url + ' this is your URL')
            response = requests.get(complete_url)
            data = response.json()
            capital = data[0]['capital'] # index's to the capital city.

            # print(capital + " this is your capital")
            message = str(capital[0])
            final = f'the capital of {query} is {message}'
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(final.encode())

        else:
            message = "Type a country in the query to get its capital city."

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
        return