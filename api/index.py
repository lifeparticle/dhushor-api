from http.server import BaseHTTPRequestHandler
from urllib import parse
from urllib.request import Request, urlopen
import os

class handler(BaseHTTPRequestHandler):

	def do_GET(self):
		s = self.path
		dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
		self.send_response(200)
		self.send_header('Content-type','application/json; charset=utf-8')
		self.send_header('Access-Control-Allow-Origin', '*')
		self.end_headers()

		hdr = {}

		if "name" in dic:
			if dic["name"] == "unsplash":
				url = 'https://api.unsplash.com/search/photos?page='+dic['page']+'&per_page=12&orientation=landscape&query='+dic['query']+'&client_id='+os.environ['unsplash_client_id']'
			if dic["name"] == "pexels":
				url = 'https://api.pexels.com/v1/search?query='+dic['query']+'&per_page=12&orientation=landscape&page='+dic['page']
				hdr = {'Authorization': os.environ['pexels_authorization'], "User-Agent": "Mozilla/5.0"}
		else:
			message = "Hello, stranger!"

		self.wfile.write(urlopen(Request(url, headers=hdr)).read())
		return