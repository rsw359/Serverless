from ast import parse
from email import message
from hashlib import algorithms_available
from http.server import BaseHTTPRequestHandler

from pyparsing import Path

path = self.path
url_components = parse.urlsplit(Path)
query_string_list = parse.parseqsl(url_components.query)
dic = dict(query_string_list)